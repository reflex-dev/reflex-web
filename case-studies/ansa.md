---
company: Ansa
description: "Why Ansa chose Reflex over a no-code/low-code framework for their workflow automations"
domain: "https://www.ansa.co"
founded: "New York, 2021"
investors: ""
stats: [
    {
        "metric": "Companies scored every month",
        "value": "16,000"
    },
    {
        "metric": "Core company workflows optimized",
        "value": "8"
    },
    {
        "metric": "Hours of manual work saved a month",
        "value": "100+"
    }
]
meta: [
  {
    "name": "keywords",
    "content": "
      python web app,
      anvil,
      python anvil,
      anvil python,
      low code python web app,
      no code python web app,
      venture capital python,
      python web app framework,
      python web apps,
      web app framework python,
      web app python,
    "
  }
]
---

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.vstack(
    image_zoom(rx.image(src="/case_studies/ansa_app.webp", border_radius="10px", alt="Ansa App")),
    rx.text("Ansa App built with Reflex"),
    width="100%",
)
```

Meet [Ansa](www.ansa.co), a venture capital firm based in New York City that invests in companies from Series A to C. They have invested in companies like Defense Unicorns, Bland, Gradient, and Selector and prior to founding the firm, supported investments in many of the venture-capital industry’s largest outcomes including Crowdstrike, Coinbase, and SurveyMonkey to name a few.

Ryan Sullivan is an investor and oversees the engineering and data science team at Ansa. He finds and supports new investments and is the architect behind Ansa's data-driven sourcing strategy, working closely with the firms’ Managing Partner Marco Demeireles to build the firms’ proprietary sourcing applications and research products.


## Ansa's data analysis challenge

Ansa has an investable universe of 10s of thousands of companies and they need to make sure they are spending time with the right companies at the right time. Their sourcing is thesis driven, so they need to both quickly find all companies in a theme of interest and track opportunities across the broader market. With a lean investment team, they need to leverage software and data to review and track all these opportunities.

Ryan and his team's goal was to automate and augment as much as they could on this company sourcing and review workflow. This included helping their lean investment team be more efficient and effective in finding interesting companies and reaching out to them. They also began using Data Science and Machine Learning to help surface more relevant companies leverage proprietary and third party data sources.

```md quote
- name: Ryan
- role: Investor and Head of Data
We have a lean investment team and there's a lot of opportunities out there, so we're trying to automate as much as we can on the workflow side to help our team be efficient and research, review, and reach out to as many companies as possible.
```

They wanted custom tools to give them an edge, such as an in-house scoring model to help flag important companies.


## How Ansa hit the limits of a low-code python framework

Ryan and his team wanted to build a web interface so the broader team could run these automations to automate their manual workflows. They wanted a pure python solution as this was the language the team was most familiar with.

```md quote
- name: Ryan
- role: Investor and Head of Data
We don't have a full engineering team, so to build a full web app from scratch seemed like a lot to manage. In addition, our team is mostly data engineers / analysts so we are far more comfortable with Python than JavaScript.
```

The team previously built on an all-python, low-code / no code framework. They didn't like the aesthetic and wanted to use more modern looking React components.

```md quote
- name: Ryan
- role: Investor and Head of Data
It’s an older framework and the components didn't look that good. We wanted to use react components and just make it look a little bit more modern.
```

Their main concern though was that they didn't want to outgrow a near no code framework, as they wanted to build their app for the long term.


```md quote
- name: Ryan
- role: Investor and Head of Data
We don't want to run into a situation where this year or next year, we want to add more functionality that this low code framework doesn't have and we're not able to integrate it. Additionally, the rate of improvement and development velocity from the Reflex team gave us confidence that their offering would continue to improve over time. We're building this for the long term and we want to make sure we both have the flexibility to not outgrow it and are working with the best out there.
```

In addition, there were particular technologies like LLMs and Vector Databases that Ryan and the team knew at some point they would want to integrate into the app. It would be extremely difficult if not impossible to keep up with these latest innovations with low/no code frameworks.


```md quote
- name: Ryan
- role: Investor and Head of Data
I started to feel that with this framework I didn’t know if they could keep up with the pace of new developments with LLMs. They abstract a lot of the backend, so it's difficult to install third party libraries and you don't have full control over the database. For example some of the newer stuff we do with vector databases, embeddings models, or LLMs would be harder to do with this framework as we'd have to move off their native database.
```


## From manual work to automation with Reflex

Ansa switched to Reflex so they could build an app for the long term and accommodate all the latest innovations in LLM development without needing any JavaScript.

They currently have an app with 8 different core company workflow automations, several of which we will discuss in this case study.

The main challenges that Ansa faces are one, figuring out what companies, out of the 10s of thousands within their investment mandate, they should be investigating further, and two, automating all the manual data collection and work required to reach out.


### Creating natural language company search

The first automated workflow they built, using a combination of OpenAI, Langchain, and Chroma, introduced vector and natural language searches over their database. This allows employees to combine quantitative and strict filtering with an understanding of the companies product offering through vector similarity. For example, an employee can type "Carbon accounting software companies with a CEO in NYC that score over 60" and receive a curated list of companies that fit that description.

```md quote
- name: Ryan
- role: Investor and Head of Data
We use LLMs to help navigate through the companies site and find different details. For example the customer page for one website, may be different from another. The LLM then summarizes all that data and creates embeddings on them and then we use that for the searches. The LLMs help us normalize across different companies, even if pages are named differently, so we can easily search through all of them and figure out what the company does.
```

### In-house company scoring algorithm

The next automated workflow takes this list of companies and scores them. With private companies, there is far less data available to assess fit than with public companies, so they rely on alternative data to power a scoring algorithm that assesses the probability a given company is a fit for their investment workflow. They proactively score ~15K companies and display them in Reflex, and also built another automated workflow to score ad-hoc lists of companies. This workflow can take in a list in any format and send the identifiers to their API where they are scored by their custom ML model hosted in Databricks.

The scored data is then displayed to the user in Reflex and emailed to the user as a CSV. This ML model is trained on a labeled dataset they have curated over years, and spots combinations of factors that they believe will lead to successful investments for the fund.


### Improving email outbound

Finally, when their team has a short list of companies that fit within an investment, they built a third workflow to automate the extraction of the relevant information to reach out to these companies. Ryan runs us through this final workflow in his quote below.


```md quote
- name: Ryan
- role: Investor and Head of Data
Let’s say we have 30 companies that we want to email. How can you efficiently send a custom note to each of these companies and track it properly? We launch a script, that runs through a Reflex background event, that'll go through each company, check the CRM ownership, fill out relevant fields and find the best person to reach out to. A lot of times, especially with early stage companies, data is missing or partially complete. So this workflow will leverage LLMs throughout the process to handle fuzzy matching and make contextual decisions, as well as proactively summarize company content, news, and relevant Ansa content to help support the email writing. Before we would do this all manually, now with this new workflow in Reflex, we've taken what was once 30+ clicks across 5 different apps and made it 5x faster with 2 clicks across 2 apps.
```

All these different workflows are now built into a single Reflex app. It makes it extremely easy for anyone on the team to run any of these workflows and leverage LLM-powered automation with a few clicks.

Throughout building this Reflex app, Ryan used:

- Supabase database to store all their data

- LLM tools like OpenAI, Tavily, Browserbase, Langchain, and Chroma

- Google Auth login component for Ansa employees to log in

- AG Grid Table Component

- Download Functionality


Overall Ansa found that with Reflex, as everything is in pure python, they were able to integrate everything they wanted and knew they always could incorporate new tech, which was a concern with their previous framework.


```md quote
- name: Ryan
- role: Investor and Head of Data
Reflex was a better fit overall. Given that it's just python code, I'm always comfortable that we'll be able use different tools and to figure out how to make it work with Reflex versus being stuck with the integrations that our old solution had.
```


## What Ansa gained from using Reflex

The app that Ryan and his team created, which contains 8 different automated workflows, is now a central dependency for Ansa to source potential companies and analyze them.

```md quote
- name: Ryan
- role: Investor and Head of Data
75% of our team uses the app on a weekly basis and we estimate we're saving over ~100 team hours per month.
```
