---
company: Ansa
description: "Why Ansa chose Reflex over Anvil for their data analysis workflow automations"
domain: "https://www.ansa.co"
founded: "New York, 2021"
stats: [
    {
        "metric": "Companies scored every month",
        "value": "16,000"
    },
    {
        "metric": "Core company workflows optimized",
        "value": "6"
    },
    {
        "metric": "Hours of manual work saved a month",
        "value": "650+"
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


Meet Ansa a venture capital firm based in New York City that invests in companies from Series A to C. They have invested in companies such as Coinbase, Rippling, Glassdoor and Godaddy.

Ryan (Sullivan) is an investor and manages the tech and data science team at Ansa. He works to help find the right companies to invest in and improve Ansa's automated outbound strategies.


## Ansa's overwhelming data analysis challenge

As a VC, Ansa must filter through thousands of companies a month to find the best possible investment deals. Their sourcing is very outbound driven and previously they could never review all the companies they wanted to, meaning they were missing potentially great deals.

Ryan and his team's goal was to automate as much as they could on the workflow side. This included finding interesting companies and reaching out to them to help their smaller investment team be more efficient and effective. They also began using Data Science and Machine Learning to help improve the sourcing of companies and to increase automated outbound. 

```md quote
- name: Ryan
- role: Investor and Head of Data Science
We're frankly a smaller team and there's a lot of opportunities out there, so we're trying to automate as much as we can on the workflow side to help our smaller team be efficient and cover as many companies as possible, researching them and scaling out our outbound.
```

They wanted inbuilt tools to give them an edge as a small team, such as a in-house scoring model to help flag important companies. They wanted a WebUI that the team can view and interact with like a scored database.

We're frankly a smaller team and there's a lot of opportunities out there, so we're trying to automate as much as we can on the workflow side to help our smaller team be efficient and cover as many companies as possible, researching them and scaling out our outbound.


## How Ansa hit the limits of the Anvil framework

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

One of the main challenges that Ansa face is how to figure out what companies to spend their time investigating further to potentially invest, and then to reach out to them.


### Creating natural language company search 

The first automated workflow, using a combination of OpenAI and Langchain, introduces natural language to SQL searches for a database. This allows employees to more easily search for companies based on semantic similarities. 


### In-house company ranking algorithm 

Once they find a long list of companies they built another automated workflow to rank these companies. They run workflow every week. It takes a list of companies, sends them to their API, and there each company is scored by running their custom AI model in Databricks. These scores are returned back and emailed to the user as a CSV. This AI model they built is used to spot factors in companies they believe will be successful for the fund. 


### Increase understanding of what a company does using vector embeddings

Once they have a list of interesting companies to explore further they created an automated workflow to quickly get a deeper understanding of what the companies do. This workflow scrapes company data from the internet and creates vector embeddings using an LLM to allow their employees to do a vector search through the companies to quickly understand what that company does. 


```md quote
- name: Ryan
- role: Investor and Head of Data Science
We use LLMs to help navigate through the site and find different details. For example the customer page for one website, maybe different for another. The LLM then summarizes all that data and creates embeddings on that and then we use that for the searches. The LLMs help us normalize across, even if pages are named differently so we can easily search through all of them and figure out what the company does.
```



### Improving email outbound 

Finally, when their team has a short list of companies they like, they built a fourth workflow to automate the extraction of the relevant information to reach out to these companies. Ryan runs us through this final workflow in his quote below.


```md quote
- name: Ryan
- role: Investor and Head of Data Science
Let’s say we have 20 companies that we want to email to. How do you actually reach out and email those companies? We launch a script that runs through a Reflex background event that'll go through each company, check the CRM ownership, it'll tag it, fill out relevant fields and find the best person to reach out to. A lot of times, especially with early stage companies, it's not always clear who the founder or CEO is or what their email is. So this workflow will find their email, test all that, and then it will go to our email engagement and tracking tool and add it there and make sure everything is relevant. Before we would do this all manually. Now with this new workflow built in Reflex it is as easy as click and it’s done.
```



All these different workflows, are now built into a single Reflex app that makes it extremely easy for anyone on the team to run any of them and move data from one to another with a few clicks.

Throughout building this Reflex app, Ansa used:

- Supabase database to store all their data

- Google Auth login component for Ansa employees to log in

- Download Functionality 

- Table Component


Overall Ansa found that with Reflex, as everything is in pure python, they were able to integrate everything they wanted and knew they always could, which was their major concern with Anvil.


```md quote
- name: Ryan
- role: Investor and Head of Data Science
Reflex was a better fit than Anvil. Given that it's just python code, I'm always comfortable that we'll be able use different tools and to figure out how to make it work with Reflex versus being stuck with the integrations that Anvil have.
```


## What Ansa gained from using Reflex


The app that Ryan and his team created, which contains 6 different automated workflows, is now a central dependency to source potential companies and to analyze them.

```md quote
- name: Ryan
- role: Investor and Head of Data Science
75% of our team uses the app on a weekly basis.
```

They process and score 16,000 companies on a monthly basis using their in-house company ranking workflow and show all that data in the app.

They then take around 4000 of the highest scoring companies a month and run them through the vector embedding workflow to research the company.

```md quote
- name: Ryan
- role: Investor and Head of Data Science
Our benchmark is researching the company and adding it into the outreach cadence saves 10 minutes per company versus doing it manually.
```

Overall this is saving over 650 hours a month for his team.

Finally, the combination of the automated workflows is not only saving the team time, it is also bringing better deals to the table that may have otherwise been overlooked.

```md quote
- name: Ryan
- role: Investor and Head of Data Science
Then there's also opportunities that get flagged and displayed that we probably otherwise would have have missed.
```

