---
company: SellerX
description: "Why ...."
domain: "https://sellerx.com"
founded: "....."
investors: "......"
stats: [
    {
        "metric": ".......",
        "value": "10x"
    },
    {
        "metric": ".....",
        "value": "5x"
    },
]
meta: [
  {
    "name": "keywords",
    "content": "
      python react,
      python web app,
      python web app framework,
      python web apps,
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

!!!! Add image of app here !!!!


Meet SellerX, a Berlin-based, high-growth eCommerce player that aims to consolidate Amazon’s most successful sellers, acquiring them to scale their business and turn their brands into global household names. 

SellerX has become one of the largest eCommerce aggregators in the European market. Today it manages more than 50 ecommerce brands. 


## SellerX's overwhelming data processing pipeline

SellerX has teams that collect a lot of data from Amazon to derive insights on which brands to acquire. This was a very manual process of employees looking up information about products, reviews, and prices so they can understand trends and make decisions on companies to look at investing in. They would have to go to Amazon and go to the companies specific websites, copy this information, put it all manually in excel.

Mike Woodcock, the Head of AI & Automation at SellerX, was placed in charge of working with these teams and finding a way to streamline this process of data sourcing. He needed to build a custom interface for the teams to help them collect their data for efficiently. 

His main requirements were that the final product needed to be a web interface, it needed SSO (single sign-on) capabilities, and they needed to be able to iterate quickly.

His plan was to create an app to extract the information and create insights, therefore streamlining the process. The task would run for a day and then the user would open up the app and the information that they need to make decisions on the companies would be there.



## SellerX's struggles with Streamlit

Mike and his team initially started with [Streamlit]("https://streamlit.io"), a python framework to build simple web apps. 