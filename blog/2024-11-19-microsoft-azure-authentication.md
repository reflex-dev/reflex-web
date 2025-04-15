---
author: Tom Gotsman
date: 2024-11-19
title: Microsoft Azure Auth
description: Implementing Microsoft Azure Single Sign-On (SSO) Auth in Reflex app.
image: /blog/azure_auth.webp
meta: [
    {
      "name": "keywords",
      "content": "
        data-driven web apps,
        modern web application development,
        python data visualization,
        python fintech applications,
        python web development,
      "
    },
]
---


```python exec
from pcweb.pages import docs
```

Authentication is a critical requirement for most internal company web applications. While building features and functionality is exciting, ensuring secure access control often becomes a necessary next step. For organizations already using Microsoft's ecosystem, this blog post will guide you through setting up Reflex authentication (SSO) with Microsoft Azure.


## Variables to Set

Before we begin, you will need the following imports and to set the following variables:

```python
import msal
import reflex as rx
from typing import Dict, List, Optional


client_id: str = "0df2a88e-####-####-####-#########373"
client_secret: str = "TPO8Q~dlz###########################"
tenant_id: str = "f2c9cbbe-####-####-####-#########d6d"

# This tells which company is issuing your credentials
authority = f"https://login.microsoftonline.com/\{tenant_id}"
# Customizable to where the user after login will get re-directed
login_redirect = "/"
# Creates an in-memory cache for storing tokens
cache = msal.TokenCache()
```

The Microsoft Authentication Library (MSAL) for Python library enables you to sign in users or apps with Microsoft identities. 

The values you should get from your Azure portal / SSO team at your company are `client_id`, `client_secret`, and `tenant_id`. These values are unique to your application and company.

It is recommended to retrieve these values from environment variables or from a configuration file (they are just hardcoded for the example for simplicity).

Next we have to set the `sso_app` variable, which is the client application that will be used to authenticate users.

```python
sso_app = msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority,
    token_cache=cache,
)
```


## Getting to the Azure Sign-In Page

Our `State` class has three state variables `_access_token`, `_flow`, and `_token`. 

The `_access_token` is the token that allows you to interact with Microsoft applications and access data from Microsoft that is relevant to you. The `_flow` variable is used to initiate the authentication flow, and the _token variable stores the the decoded token and claims that is returned from Microsoft. All of these variables are [backend variables]({docs.vars.base_vars.path}#backend-only-vars) and therefore the user cannot change these via the UI.  {docs.vars.base_vars.path}

When we land on the home page, and we are not logged in, instantly the `require_auth` event handler is called, which checks if the `_token` variable is empty. As we are not logged in yet, the `_token` variable is empty, and the `redirect_sso` event handler is called.

This event handler initiates the authentication flow and redirects the user to the Microsoft sign-in page. It also sets the `redirect_uri` to be the port serving the current page, using `self.router.page.host`, plus `/callback`. The `redirect_uri` is where you want to re-direct microsoft to do the auth (i.e. the app page that takes the azure info and parses out who you are before setting your tokens) You can learn more about `state.router` and how it works [here]({docs.utility_methods.router_attributes.path}).

```python
class State(rx.State):
    _access_token: str = "" # _access_token has an expiration date and allows you to interact with microsoft applications and access data from microsoft that is relevant to you
    _flow: dict # do not touch this
    _token: Dict[str, str] = \{}
 
    def redirect_sso(self, scope: Optional[List] = None) -> rx.Component:
        if scope is None:
            scope = []
        self._flow = sso_app.initiate_auth_code_flow(
            scopes=scope, redirect_uri=f"\{self.router.page.host}/callback"
        )
        # this redirect sends you to microsoft 
        return rx.redirect(self._flow["auth_uri"])

    def require_auth(self):
        if not self._token:
            return self.redirect_sso()


@rx.page(route="/", on_load=State.require_auth)
def home() -> rx.Component:
    return rx.container(...)
```


## Validate the Login

Once the user is finished signing in on the Microsoft sign-in page, they are redirected back to the `redirect_uri` that we set earlier. This is the `/callback` page. 

This page has an `on_load` event trigger that calls the `callback` event handler when the page is loaded. The `callback` event handler retrieves the query parameters from the URL and uses them to authenticate the user, by setting the `_access_token` and the `_token`. 

Finally the user is redirected to the `login_redirect` page, which in this example is the home page. You are now logged in.


```python
class State(rx.State):
    _access_token: str = "" 
    _flow: dict
    _token: Dict[str, str] = \{}

    def callback(self):
        query_components = self.router.page.params

        auth_response = {
            "code": query_components.get("code"),
            "client_info": query_components.get("client_info"),
            "state": query_components.get("state"),
            "session_state": query_components.get("session_state"),
            "client-secret": client_secret,
        }
        try:
            result = sso_app.acquire_token_by_auth_code_flow(
                self._flow, auth_response, scopes=[]
            )
        except Exception as e:
            return rx.toast(f"error something went wrong")
        # this can be used for accessing graph
        self._access_token = result.get("access_token")
        self._token = result.get("id_token_claims")
        return rx.redirect(login_redirect)



@rx.page(route="/callback", on_load=State.callback)
def callback() -> rx.Component:
    return rx.container()
```


## Logging into the App

Now that we have all our tokens set correctly, when we redirect back to the home page, again the `require_auth` event handler is called. This time, the `_token` variable is not empty and so the page renders.

The page contains an [`rx.cond`]({docs.components.conditional_rendering.path}) component that checks if the user is authenticated. It runs the `check_auth` [computed var]({docs.vars.computed_vars.path}), which returns `True` if the `_token` variable is not empty and `False` otherwise.

If the user is authenticated, the `auth_view` component is rendered. If the user is not authenticated, the `unauth_view` component is rendered. The `auth_view` component displays a welcome message with the user's name from the `token` [computed var]({docs.vars.computed_vars.path}), which returns the `_token` [backend variable]({docs.vars.base_vars.path}#backend-only-vars).


```python
class State(rx.State):
    _access_token: str = ""
    _flow: dict
    _token: Dict[str, str] = \{}

    def require_auth(self):
        if not self._token:
            return self.redirect_sso()

    @rx.var(cache=True)
    def check_auth(self) -> bool:
        return True if self._token else False

    @rx.var(cache=True)
    def token(self) -> Dict[str, str]:
        return self._token



@rx.page(route="/", on_load=State.require_auth)
def home() -> rx.Component:
    return rx.container(rx.cond(State.check_auth, auth_view(), unauth_view()))


def auth_view() -> rx.Component:
    return rx.text(f"Hello \{State.token['name']}")


def unauth_view() -> rx.Component:
    return rx.text("Unauthorized, redirected...")
```


## Logging Out

Lastly we have the logout functionality. When the user goes to the `/logout` page the `logout` event handler is called. This event handler clears the `_token` variable and redirects the user to the Microsoft logout page. This event handler could also easliy be put on the `on_click` event of a button.

```python
class State(rx.State):
    _access_token: str = "" 
    _flow: dict 
    _token: Dict[str, str] = \{}

    def logout(self):
        self._token = \{}
        return rx.redirect(authority + "/oauth2/v2.0/logout")


@rx.page(route="/logout", on_load=State.logout)
def logout() -> rx.Component:
    return rx.container("Logged out")
```

## Putting it all together

The full code is shown below and in this [git repo](https://github.com/reflex-dev/reflex-examples/tree/main/azure_auth). In this final code we have broken the app down into two different pages, with our state class in `azure_auth/azure_auth/auth/core.py` and the pages in `azure_auth/azure_auth/azure_auth.py`.

Overall the final workflow is as follows:

1. The user lands on the home page (localhost:3000) while not logged in.
2. This runs the `require_auth` event handler and then the `redirect_sso` event handler.
3. This redirects the user to the Microsoft sign-in page.
4. After the user completes the Microsoft sign-in, they are redirected back to the `/callback` page based on the `redirect_uri`.
5. The `callback` event handler is called, which parses out info sent back from Microsoft and validates it and stores it in `_token` and `_access_token`.
6. The user is then redirected back to the home page based on the `login_redirect`.
7. The `require_auth` event handler is called again, but this time the user is authenticated and the page renders.
8. As the `check_auth` computed var inside of the `rx.cond` returns `True`, the `auth_view` component is rendered, displaying the user's name.
9. On logout the `logout` event handler sets `self._token` to an empty dictionary and redirects to Microsoft logout page which forces the everything about the login state to be invalid.

```python
# azure_auth/azure_auth/auth/core.py
import msal
import reflex as rx
from typing import Dict, List, Optional


client_id: str = "0df2a88e-####-####-####-#########373"
client_secret: str = "TPO8Q~dlz###########################"
tenant_id: str = "f2c9cbbe-####-####-####-#########d6d"
authority = f"https://login.microsoftonline.com/\{tenant_id}"
login_redirect = "/"
cache = msal.TokenCache()


sso_app = msal.ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority,
        token_cache=cache,
    )

class State(rx.State):
    _access_token: str = ""
    _flow: dict
    _token: Dict[str, str] = \{}

    def redirect_sso(self, scope: Optional[List] = None) -> rx.Component:
        if scope is None:
            scope = []
        self._flow = sso_app.initiate_auth_code_flow(
            scopes=scope, redirect_uri=f"\{self.router.page.host}/callback"
        )
        return rx.redirect(self._flow["auth_uri"])

    def require_auth(self):
        if not self._token:
            return self.redirect_sso()

    @rx.var(cache=True)
    def check_auth(self) -> bool:
        return True if self._token else False

    @rx.var(cache=True)
    def token(self) -> Dict[str, str]:
        return self._token

    def logout(self):
        self._token = \{}
        return rx.redirect(authority + "/oauth2/v2.0/logout")

    def callback(self):
        query_components = self.router.page.params

        auth_response = {
            "code": query_components.get("code"),
            "client_info": query_components.get("client_info"),
            "state": query_components.get("state"),
            "session_state": query_components.get("session_state"),
            "client-secret": client_secret,
        }
        try:
            result = sso_app.acquire_token_by_auth_code_flow(
                self._flow, auth_response, scopes=[]
            )
        except Exception as e:
            return rx.toast(f"error something went wrong")
        # this can be used for accessing graph
        self._access_token = result.get("access_token")
        self._token = result.get("id_token_claims")
        return rx.redirect(login_redirect)
```

```python
# azure_auth/azure_auth/azure_auth.py
import reflex as rx
from azure_auth.auth.core import State as SsoState


@rx.page(route="/callback", on_load=SsoState.callback)
def callback() -> rx.Component:
    return rx.container()


@rx.page(route="/logout", on_load=SsoState.logout)
def logout() -> rx.Component:
    return rx.container("Logged out")


@rx.page(route="/", on_load=SsoState.require_auth)
def home() -> rx.Component:
    return rx.container(rx.cond(SsoState.check_auth, auth_view(), unauth_view()))


def auth_view() -> rx.Component:
    return rx.text(f"Hello \{SsoState.token['name']}")


def unauth_view() -> rx.Component:
    return rx.text("Unauthorized, redirected...")
```
