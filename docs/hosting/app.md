```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import hosting 
from pcweb.pages import docs
from pcweb.styles.styles import get_code_style, cell_style


regions = {
    "ams": "Amsterdam, Netherlands",
    "arn": "Stockholm, Sweden",
    "alt": "Atlanta, Georgia (US)",
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

vmtypes = [
    {"id": "c1m.5", "name": "Single CPU Small", "cpu_cores": 1, "ram_gb": 0.512},
    {"id": "c1m1", "name": "Single CPU Medium", "cpu_cores": 1, "ram_gb": 1.024},
    {"id": "c1m2", "name": "Single CPU Large", "cpu_cores": 1, "ram_gb": 2.048},
    {"id": "c2m.5", "name": "Double CPU Micro", "cpu_cores": 2, "ram_gb": 0.512},
    {"id": "c2m1", "name": "Double CPU Small", "cpu_cores": 2, "ram_gb": 1.024},
    {"id": "c2m2", "name": "Double CPU Medium", "cpu_cores": 2, "ram_gb": 2.048},
    {"id": "c2m4", "name": "Double CPU Large", "cpu_cores": 2, "ram_gb": 4.096},
    {"id": "c4m1", "name": "Quad CPU Micro", "cpu_cores": 4, "ram_gb": 1.024},
    {"id": "c4m2", "name": "Quad CPU Small", "cpu_cores": 4, "ram_gb": 2.048},
    {"id": "c4m4", "name": "Quad CPU Medium", "cpu_cores": 4, "ram_gb": 4.096},
    {"id": "c4m8", "name": "Quad CPU Large", "cpu_cores": 4, "ram_gb": 8.192}
]

```

# App

In Reflex Cloud an "app" (or "application" or "website") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. 

You can deploy an app using the `reflex deploy` command.

There are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.


## VMTypes

To get all the possible VMTypes you can run the following command:

```bash
reflex apps vmtypes
```

To set which VMType to use when deploying your app you can pass the `--vmtype` flag with the id of the VMType. For example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --vmtype c2m4
```

This will deploy your app with the `c2m4` VMType, giving your app 2 cpu cores and 4 gb of ram.

Below is a table of all the possible VMTypes:

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("id"),
            rx.table.column_header_cell("name"),
            rx.table.column_header_cell("cpu (cores)"),
            rx.table.column_header_cell("ram (gb)"),
        ),
    ),
    rx.table.body(
        *[
            rx.table.row(
                rx.table.cell(rx.code(vmtype["id"], style=get_code_style("violet"))),
                rx.table.cell(vmtype["name"], style=cell_style),
                rx.table.cell(vmtype["cpu_cores"], style=cell_style),
                rx.table.cell(vmtype["ram_gb"], style=cell_style),
            )
            for vmtype in vmtypes
        ]
    ),
    variant="surface",
)
```


## Regions

Below is an example of how to deploy your app in several regions:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --region sjc --region iad
```

By default all apps are deloyed in `sjc` if no other regions are given. If you wish to deploy in another region or several regions you can pass the `--region` flag (`-r` also works) with the region code. Check out all the regions that we can deploy to below:


```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Region Code"),
            rx.table.column_header_cell("Region"),
        ),
    ),
    rx.table.body(
        *[
            rx.table.row(
                rx.table.cell(rx.code(region_code, style=get_code_style("violet"))),
                rx.table.cell(region_name, style=cell_style),
            )
            for region_code, region_name in regions.items()
        ]
    ),
    variant="surface",
)
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
