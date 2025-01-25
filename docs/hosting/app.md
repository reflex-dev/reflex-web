```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import hosting 
from pcweb.pages import docs
from pcweb.styles.styles import get_code_style, cell_style


regions = {
    "ams": "Amsterdam, Netherlands",
    "arn": "Stockholm, Sweden",
    "atl": "Atlanta, Georgia (US)",
    "bog": "Bogotá, Colombia",
    "bom": "Mumbai, India",
    "bos": "Boston, Massachusetts (US)",
    "cdg": "Paris, France",
    "den": "Denver, Colorado (US)",
    "dfw": "Dallas, Texas (US)",
    "ewr": "Secaucus, NJ (US)",
    "eze": "Ezeiza, Argentina",
    "fra": "Frankfurt, Germany",
    "gdl": "Guadalajara, Mexico",
    "gig": "Rio de Janeiro, Brazil",
    "gru": "Sao Paulo, Brazil",
    "hkg": "Hong Kong, Hong Kong",
    "iad": "Ashburn, Virginia (US)",
    "jnb": "Johannesburg, South Africa",
    "lax": "Los Angeles, California (US)",
    "lhr": "London, United Kingdom",
    "mad": "Madrid, Spain",
    "mia": "Miami, Florida (US)",
    "nrt": "Tokyo, Japan",
    "ord": "Chicago, Illinois (US)",
    "otp": "Bucharest, Romania",
    "phx": "Phoenix, Arizona (US)",
    "qro": "Querétaro, Mexico",
    "scl": "Santiago, Chile",
    "sea": "Seattle, Washington (US)",
    "sin": "Singapore, Singapore",
    "sjc": "San Jose, California (US)",
    "syd": "Sydney, Australia",
    "waw": "Warsaw, Poland",
    "yul": "Montreal, Canada",
    "yyz": "Toronto, Canada"
}


```

# App

In Reflex Cloud an "app" (or "application" or "website") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. 

You can deploy an app using the `reflex deploy` command.

There are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.


## VMTypes


To scale your app you can choose different VMTypes. VMTypes are different configurations of CPU and RAM.

To scale your VM in the Cloud UI, click on the `Settings` tab in the Cloud UI on the app page, and then click on the `Scale` tab as shown below. Clicking on the `Change VM` button will allow you to scale your app.


```python eval
image_zoom(rx.image(src="/scaling_vms.webp", padding_bottom="20px"))
```

### VMTypes in the CLI

To get all the possible VMTypes you can run the following command:

```bash
reflex apps vmtypes
```

To set which VMType to use when deploying your app you can pass the `--vmtype` flag with the id of the VMType. For example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --vmtype c2m4
```

This will deploy your app with the `c2m4` VMType, giving your app 2 CPU cores and 4 GB of RAM.



## Regions

To scale your app you can choose different regions. Regions are different locations around the world where your app can be deployed. 

To scale your app to multiple regions in the Cloud UI, click on the `Settings` tab in the Cloud UI on the app page, and then click on the `Regions` tab as shown below. Clicking on the `Add new region` button will allow you to scale your app to multiple regions.

```python eval
image_zoom(rx.image(src="/scaling_regions.webp", padding_bottom="20px"))
```

The images below show all the regions that can be deployed in.

```python eval
rx.hstack(
    image_zoom(rx.image(src="/regions_1.webp", padding_bottom="20px")),
    image_zoom(rx.image(src="/regions_2.webp", padding_bottom="20px")),
)
```


### Selecting Regions to Deploy in the CLI

Below is an example of how to deploy your app in several regions:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --region sjc --region iad
```

By default all apps are deloyed in `sjc` if no other regions are given. If you wish to deploy in another region or several regions you can pass the `--region` flag (`-r` also works) with the region code. Check out all the regions that we can deploy to below:


## Config File

To create a `config.yml` file for your app run the command below:

```bash
reflex cloud config
```

This will create a yaml file similar to the one below where you can edit the app configuration:

```yaml
name: medo
description: ''
regions:
  sjc: 1
  lhr: 2
vmtype: c1m1
hostname: null
envfile: .env
project: null
packages:
- procps
```



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
