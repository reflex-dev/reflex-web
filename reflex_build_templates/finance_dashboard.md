---
title: finance_dashboard
description: "Interactive dashboard for visualizing and managing financial data and performance."
author: "Reflex"
image: "finance_dashboard.png"
demo: "https://finance-dashboard-neon-apple.reflex.run/"
# source: "https://github.com/reflex-dev/templates/tree/main/api_admin_panel"
meta: [
    {"name": "keywords", "content": "finance dashboard, financial data, reflex dashboard"},
]
tags: ["Dashboard"]
---

The following is a finance dashboard designed for analyzing and managing key financial metrics. It provides a clear view of performance indicators, cash flow trends, and other essential financial insights in a single interface.

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
