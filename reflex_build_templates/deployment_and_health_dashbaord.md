---
title: deployment_and_health_dashbaord
description: "Interactive dashboard for managing deployments and monitoring system health."
author: "Reflex"
image: "deployment_and_health_dashbaord.png"
demo: "https://retail-analytics-dashboard-cyan-ring.rxc.app/"
# source: "https://github.com/reflex-dev/templates/tree/main/api_admin_panel"
meta: [
    {"name": "keywords", "content": "deployment dashboard, system health, reflex dashboard"},
]
tags: ["Dashboard"]
---

The following is a deployment and health dashboard designed to track deployment activities and monitor system performance. It helps developers and operators oversee application status, request history, and service health in real time.

## Setup

To run this app locally, install Reflex and run:

```bash
reflex init --template api_admin_panel
```

To run the app, use:

```bash
reflex run
```

## Usage

To use the app insert the desired endpoint click `New Request` then in the input field and click on the `Send` button. You can optionally add a body, headers, and cookies to the request. The response will be displayed in the table.

When clicking on a row the request and response will be displayed in the respective sections. You can further customize this app by adding custom actions to the rows and `Commit` and `Close` buttons.
