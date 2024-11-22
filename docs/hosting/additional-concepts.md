```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
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
```


# Reflex Cloud - Additional Concepts

To go back, i.e. from an app to a project or from a project to your list of projects you just click the `REFLEX logo` in the top left corner of the page.

## Environment Variables

Below is an example of how to use an environment variable in a deployment command:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --env OPENAI_API_KEY=sk-proj-vD4i9t6U############################
```

They are passed after the `--env` flag as key value pairs. 

To pass multiple environment variables, you can repeat the `--env` tag. i.e. `reflex deploy --project f88b1574-f101-####-####-5f########## --env KEY1=VALUE1 --env KEY2=VALUE`


Alternatively if there is an environment variable file in your project directory you can pass the `--envfile` flag with the path to the env file. For example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --envfile .env
```

In this example the path to the file is `.env`. This will override any envs set manually.


```md alert info
# More information on Environment Variables
Environment variables are encrypted and safely stored. We recommend that backend API keys or secrets are entered as `envs`. Make sure to enter the `envs` without any quotation marks. We do not show the values of them in any CLI commands, only their names (or keys).

You access the values of `envs` by referencing `os.environ` with their names as keys in your app's backend. For example, if you set an env `ASYNC_DB_URL`, you are able to access it by `os.environ["ASYNC_DB_URL"]`. Some Python libraries automatically look for certain environment variables. For example, `OPENAI_API_KEY` for the `openai` python client. The `boto3` client credentials can be configured by setting `AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY`. This information is typically available in the documentation of the Python packages you use.
```

## Adding Team Members

If you are a User you have the ability to create, deploy and delete apps, but you do not have the power to add or delete users from that project. You must be an Admin for that.

As an Admin you will see the an `Add user` button in the top right of the screen, as shown in the image below. Clicking on this will allow you to add a user to the project. You will need to enter the email address of the user you wish to add.

```python eval
image_zoom(rx.image(src="/hosting_adding_team_members.png", alt="Adding team members to Reflex Cloud"))
```

```python eval
rx.box(height="20px")
```

```md alert warning
# Currently a User must already have logged in once before they can be added to a project. 
At this time a User must be logged in to be added to a project. In future there will be automatic email invites sent to add new users who have never logged in before.
```


## Regions

Below is an example of how to deploy your app in several regions:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --region sjc --region iad
```

By default all apps are deloyed in `sjc` if no other regions are given. If you wish to deploy in another region or several regions you can pass the `--region` flag with the region code. Check out all the regions that we can deploy to below:


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




## Tokens

A token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the `--token` flag. A good use case would be for GitHub actions (you store this token in the secrets).

Tokens are found on the Project List page. If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below.

```python eval
image_zoom(rx.image(src="/hosting_tokens.png", alt="Adding tokens to Reflex Cloud"))
```


## VMTypes


!!!!!!!!!!!!!!!! Still to come
c1m1
c1m2 
!!!!!!!!!!!!