```python exec
import reflex as rx
```

# Architecture

This page provides an technical overview of the Reflex internals. You don't need to understand this to use Reflex, but it can be helpful if you want to contribute to Reflex development, or if you're just interested in how Reflex works under the hood.

We will use a basic app that displays Github profile images as an example to explain the different parts of the architecture.

```python demo exec
import reflex as rx

class GithubState(rx.State):
    username: str = "reflex-dev"

    def set_username(self, username: str):
        self.username = username


def index():
    return rx.hstack(
        rx.avatar(src=f"https://github.com/{GithubState.username}.png"),
        rx.input(
            placeholder="Enter your username",
            on_blur=GithubState.set_username,
        ),
    )
```

## TLDR

Reflex is a framework to build full-stack web apps in pure Python.
We handle the frontend, backend, and deployment of your app, so you can focus more on your ideas and less on the technical details.

Reflex apps compile down to a [Next.js](https://github.com/vercel/next.js) frontend app and a [FastAPI](https://github.com/tiangolo/fastapi) backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses websockets to send events from the frontend to the backend, and to send state updates from the backend to the frontend.

The diagram below shows a detailed overview of how a Reflex app works.
We'll go through each part in more detail in the following sections.

![Reflex Architecture](/architecture.png)

## Frontend

Reflex frontends compile down to Javascript, and are run using [Node.js](https://nodejs.org/en).
The very first time you run `reflex`, we install a `node` runtime and a package manager ([npm](https://www.npmjs.com) on Windows and [Bun](https://bun.sh) on Linux and MacOS) to manage the frontend dependencies. 

When you run `reflex init`, Reflex creates a `.web` directory in your project, which contains the Next.js app with your compiled frontend code. This directory is automatically managed by Reflex, and you shouldn't modify it, but it can be useful for debugging.

When you `reflex run`, the frontend is served on a port (by default 3000) and you can access it in your browser.

### Components

Reflex frontends are built using components which are based on [React](https://react.dev). Pages are defined declaratively as Python functions, and during compilation they are converted to React components.

Each component such as `rx.hstack` and `rx.input` maps to a React component. 
We chose React because it is a popular library with a huge ecosystem - our goal isn't to recreate the web ecosystem, but to make it accessible to Python developers.

Let's take a look at the `index` page from our example app:

```python
def index():
    return rx.hstack(
        rx.avatar(src=f"https://github.com/\{GithubState.username}.png"),
        rx.input(
            placeholder="Enter your username",
            on_blur=GithubState.set_username,
        ),
    )
```

The above Python code is compiled roughly to the following Javascript code:

```jsx
<Hstack>
    <Avatar src=\{`https://github.com/$\{GithubState.username}.png`}/>
    <Input
        placeholder="Enter your username"
        onBlur=\{GithubState.set_username}
    >
</Hstack>
```

You can wrap any React component by subclassing `rx.Component`. For example the `rx.avatar` is based on the [Radix UI](https://www.radix-ui.com/themes/docs/components/avatar) component, and its implementation is just a few lines of Python code:

```python
class Avatar(rx.Component):
    # Specify the library.
    library = "@radix-ui/themes@^2.0.0"

    # Specify the tag.
    tag = "Avatar"

    # Specify the props (only one for simplicity here).
    src: Var[str]

avatar = Avatar.create
```

### Package Management

Depending on which components you use, your app may require different frontend packages. For example, the `rx.avatar` component uses the `@radix-ui/themes` library. 

To avoid installing every library for every app, Reflex automatically detects which components you use and installs only the required libraries for you.
This applies to any components you wrap as well.

When running in `dev` mode, if you add a new component you may see a message like this:

```bash
New packages detected: Updating app...
```




## Reactive UIs With Vars

## Event Processing

Now we get into the heart of Reflex: the event processing system. Reflex uses a reactive programming model to handle events and state updates.

The frontend and backend communicate using websockets. When a user interacts with the frontend, an event is sent to the backend. The backend processes the event and updates the state, and then sends the updated state back to the frontend.


### Event Queue

### State Manager

### Event Handling

### State Updates

## Exporting