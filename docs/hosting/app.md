```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```


# App

In Reflex Cloud an "app" (or "application" or "website") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. 

You can deploy an app using the `reflex deploy --project dc763ea6-####-####-####-############` command, where the id passed with the `--project` flag is your project id.

There are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.


## View Logs

To view the app logs follow the arrow in the image below and press on the `Logs` dropdown.

```python eval
image_zoom(rx.image(src="/view_logs.webp"))
```


## View Deployment Logs and Deployment History

To view the deployment history follow the arrow in the image below and press on the `Deployments`.

```python eval
image_zoom(rx.image(src="/view_deployment_logs.webp"))
```

This brings you to the page below where you can see the deployment history of your app. Click on deployment you wish to explore further.

```python eval
image_zoom(rx.image(src="/view_deployment_logs_2.webp"))
```

This brings you to the page below where you can view the deployment logs of your app by clicking the `Build logs` dropdown.

```python eval
image_zoom(rx.image(src="/view_deployment_logs_3.webp"))
```


