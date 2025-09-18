---
author: Masen Furer
date: 2023-10-25
title: "Implementing Sign In with Google"
description: "How to wrap a third-party auth component and integrate it into a Reflex app."
image: /blog/google_auth.webp
meta: [
    {"name": "keywords", "content": ""},
]
---

```python exec
import reflex as rx
from pcweb.pages.docs import api_reference, state
```

Almost any non-trivial web app needs a way to identify and authenticate users,
but Reflex does not provide this functionality out of the box because there are
way too many different ways to approach the problem. Thanks to the plethora of
existing React components for performing auth, a wrapper can be created to
include most third-party auth solutions within a Reflex app.

In this post, I'll walk through how I set up a Google API project and wrapped
`@react-oauth/google` to provide Sign In with Google functionality in my Reflex
app.

## Create a Google OAuth Client ID

Head over to
[https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)
and sign in with the Google account that should manage the app and credential tokens.

* Click "Create Project" and give it a name. After creation the new project should be selected.
* Click "Configure Consent Screen", Choose "External", then Create.
  * Enter App Name and User Support Email -- these will be shown to users when logging in
  * Scroll all the way down to "Developer contact information" and add your email address, click "Save and Continue"
  * Click "Add or Remove Scopes"
    * Select "Email", "Profile", and "OpenID Connect"
    * Click "Update", then "Save and Continue"
  * Add any test users that should be able to log in during development.
* From the "Credentials" page, click "+ Create Credentials", then "OAuth client ID"
  * Select Application Type: "Web Application"
  * Add Authorized Javascript Origins: `http://localhost`, `http://localhost:3000`, `https://example.com` (prod domain must be HTTPS)
  * Click "Save"
* Copy the OAuth "Client ID" and save it for later. Mine looks like `309209880368-4uqd9e44h7t4alhhdqn48pvvr63cc5j5.apps.googleusercontent.com`

```python eval
rx.center(
    rx.video(url="https://github.com/reflex-dev/reflex-examples/assets/1524005/af2499a6-0bda-4d60-b52b-4f51b7322fd5"),
    rx.box(height="3em"),
    width="100%",
    padding_y="2em"
)
```

## Wrap @react-oauth/google

The [`@react-oauth/google`](https://github.com/MomenSherif/react-oauth)
package provides a React component that handles all of the interaction with
Google's OAuth API. It has rich functionality and many options, but for the
purposes of this post, we will only wrap the props needed to get basic login
working.

### GoogleOAuthProvider

The `GoogleOAuthProvider` component is responsible for downloading Google's SDK
and supplying the Client ID.

Create a new file in your app directory, `react_oauth_google.py`.

```python
import reflex as rx

class GoogleOAuthProvider(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleOAuthProvider"

    client_id: rx.Var[str]
```

```md alert
# Why client_id and not clientID

When Reflex compiles the component to Javascript, `snake_case` property names are automatically formatted as `camelCase`, although the names may be defined in `camelCase` as well.
```
### GoogleLogin

The `GoogleLogin` component renders the familiar "Sign in with Google" button.

Since we will use the default configuration, no props are needed, however the
event trigger does need to be defined so our Reflex app is able to get the token
after logging in.

Define the following wrapper in the same `react_oauth_google.py`.

```python
class GoogleLogin(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleLogin"

    on_success: rx.EventHandler[lambda data: [data]]
```

The `on_success` trigger is defined to pass its argument directly to the Reflex
event handler.

## Handling the Token

```md alert warning
# Always use TLS in production",

The user's token may be compromised if sent over an insecure websocket!
```

An event handler will be used to receive the token after a successful login.
Critically, the token must be verified and decoded to access the user
information it contains.

### google-auth

The simplest way to verify the token is to use Google's own `google-auth` python
library. Add `google-auth[requests]` to your app's `requirements.txt` and install it with
`pip install -r requirements.txt`.

Add the necessary imports to the module where your app `State` is defined and
set the `CLIENT_ID` saved earlier, as it is needed to verify the token.

```python
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

CLIENT_ID = "309209880368-4uqd9e44h7t4alhhdqn48pvvr63cc5j5.apps.googleusercontent.com"
```

### on_success

The `on_success` trigger is fired by `GoogleLogin` after a successful login, and it contains the `id_token` that provides user information. For now, this event handler will verify the token and dump its contents to the console to verify that it is working.

```python
class State(rx.State):
    ...
    def on_success(self, id_token: dict):
        print(
            verify_oauth2_token(
                id_token["credential"],
                requests.Request(),
                CLIENT_ID
            )
        )
```

## Logging In

With this minimal functionality in place, it should be possible to log in with
one of the test accounts defined earlier on the Consent Screen configuration.

Add the `GoogleOAuthProvider` and `GoogleLogin` components linked with the
previously defined `CLIENT_ID` and `State.on_success` event handler to test the
functionality so far.

```python
from .react_oauth_google import GoogleOAuthProvider, GoogleLogin

def index():
    return rx.vstack(
        GoogleOAuthProvider.create(
            GoogleLogin.create(on_success=State.on_success),
            client_id=CLIENT_ID
        )
    )

app = rx.App()
app.add_page(index)
```

After a successful login, you will see the decoded [JSON Web Token
(JWT)](https://jwt.io) with user profile information displayed in the terminal!

## Saving the Token

The `GoogleLogin` component does NOT store the token in any way, so it is up to
our app to store and manage the credential after login. For this purpose, we
will use an
[`rx.LocalStorage`]({api_reference.browser_storage.path}) `Var` in the
[`State`]({state.overview.path}) that is set in the
`on_success` event handler.

Additionally, an `rx.var` will be used to verify and return the decoded
token info for the frontend to use.

Finally, a new `logout` event handler will be defined to clear out the saved token
and effectively log the user out of the app.

```python
import json
from typing import Any

class State(rx.State):
    id_token_json: str = rx.LocalStorage()

    def on_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    @rx.var(cache=True)
    def tokeninfo(self) -> dict[str, Any]:
        try:
            return verify_oauth2_token(
                json.loads(self.id_token_json)["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception as exc:
            if self.id_token_json:
                print(f"Error verifying token: \{exc}")
        return \{}

    def logout(self):
        self.id_token_json = ""
```

### Checking Token Validity

For convenience, a `token_is_valid` computed var can be defined to return a
simple `bool` if the token is valid or not. This is specifically not a
cached var because it should be re-evaluated every time it is accessed, in
case the expiry time has passed.

```python
import time

class State(rx.State):
    ...
    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo
                and int(self.tokeninfo.get("exp", 0)) > time.time()
            )
        except Exception:
            return False
```

## Rendering User Info

With the decoded token data provided in the state, we can render the user's
name, email, avatar, and provide a logout button.

```python
def user_info(tokeninfo: dict) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            name=tokeninfo["name"],
            src=tokeninfo["picture"],
            size="lg",
        ),
        rx.vstack(
            rx.heading(tokeninfo["name"], size="md"),
            rx.text(tokeninfo["email"]),
            align_items="flex-start",
        ),
        rx.button("Logout", on_click=State.logout),
        padding="10px",
    )
```

## Requiring Login

Now that the user's token is stored in the state, its absence can be used to
prompt for login on protected pages. For this purpose, we will define a
decorator that can be applied to any page function which shows a login button if
the user token is not valid.

First define the `login` component that will be shown to unauthenticated users.

```python
def login() -> rx.Component:
    return rx.vstack(
        GoogleLogin.create(on_success=State.on_success),
    )
```

Then define the decorator that will wrap page components.

```python
import functools

def require_google_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(
                State.is_hydrated,
                rx.cond(State.token_is_valid, page(), login()),
                rx.spinner(),
            ),
            client_id=CLIENT_ID,
        )
    return _auth_wrapper
```

```md alert
# Why two rx.cond?

The first rx.cond checks if the State is hydrated, meaning the frontend has access to the latest state values from the backend.
Before hydration, we show a loading spinner instead of flashing a login button to users that may already logged in without the frontend being aware of it yet.
```

### Protecting Content

Content that should never be available to unauthenticated users, must be
returned from a computed var that checks token validity.

```python
class State(rx.State):
    ...
    @rx.var(cache=True)
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"This content can only be viewed by a logged in User. Nice to see you \{self.tokeninfo['name']}"
        return "Not logged in."
```

```md alert warning
# Private data must come from the State

Reflex compiles the page function and makes its content publicly accessible!
Although conditional rendering is used to show the login button to unauthenticated users, the source code of the page will also be available to unauthenticated users.

Because of this, all private content must originate from the State and only be returned after verifying the user's token is valid on the backend.
```

### Show Login Button

The decorator may be applied to any function that returns an `rx.Component` to
give the user a chance to authenticate.

```python
@rx.page(route="/protected")
@require_google_login
def protected() -> rx.Component:
    return rx.vstack(
        user_info(State.tokeninfo),
        rx.text(State.protected_content),
        rx.link("Home", href="/"),
    )
```

## Putting the Pieces Together

The production code for this example has been published as a reuable third-party
component, [`reflex-google-auth`](https://github.com/masenf/reflex-google-auth)
and can be used directly in any Reflex app.

### react_oauth_google.py

```python
import reflex as rx


class GoogleOAuthProvider(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleOAuthProvider"

    client_id: rx.Var[str]


class GoogleLogin(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleLogin"

    on_success: rx.EventHandler[lambda data: [data]]
```

### google_auth.py

```python
import functools
import json
import os
import time
from typing import Any

from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

import reflex as rx

from .react_oauth_google import GoogleOAuthProvider, GoogleLogin

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")


class State(rx.State):
    id_token_json: str = rx.LocalStorage()

    def on_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    @rx.var(cache=True)
    def tokeninfo(self) -> dict[str, Any]:
        try:
            return verify_oauth2_token(
                json.loads(self.id_token_json)["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception as exc:
            if self.id_token_json:
                print(f"Error verifying token: \{exc}")
        return \{}

    def logout(self):
        self.id_token_json = ""

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo
                and int(self.tokeninfo.get("exp", 0)) > time.time()
            )
        except Exception:
            return False

    @rx.var(cache=True)
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"This content can only be viewed by a logged in User. Nice to see you \{self.tokeninfo['name']}"
        return "Not logged in."


def user_info(tokeninfo: dict) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            name=tokeninfo["name"],
            src=tokeninfo["picture"],
            size="lg",
        ),
        rx.vstack(
            rx.heading(tokeninfo["name"], size="md"),
            rx.text(tokeninfo["email"]),
            align_items="flex-start",
        ),
        rx.button("Logout", on_click=State.logout),
        padding="10px",
    )


def login() -> rx.Component:
    return rx.vstack(
        GoogleLogin.create(on_success=State.on_success),
    )


def require_google_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(
                State.is_hydrated,
                rx.cond(State.token_is_valid, page(), login()),
                rx.spinner(),
            ),
            client_id=CLIENT_ID,
        )
    return _auth_wrapper


def index():
    return rx.vstack(
        rx.heading("Google OAuth", size="lg"),
        rx.link("Protected Page", href="/protected"),
    )


@rx.page(route="/protected")
@require_google_login
def protected() -> rx.Component:
    return rx.vstack(
        user_info(State.tokeninfo),
        rx.text(State.protected_content),
        rx.link("Home", href="/"),
    )


app = rx.App()
app.add_page(index)
```

### Demo

```python eval
rx.center(
    rx.video(url="https://github.com/reflex-dev/reflex-examples/assets/1524005/b0c7145b-6c19-4072-bc9d-ae8927c8988f"),
    rx.box(height="3em"),
    width="100%",
    padding_y="2em"
)
```

🔐 Happy Building 🚀

-- Reflex Team
