---
company: Bayesline
description: "How Bayesline builds 4x faster using Reflex instead of Plotly Dash"
domain: "https://bayesline.com/"
founded: "New York, 2024"
investors: "Y Combinator",
meta: [
  {
    "name": "keywords",
    "content": "
      plotly dash,
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

Why Bayesline chose Reflex instead of Plotly Dash

## TLDR;

Sebastian and his small team use Reflex to build a production-grade web app while still keeping the full flexibility of a traditional ReactJS app **WITHOUT** needing to:

* Learn frontend: React (JavaScript), NodeJS, TailwindCSS

```md quote Misha and Sebastian
Reflex definitely saved us from needing to hire a frontend engineer and sped us up by 4x relative to learning React
```

* Write boilerplate to stitch together their frontend and backend (including database management)

```md quote Sebastian
50% less code than the same Dash app and easier to easier to read / write / maintain code compared to Dash
```

* Maintain expensive, fragile, and inevitably slow Dash apps

```md quote Misha
Using Reflex instead of Plotly Dash was like the difference between organized Legos and a plate of spaghetti
```

## What Baylesline is building

Meet Bayesline, the Y-combinator-backed GPU-powered financial analytics suite for institutional investors.
Bayesline deploys customized equity factor risk (ML) models in the cloud, which previously could take weeks or months for investors to build.
Sebastian Janisch, the Bayesline co-founder, led the technical team and worked previously at Bloomberg and BlackRock, where he was a Director in their Financial Modeling Group.
Here is a blog that further shows what Bayesline does in further detail [https://bayesline.com/blog/building-risk-models](https://bayesline.com/blog/building-risk-models) (The images and demos are all Reflex apps).

## How Bayesline builds faster using Reflex instead of Plotly Dash

Quantitative Analysts (Quants), like Sebastian, are usually proficient in data-oriented programming languages like Python.
Quants want to spend their time building models, proving out their ideas, and not worrying about the UI.

```md quote Sebastian
"The UI is the necessary evil, that is not our bread and butter.”,
```

They used to build prototypes with Dash and eventually hand them to a fully-fledged engineering team.
It would take months before their app ideas could be used across an organization; with Reflex you can both build and share apps in a matter of hours (`reflex deploy`).

```md quote Sebastian
You wouldn’t want to use Dash to build a production-grade application. It’s a prototyping tool. Usually, a UX and engineering team would re-implement everything from scratch. It will take six months for anyone to get hands on it, but we want this now.
```

When embarking on building Bayesline, Sebastian and his co-founder wanted an open-source framework that would enable them to build a fully-fledged web app in pure Python, the language and ecosystem they were already familiar with.

```md quote Sebastian
So we basically need the tool that gets us to the finish line fastest without having to learn (a new framework) and without a super steep learning curve.
```

Sebastian and his team built an initial prototype of Dash, a low-code framework for rapidly building data apps in Python.
As their app grew, it eventually became slow and difficult to maintain.

```md quote Sebastian
The app was just getting painfully slow. Dash loads the entire application, the entire dom of every single page...by definition, almost as the application gets bigger, the performance will just grind, will go down.
```

Bayesline switched from Dash to Reflex because they could build both a production-grade and an aesthetically pleasing web app quickly–without JavaScript experience.

```md quote Sebastian
... we wanted to build a frontend that would be as indistinguishable as possible from one built by professional frontend developers.
```

Complicated Dash apps not only eventually hit performance limits but are also challenging to maintain since there isn’t first-class support for object-oriented programming (OOP) design patterns:

```md quote Sebastian
When we started looking at the (Dash) code, it just got to this point where you’re scared of it because there is no object-oriented notion; the code just turns into an enormous mess because you just have this huge collection of functions.
```

In addition, Reflex improves the developer experience with 60+ UI components out of the box while still offering the flexibility of integrating your own custom React components.
Bayesline wrapped AG Grid--a high-performance React grid--the industry standard data table for fintech.
This powerful combination of out-of-the-box functionality and flexibility made Reflex an attractive choice for Bayesline.

Sebastian and Misha originally started building with Reflex to create a minimum viable product that would get them through YC and their initial funding round.
They quickly learned that Reflex was already ready to build production grade web apps.

```md quote Sebastian
Turns out I don’t see right now, as it stands at least, reasons to migrate from Reflex to somewhere else.
```

Bayesline has since scaled from an MVP that investors leverage daily.
The team continues to build and deploy data-intensive apps using Reflex.
