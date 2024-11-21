# Reflex Cloud - Quick Start

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages import docs
```

So far, we have been running our apps locally on our own machines.
But what if we want to share our apps with the world? This is where
the hosting service comes in.

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.

### Prerequisites

1. Hosting service requires `reflex>=0.6.5`.
2. This tutorial assumes you have successfully `reflex init` and `reflex run` your app.
3. Also make sure you have a `requirements.txt` file at the top level app directory that contains all your python dependencies! (To create a `requirements.txt` file, run `pip freeze > requirements.txt`.)


### Authentication

First run the command below to login / signup to your Reflex Cloud account: (command ine)

```bash
reflex login
```

You will be redirected to your browser where you can authenticate through Github or Gmail.

### Web UI

Once you are at this URL and you have successfully authenticated, click on the one project you have in your workspace. You should get a screen like this:

```python eval
image_zoom(rx.image(src="/cloud_project_page.png", alt="Reflex Cloud Dashboard"))
```

This screen shows the login command and the deploy command. As we are already logged in, we can skip the login command.

### Deployment

Now you can start deploying your app.

In your cloud UI copy the `reflex deploy` command similar to the one shown below.

```bash
reflex deploy --project 2a432b8f-2605-4753-####-####0cd1####
```

In your project directory (where you would normally run `reflex run`) paste this command.

The command is by default interactive. It asks you a few questions for information required for the deployment.


1. The first question will compare your `requirements.txt` to your python environment and if they are different then it will ask you if you want to update your `requirements.txt` or to continue with the current one. If they are identical this queston will not appear. To create a `requirements.txt` file, run `pip freeze > requirements.txt`.
2. The second question will search for a deployed app with the name of your current app, if it does not find one then it will ask if you wish to proceed in deploying your new app.
3. The third question is optional and will ask you for an app description.


That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

```md alert info
# Once your code is uploaded, the hosting service will start the deployment. After a complete upload, exiting from the command **does not** affect the deployment process. The command prints a message when you can safely close it without affecting the deployment.
```

If you go back to the Cloud UI you should be able to see your deployed app and other useful app information.










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
