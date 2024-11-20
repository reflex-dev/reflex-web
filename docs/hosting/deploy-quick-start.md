# Reflex Hosting Service

```python exec
import reflex as rx
from pcweb import constants
from pcweb.pages import docs
from pcweb.templates.docpage import doccmdoutput
```

So far, we have been running our apps locally on our own machines.
But what if we want to share our apps with the world? This is where
the hosting service comes in.

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.

### Prerequisites

1. Hosting service requires `reflex>=0.6.5`.
2. This tutorial assumes you have successfully `reflex init` and `reflex run` your app.
3. Also make sure you have a `requirements.txt` file at the top level app directory that contains all your python dependencies!

### Authentication

First, create an account or log into it using the following command.

```bash
reflex login
```

You will be redirected to your browser where you can authenticate through Github or Gmail.

### Deployment

Once you have successfully authenticated, you can start deploying your apps.

Navigate to the project directory that you want to deploy and type the following command:

```bash
reflex deploy
```

The command is by default interactive. It asks you a few questions for information required for the deployment.

**Name**: choose a name for the deployed app. This name will be part of the deployed app URL, i.e. `<app-name>-randomword-randomword.reflex.run`. 

The name should only contain domain name safe characters: no slashes, no underscores.

```md alert info
# Custom domains are available for paid plans.
```

**Regions**: enter the region code here or press `Enter` to accept the default. The default code `sjc` stands for San Jose, California in the US west coast. Check the list of supported regions at [reflex deployments regions](#reflex-deployments-regions).

**Envs**: `Envs` are environment variables. You might not have used them at all in your app. In that case, press `Enter` to skip. More on the environment variables in the later section [Environment Variables](#environment-variables).

That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

```md alert info
# The hosting service does not currently handle database or file upload operations. Set up an external database use it within your app.
```

## See it in Action

Below is a video of deploying the [AI chat app]({docs.getting_started.chatapp_tutorial.path}) to our hosting service.

```python eval
rx.box(
    rx.el.iframe(
        src="https://www.loom.com/embed/bee928924a454a8098e741e1d19b2857?sid=38523a3f-4c7d-4ee2-9a51-4ca1a36828dc",
        frameborder="0",
        webkitallowfullscreen=True,
        mozallowfullscreen=True,
        allowfullscreen=True,
        position="absolute",
        top="0",
        left="0",
        width="100%",
        height="100%",
    ),
    position="relative",
    padding_bottom="64.94708994708994%",
    height="0",
)
```
