---
title: trade_blotter_dashboard
description: "Automatically pulls executions from every venue, flags outliers, and emails a compliance-ready PDF to traders each night."
author: "Reflex"
image: "trade_blotter_dashboard.webp"
video: "https://www.youtube.com/embed/gc_he7I1vGc"
demo: "https://csv-trade-report-tool-gray-piano.rxc.app/"
meta: [
    {"name": "keywords", "content": "trade blotter, trading dashboard, financial operations, execution management, outlier detection, compliance reporting, nightly pdf, trading analytics"},
]
tags: ["Trading", "Finance", "Compliance", "Analytics"]
integrations: ["Resend", "Database"]
---

# End-of-Day Trade Blotter

Trading desks juggle dozens of execution venues and ever-tightening regulations.
This app consolidates every fill, surfaces unusual activity, and mails a polished, audit-ready report to your inbox before you leave for the day.

---

**Industry**
Capital Markets · Asset Management · Hedge Funds

**End users**
Traders · Compliance Officers · Risk Analysts · Middle-Office Operations

**Components**
Data Grid · KPI Cards · Line & Bar Charts · PDF Generator · Email Scheduler · Threshold Slider · Buttons & Toasts

---

### What you can build

* **Unified Executions Stream** – connect FIX sessions, REST APIs, or CSV drops to view all fills in one sortable grid.
* **Outlier Radar** – auto-detect price or size deviations beyond configurable σ-levels; color-code and comment inline.
* **Blotter PDF** – nightly PDF with firm branding, summary stats, full trade table, and highlighted anomalies—ready for regulators.
* **On-Demand Sync** – “Sync Now” button re-pulls today’s trades and refreshes flags in seconds.
* **Threshold Tuning Panel** – adjust detection sensitivity and instantly preview which trades will be flagged.
* **Venue Credential Vault** – manage API keys, FIX logins, and test connectivity without leaving the UI.
* **Flagged Trades CSV Export** – share anomaly lists with desk heads or auditors via one-click download.

Everything runs in pure Python with Reflex—swap the mock data ingestors for your OMS or FIX engine, connect SMTP for real emails, and you’ve got a production-grade compliance blotter in minutes.
