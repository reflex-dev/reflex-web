---
title: treasury_dashboard
description: "Interactive dashboard for managing treasury operations, liquidity, and cash positions."
author: "Reflex"
image: "treasury_dashboard.png"
demo: "https://treasury-and-liquidity-monitor-gold-sun.rxc.app/"
# source: "https://github.com/reflex-dev/templates/tree/main/api_admin_panel"
meta: [
    {"name": "keywords", "content": "treasury dashboard, liquidity management, cash position, reflex dashboard"},
]
tags: ["Dashboard"]
---

The following is a treasury dashboard designed to help teams manage liquidity, monitor cash positions, and streamline treasury workflows. It provides visibility into financial health, cash flow activity, and operational risk from a centralized interface.

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
