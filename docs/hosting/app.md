```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import hosting 
```


# App

In Reflex Cloud an "app" (or "application" or "website") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. 

You can deploy an app using the `reflex deploy` command.

There are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.


## View Logs

To view the app logs follow the arrow in the image below and press on the `Logs` dropdown.

```python eval
image_zoom(rx.image(src="/view_logs.webp", padding_bottom="20px"))
```

```md alert info
# CLI Command to view logs
`reflex cloud apps logs [OPTIONS] [APP_ID]`
```

## View Deployment Logs and Deployment History

To view the deployment history follow the arrow in the image below and press on the `Deployments`.

```python eval
image_zoom(rx.image(src="/view_deployment_logs.webp"))
```

This brings you to the page below where you can see the deployment history of your app. Click on deployment you wish to explore further.

```python eval
image_zoom(rx.image(src="/view_deployment_logs_2.webp", padding_bottom="20px"))
```

```md alert info
# CLI Command to view deployment history
`reflex cloud apps history [OPTIONS] [APP_ID]`
```

This brings you to the page below where you can view the deployment logs of your app by clicking the `Build logs` dropdown.

```python eval
image_zoom(rx.image(src="/view_deployment_logs_3.webp"))
```


## Stopping an App

To stop an app follow the arrow in the image below and press on the `Stop app` button. Pausing an app will stop it from running and will not be accessible to users until you resume it. In addition, this will stop you being billed for your app.

```python eval
image_zoom(rx.image(src="/stopping_app.webp", padding_bottom="20px"))
```

```md alert info
# CLI Command to stop an app
`reflex cloud apps stop [OPTIONS] [APP_ID]`
```

## Deleting an App

To delete an app click on the `Settings` tab in the Cloud UI on the app page.

```python eval
image_zoom(rx.image(src="/environment_variables.webp"))
```

Then click on the `Danger` tab as shown below.

```python eval
image_zoom(rx.image(src="/deleting_app.webp"))
```

Here there is a `Delete app` button. Pressing this button will delete the app and all of its data. This action is irreversible.

```md alert info
# CLI Command to delete an app
`reflex cloud apps delete [OPTIONS] [APP_ID]`
```


## Other app settings

Clicking on the `Settings` tab in the Cloud UI on the app page also allows a user to change the `app name`, change the `app description` and check the `app id`.

The other app settings also allows users to edit and add secrets (environment variables) to the app. For more information on secrets, see the [Secrets (Environment Variables)]({hosting.secrets_environment_vars.path}) page.
