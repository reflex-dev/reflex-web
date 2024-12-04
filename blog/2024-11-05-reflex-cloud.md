---
author: Nikhil Rao
date: 2024-12-05
title: Reflex Cloud
description: Deploy your app with a single command
image: /blog/fundraise_dark.png
meta: [
    {"name": "keywords", "content": ""},
]
---

```python exec
import reflex as rx
from pcweb import pages
```

## Reflex Cloud

Today we're launching [Reflex Cloud](/hosting), a unified platform for deploying and managing your Reflex apps.

Deploy your first app for free - and scale it as your app grows with our Pro and Enterprise tiers.

## What's Included

### One Command Deployment

Deploy your app with a single command:

```bash 
reflex deploy
```

We will set up your infrastructure and in a few minutes your app will be live to share with the world.

The new `deploy` command lets you set environment variables, specify machine sizes, and choose regions to deploy to all from the command line.

See the full list of options in our [deployment docs](/docs/hosting/deploy-quick-start).

### A Unified Dashboard        

Log in to [Reflex Cloud](https://cloud.reflex.dev) to see a unified dashboard of all your apps.

```python eval
rx.color_mode_cond(
    rx.image(src="/hosting/light/hosting-preview.jpg"),
    rx.image(src="/hosting/dark/hosting-preview.jpg"),
)
```

You can see the status of your apps, the resources they're using, and application logs all in one place.

You can also 

### Pro Features

Reflex Pro lets you take your app from a prototype to a production app with:
* **Custom Domains**: Use your own domain for your app
* **Larger Apps**: Increased memory and CPU options
* **Add Collaborators**: Add team members to your project

We're also introducing team and enterprise plans with
* **One-Click Auth**: Add Github, Google, or other OAuth providers to your app with no code
* **Full Analytics**: Comprehensive insight into your app's performance and usage 
* **On Premise Hosting**: Run Reflex Cloud on your own infrastructure

See the full list of features on our [pricing page](/pricing).

## What's Next




