---
title: company_dashboard
description: "Comprehensive dashboard for audio analysis, monitoring, and operational insights."
author: "Reflex"
image: "company_dashboard.png"
demo: "https://company-dashboard-navy-book.reflex.run/"
# source: "https://github.com/reflex-dev/templates/tree/main/api_admin_panel"
meta: [
    {"name": "keywords", "content": "audio dashboard, sound analysis, reflex audio tools"},
]
tags: ["Dashboard"]
---

The following is an audio operations dashboard that allows you to analyze, monitor, and manage various audio-related workflows. It provides real-time insights and tools for interacting with sound or voice data in a structured and intuitive interface.

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
