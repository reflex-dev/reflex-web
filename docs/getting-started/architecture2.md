```python exec
import reflex as rx
```

# Architecture

This page provides an overview of the Reflex internals. You don't need to understand this to use Reflex, but it can be helpful if you want to contribute to Reflex development, or if you're just interested in how Reflex works under the hood.

## Motivation

Reflex is a framework to build full-stack web apps in pure Python.

We wanted to build a way so anyone who knows Python can easily build apps and share them with the world, without needing to learn a new language and piece together a bunch of different tools.
Reflex handles the frontend, backend, and deployment of your app, so you can focus more on your ideas and less on the technical details.

There are other Python libraries to make web apps, but they often have a low ceiling and high graduation risk.
As your app grows in features and complexity, you may find yourself hitting the limits of the framework.
At that point you either have to limit your idea to fit the framework, or scrap your project and rebuild it using a "real web framework" like React.

Reflex aims to be simple to get started building a basic app, but also have the power and flexibility to grow with your app.

## High Level Overview

The diagram below shows a detailed overview of how a Reflex app works.
We'll go through each part in more detail in the following sections.

![Reflex Architecture](/architecture.png)

```python eval
rx.box(height="1em")
```

Reflex apps compile down to a [Next.js](https://github.com/vercel/next.js) frontend app and a [FastAPI](https://github.com/tiangolo/fastapi) backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses websockets to send events from the frontend to the backend, and to send state updates from the backend to the frontend.

## Frontend

Reflex frontends compile down to 

### Node.js

Next.js apps require a Node.js environment to run. 

Reflex manages this for you, so you don't need to worry about installing Node.js or managing the Node.js environment. When you run `reflex init` for the first time, 


### Components

Reflex components are based on [React](https://github.com/facebook/react).

We ch

## State and Vars

## Event Processing

### Event Queue

### State Manager

### Event Handling
