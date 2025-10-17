```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import hosting 
from pcweb.pages import docs
from pcweb.styles.styles import get_code_style, cell_style


regions = {
    "ams": "Amsterdam, Netherlands",
    "arn": "Stockholm, Sweden",
    "bom": "Mumbai, India",
    "cdg": "Paris, France",
    "dfw": "Dallas, Texas (US)",
    "ewr": "Secaucus, NJ (US)",
    "fra": "Frankfurt, Germany",
    "gru": "Sao Paulo, Brazil",
    "iad": "Ashburn, Virginia (US)",
    "jnb": "Johannesburg, South Africa",
    "lax": "Los Angeles, California (US)",
    "lhr": "London, United Kingdom",
    "nrt": "Tokyo, Japan",
    "ord": "Chicago, Illinois (US)",
    "sin": "Singapore, Singapore",
    "sjc": "San Jose, California (US)",
    "syd": "Sydney, Australia",
    "yyz": "Toronto, Canada"
}


```

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

