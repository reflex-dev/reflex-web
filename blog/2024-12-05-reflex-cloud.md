---
author: Nikhil Rao
date: 2024-12-05
title: Reflex Cloud
description: Deploy your Reflex apps with a single command
image: /blog/reflex-cloud.webp
meta: [
    {"name": "keywords", "content": ""},
]
---

```python exec
import reflex as rx
from pcweb import pages, constants
from pcweb.pages.hosting_countdown.animated_box import animated_box
```

## Reflex Cloud

Today we're launching [Reflex Cloud](/hosting), a unified platform for deploying and managing Reflex apps.

We released our [open-source framework]({constants.GITHUB_URL}) with a goal to simplify web development - anyone who knows Python should be able to turn their ideas into web apps. Today thousands of teams use Reflex for their data/AI apps, internal tools, and customer-facing web apps.

With Reflex Cloud we're extending that same simplicity to hosting. Just `reflex deploy`, and in a few minutes your app will be live to share with the world.

```python eval
animated_box(relative=True)
```

Our free tier lets you deploy your first app at no cost. We're also introducing the **Enterprise** tier with additional features like one-click auth, custom domains, and on-premise hosting.

## What's Included

### One Command Deployment

Deploy your app with a single command:

```bash 
reflex deploy
```

The new `deploy` command lets you set environment variables, specify machine sizes, and choose regions to deploy to all from the command line.

See the full list of options in our [deployment docs]({pages.docs.hosting.deploy_quick_start.path}).

### Unified Dashboard        

Log in to [Reflex Cloud]({constants.REFLEX_CLOUD_URL}) to see a unified dashboard of all your apps.

```python eval
rx.color_mode_cond(
    rx.image(src="/hosting/light/hosting-preview.jpg"),
    rx.image(src="/hosting/dark/hosting-preview.jpg"),
)
```

From there you can see the status of your apps, the resources they're using, and application logs all in one place.

You can also add team members to collaborate on apps, set up custom domains, and view detailed analytics on your app's performance.

### Enterprise Features

Reflex Enterprise lets you take your app from a prototype to a production app with:
* **Custom Domains**: Use your own domain for your app
* **Larger Apps**: Increased memory and CPU options
* **Add Collaborators**: Add team members to your project
* **One-Click Auth**: Add Github, Google, or other OAuth providers to your app with no code
* **Full Analytics**: Comprehensive insight into your app's performance and usage 
* **On Premise Hosting**: Run Reflex Cloud on your own infrastructure

See the full list of features on our [pricing page](/pricing).

## What's Next

Over the next few months we're working on building out the team features while making the platform more robust and reliable. We're also expanding Reflex Enterprise to go beyond hosting - including AI tools to help you build apps at the speed of thought.