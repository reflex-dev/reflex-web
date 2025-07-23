---
title: trade_blotter_dashboard
description: "Interactive dashboard for tracking, managing, and reviewing trade activity in real time."
author: "Reflex"
image: "trade_blotter_dashboard.png"
demo: "https://csv-trade-report-tool-gray-piano.rxc.app/"
# source: "https://github.com/reflex-dev/templates/tree/main/api_admin_panel"
meta: [
    {"name": "keywords", "content": "trade blotter, trading dashboard, financial operations, reflex dashboard"},
]
tags: ["Dashboard"]
---

The following is a trade blotter dashboard built to help you track and manage trading activity. It offers real-time visibility into executed trades, pending orders, and key performance metrics, streamlining financial operations for traders and analysts.

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
