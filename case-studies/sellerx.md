---
company: SellerX
description: "Why SellerX chose Reflex over Streamlit for their data processing pipeline"
domain: "https://sellerx.com"
founded: "Berlin, 2020"
investors: "L Catterton, Sofina, BlackRock and more"
stats: [
    {
        "metric": "Faster than developing with React and FastAPI",
        "value": "10x"
    },
    {
        "metric": "Increase in speed of data analysis, allowing a whole month of work to be done in less than a week",
        "value": "5x"
    },
    {
        "metric": "Worth of data, over 500,000 data points, is ingested by the app daily",
        "value": "100 GB"
    },
]
meta: [
  {
    "name": "keywords",
    "content": "
      python react,
      python web app,
      python web app framework,
      streamlit,
      streamlit python,
      streamlit vs reflex,
      react python,
      react with python,
      web app python,
    "
  }
]
---

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import library
```

```python eval
rx.vstack(
    image_zoom(rx.image(src="/case_studies/sellerx_app.webp", border_radius="10px", alt="SellerX App")),
    rx.text("SellerX App built with Reflex"),
    width="100%",
)
```

```python eval
rx.box(height="30px")
```



Meet SellerX, a Berlin-based, high-growth eCommerce player that aims to consolidate Amazon’s most successful sellers, acquiring them to scale their business and turn their brands into global household names.

SellerX has become one of the largest eCommerce aggregators in the European market. Today it manages more than 50 ecommerce brands.


## SellerX's overwhelming data processing pipeline

SellerX has teams that collect a lot of data from Amazon and different marketplaces to derive insights on their brands and products. SellerX handles around half a million data points daily. It handles hundreds of thousands of products in different marketplaces in 4 different continents and ingests daily DBs the size of 100 GB worth of information.

Some of the processes require information about products, reviews, and prices so they can understand trends and make decisions on companies to look at investing in. This process could be very labour intensive, they would have to go to Amazon and to the companies specific websites, explore different DBs, copy this information and put it all manually in excel.

[Mike Woodcock](https://www.linkedin.com/in/mike-woodcock/), the Head of AI & Automation at SellerX, was placed in charge of working with various teams, among his other duties, to streamline the process of data sourcing. He needed to build a custom interface for the teams to help them collect their data more efficiently.

His main requirements were that the final product needed to be a web interface, it needed SSO (single sign-on) capabilities, and the team needed to be able to iterate quickly with feedback.

His plan was to create a web app to extract the needed information to create insights, therefore streamlining the process and cutting down on hundreds of hours of manual work a month. The data collection task would run in the background and then the end user would open up the app and all the information that they need to make their buying decisions on the companies would be ready for them.



## SellerX's struggles with Streamlit

Mike and his team initially started with [Streamlit](https://streamlit.io), a python framework to build simple web apps, but it was very limited for this use case. Their first concern was with the limitations of the Streamlit framework.


```md quote
- name: Mike
- role: Head of AI
Streamlit's linear execution model, which re-runs the entire script upon each user interaction, can lead to inefficiencies and potential memory leaks, posing challenges for long-term projects.
```

Furthermore, Mike and his team found it hard as Streamlit is not built to be event driven.

```md quote
- name: Mike
- role: Head of AI
Streamlit is not an event based tool, for example you cannot subscribe to a specific on edit event.
```

Lastly, there were issues with the layout and lack of customizability.


```md quote
- name: Mike
- role: Head of AI
Streamlit had very basic layout and you don’t have any other options.
```

Overall they found that when they used Streamlit they always needed to go and build the real app again afterwards. Their alternative approach up until now was to build using React with a FastAPI backend.



## How Reflex empowered SellerX

The app Mike and his team were building handles around half a million data points daily. It handles hundreds of thousands of products in different marketplaces in 4 different continents and ingests daily a DB the size of 100 GB worth of information.

The app has several tables of data with images, links and lots of text data. It included web scrapers as well as many api calls.

Below are some of the key Reflex features their app took advantage of:

- Reflex's background events for long running scraping tasks to extract all the data that they needed.

- [AG Grid]({library.tables_and_data_grids.ag_grid.path}), which is built into Reflex, to display the data in a table. AG Grid is a high performance data grid that is used in many fortune 500 companies web applications.

- SSO was a requirement for the app, and Mike used Azure Auth, one of the many options provided by Reflex for authentication.



Finally the code was far more organized and maintainable than their previous Streamlit app, and they were able to write more event driven code.

```md quote
- name: Mike
- role: Head of AI
With Reflex the code is much more organized and every time the user does something it's more dynamic, more event based.
```


## Why SellerX chose Reflex

The app that Mike and his team built with Reflex has been a huge success. It is allowing a team within SellerX to review 5 times more data than before, essentially allowing them to do a whole month of work in less than a week.


```md quote
- name: Mike
- role: Head of AI
A team of 6 non-technical employees use the app to make decisions based on Amazon information. It is allowing this team to be significantly more efficient and structured in the way they work and they are very happy with the improvements in speed. This team is now able to review 5x more Amazon data than their previous approach.
```

Reflex also allowed the team to iterate much faster than using React but with the confidence that they will not need to rebuild their entire app as they would with Streamlit.


```md quote
- name: Mike
- role: Head of AI
We are moving significantly faster, which has been very very useful. To have a quick call with the end user of the app and then the next day you have a nice basic interface for them to use, to double check if they like the setup, and see if it's going to work, it's just fantastic.
```

```md quote
- name: Mike
- role: Head of AI
With Reflex it is ten times faster than developing with React and FastApi.
```

Finally deployments have been much more straightforward with Reflex.


```md quote
- name: Mike
- role: Head of AI
Also for deploying everything is significantly easier. It's all just Python. You just open the right ports, add SSO, and then everyone that needs to have access can use the app.
```
