---
company: Ansa
description: "Why ..."
domain: "https://www.ansa.co"
founded: "New York, 2021"
investors: "....."
stats: [
    {
        "metric": "......",
        "value": "50%"
    },
    {
        "metric": "......",
        "value": "4x"
    },
    {
        "metric": ".......",
        "value": "$0"
    }
]
meta: [
  {
    "name": "keywords",
    "content": "
      python and react,
      python and react js,
      python react,
      python web app,
      python web app framework,
      python web apps,
      react js python,
      react js with python,
      react python,
      react python websocket,
      react with python,
      web app framework python,
      web app python,
    "
  }
]
---


Meet Ansa a venture capital firm based that invests in (types of companies) from Series A to C. They have invested in companies such as Coinbase, Rippling, Glassdoor and Godaddy.


Ryan (Sullivan) is an investor and manages the tech and data science team at Ansa, to help find the right companies to invest in and improve their automated outbound strategies.


## Ansa's (Information Overload),..\


As a VC, Ansa must filter through thousands of companies a month to find the best possible investment deals. Their sourcing is very outbound driven and previously they could never review all the companies they wanted to, meaning they were missing potentially great deals.

Ryan and his team's goal was to automate as much as they could on the workflow side. This included finding interesting companies and reaching out to them to help their smaller investment team be more efficient and effective. They also began using Data Science and Machine Learning to help improve the sourcing of companies and to increase automated outbound. 

```md quote
- name: Ryan
- role: Investor and Head of Data Science
We're frankly a smaller team and there's a lot of opportunities out there, so we're trying to automate as much as we can on the workflow side to help our smaller team be efficient and cover as many companies as possible, researching them and scaling out our outbound.
```

They wanted inbuilt tools to give them an edge as a small team, such as a in-house scoring model to help flag important companies. They wanted a WebUI that the team can view and interact with like a scored database.

We're frankly a smaller team and there's a lot of opportunities out there, so we're trying to automate as much as we can on the workflow side to help our smaller team be efficient and cover as many companies as possible, researching them and scaling out our outbound.


## How Ansa hit the limits of the Anvil Framework

Ryan and his team wanted to build a web interface for their team to use to automate their currently very manual workflows. They wanted a pure python solution, as this was the language most people in the team were most familiar with. 

```md quote
- name: Ryan
- role: Investor and Head of Data Science
We don't have a full engineering team, so to build a full web app from scratch seemed like a lot for me to do. In addition, we don't have experience on the JavaScript side.
```

The team previously built an [Anvil](link to anvil!!!!!!!!!!) app, a near no code python framework. They didn't like the aesthetic and wanted to use more modern looking React components.

```md quote
- name: Ryan
- role: Investor and Head of Data Science
It’s an older framework and the components didn't really look that good. We wanted to use react components and just make it look a little bit more modern.
```

Their main concern with Anvil though was that they didn't want to outgrow a near no code framework, and wanted to build their app for the long term.


```md quote
- name: Ryan
- role: Investor and Head of Data Science
We don't want to run into a situation where this year or next year, we want to add more functionality that Anvil doesn't have and we're not able to integrate it. We know we're building this for the long term and we want to have flexibility and not outgrow it.
```

In addition, there were particular technologies like LLMs and Vector Databases that Ryan and the team knew at some point they would want to integrate into the app, but that this would be extremely difficult if not impossible with low/no code frameworks like Anvil.


```md quote
- name: Ryan
- role: Investor and Head of Data Science
I started to feel that with Anvil I didn’t know if we can do everything. If they don't have a component for it, I wouldn’t know how to integrate it. For example some of the newer stuff we do with vector databases and embeddings or LLMs would be harder to do in Anvil as we would be stuck to the integration that Anvil have.
```


## From manual work to automation with Reflex

Ansa switched from Anvil to Reflex because they could build both a web app for the long term that they would not outgrow and they required no JavaScript experience.

They currently have an app with 6 different core company workflow automations, several of which we will discuss in this case study. 