# Reflex Hosting Service CLI Commands

```python exec
import reflex as rx
from pcweb import constants
from pcweb.templates.docpage import doccmdoutput
from pcweb.styles.styles import get_code_style, cell_style


regions = {
    "alt": "Atlanta, Georgia (US)",
    "bog": "Bogotá, Colombia",
    "bos": "Boston, Massachusetts (US)",
    "cdg": "Paris, France",
    "den": "Denver, Colorado (US)",
    "dfw": "Dallas, Texas (US)",
    "eze": "Ezeiza, Argentina",
    "fra": "Frankfurt, Germany",
    "hkg": "Hong Kong, Hong Kong",
    "iad": "Ashburn, Virginia (US)",
    "lax": "Los Angeles, California (US)",
    "lhr": "London, United Kingdom",
    "mad": "Madrid, Spain",
    "mia": "Miami, Florida (US)",
    "ord": "Chicago, Illinois (US)",
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

## Concepts

### Requirements

To be able to deploy your app, we ask that you prepare a `requirements.txt` file containing all the required Python packages for it. The hosting service runs a `pip install` command based on this file to prepare the instances that run your app. We recommend that  you use a Python virtual environment when starting a new app, and only install the necessary packages. This reduces the preparation time installing no more packages than needed, and your app is deployed faster. There are a lot of resources online on Python virtual environment tools and how to capture the packages in a `requirements.txt` file.

### Environment Variables

When deploying to Reflex's hosting service, the command prompt asks if you want to add any environment variables. These are encrypted and safely stored. We recommend that backend API keys or secrets are entered as `envs`. Make sure to enter the `envs` without any quotation marks.

The environment variables are key value pairs. We do not show the values of them in any CLI commands, only their names (or keys). However, if your app intentionally prints the values of these variables, the logs returned still contain the printed values. At the moment, the logs are not censored for anything resembling secrets. Only the app owner and Reflex team admins can access these logs.

You access the values of `envs` by referencing `os.environ` with their names as keys in your app's backend. For example, if you set an env `ASYNC_DB_URL`, you are able to access it by `os.environ["ASYNC_DB_URL"]`. Some Python libraries automatically look for certain environment variables. For example, `OPENAI_API_KEY` for the `openai` python client. The `boto3` client credentials can be configured by setting `AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY`. This information is typically available in the documentation of the Python packages you use.

### Updating Deployment

To redeploy or update your app, navigate to the project directory and type `reflex deploy` again. This command communicates with the hosting service to automatically detect your existing app with the same name. This time the deploy command overwrites the app. You should see a prompt similar to `Overwrite deployment [ app-name ] ...`. This operation is a complete overwrite and not an incremental update.

## CLI Command Reference

All the `reflex` commands come with a help manual. The help manual lists additional command options that may be useful. You type `--help` to see the help manual. Some commands are organized under a `subcommands` series. Here is an example below. Note that the help manual may look different depending on the version of `reflex` or the `reflex-hosting-cli`.

``` bash
reflex deployments --help
```

### Authentication Commands

#### reflex login

When you type the `reflex login` command for the very first time, it opens the hosting service login page in your browser. We authenticate users through OAuth. At the moment the supported OAuth providers are Github and Gmail. You should be able to revoke such authorization on your Github and Google account settings page. We do not log into your Github or Gmail account. OAuth authorization provides us your email address and in case of Github your username handle. We use those to create an account for you. The email used in the original account creation is used to identify you as a user. If you have authenticated using different emails, those create separate accounts. To switch to another account, first log out using the `reflex logout` command. More details on the logout command are in [reflex logout](#reflex-logout) section.

``` bash
reflex login
```

After authentication, the browser redirects to the original hosting service login page. It shows that you have logged in. Now you can return to the terminal where you type the login command. It should print a message such as `Successfully logged in`.

Your access token is cached locally in the reflex support directory. For subsequent login commands, the cached token is validated first. If the token is still valid, the CLI command simply shows `You’re already logged in`. If the token is expired or simply not valid for any reason, the login command tries to open your browser again for web based authentication.

#### reflex logout

When you successfully authenticate with the hosting service, there is information cached in two different places: a file containing the access token in the reflex support directory, and cookies in your browser. The cookies include the access token, a refresh token, some unix epochs indicating when the access token expires. The logout command removes the cached information from these places.

### Deployment Commands

#### reflex deploy

This is the command to deploy a reflex app from its top level app directory. This directory contains a `rxconfig.py` where you run `reflex init` and `reflex run`.

A `requirements.txt` file is required. The deploy command checks the content of this file against the top level packages installed in your current Python environment. If the command detects new packages in your Python environment, or newer versions of the same packages, it prints the difference and asks if you would like to update your `requirements.txt`. Make sure you double check the suggested updates. This functionality is added in more recent versions of the hosting CLI package `reflex-hosting-cli>=0.1.3`.

``` bash
reflex deploy
```

The deploy command is by default interactive. To deploy without interaction, add `--no-interactive` and set the relevant command options as deployment settings. Type `reflex deploy --help` to see the help manual for explanations on each option. The deploy sequences are the same, whether the deploy command is interactive or not.

```bash
reflex deploy --no-interactive -k todo -r sjc -r sea --env OPENAI_API_KEY=YOU-KEY-NO-EXTRA-QUOTES --env DB_URL=YOUR-EXTERNAL-DB-URI --env KEY3=THATS-ALOTOF-KEYS
```

#### reflex deployments list

List all your deployments.

``` bash
reflex deployments list
```

#### reflex deployments status `app-name`

Get the status of a specific app, including backend and frontend.

``` bash
reflex deployments status clock-gray-piano
```

#### reflex deployments logs `app-name`

Get the logs from a specific deployment.

The returned logs are the messages printed to console. If you have `print` statements in your code, they show up in these logs. By default, the logs command return the latest 100 lines of logs and continue to stream any new lines.

We have added more options to this command including `from` and `to` timestamps and the limit on how many lines of logs to fetch. Accepted timestamp formats include the ISO 8601 format, unix epoch and relative timestamp. A relative timestamp is some time units ago from `now`. The units are `d (day), h (hour), m (minute), s (second)`. For example, `--from 3d --to 4h` queries from 3 days ago up to 4 hours ago. For the exact syntax in the version of CLI you use, refer to the help manual.

``` bash
reflex deployments logs todo
```

#### reflex deployments build-logs `app-name`

Get the logs of the hosting service deploying the app.

``` bash
reflex deployments build-logs webcam-demo
```

The hosting service prints log messages when preparing and deploying your app. These log messages are called build logs. Build logs are useful in troubleshooting deploy failures. For example, if there is a package `numpz==1.26.3` (supposed to be `numpy`) in the `requirements.txt`, hosting service will be unable to install it. That package does not exist. We expect to find a few lines in the build logs indicating that the `pip install` command fails.

#### reflex deployments delete `app-name`

Delete a specific deployment.

### Public Commands

These commands do not require authentication.

#### reflex deployments regions

List all the valid regions to select for a deployment.

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
