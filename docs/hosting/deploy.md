# Reflex Hosting Service

```python exec
import reflex as rx
from pcweb import constants
from pcweb.templates.docpage import doccmdoutput
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

So far, we've been running our apps locally on our own machines.
But what if we want to share our apps with the world?  This is where
the hosting service comes in.

```md alert info
Hosting is in Alpha. Please reach out to us on Discord if you are ready to deploy and we will give you an invitation code.
```

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        text("Hosting is in Alpha. Please reach out to us on "),
        link("Discord", href=constants.DISCORD_URL),
        text(" if you are ready to deploy and we will give you an invitation code."),
        color_scheme="black",
        font_weight="bold"
    ),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.

```md alert info
This tutorial assumes you’ve successfully `reflex init` and `reflex run` your app.
```

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        text("This tutorial assumes you’ve successfully "),
        code("reflex init"),
        text(" and "),
        code("reflex run"),
        text(" your app"),
        color="black",
        font_weight="bold"
    ),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

### Authentication

```md alert info
Hosting service requires `reflex>=0.3.2`.
```

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        text("Hosting service requires "),
        code("reflex>=0.3.2"),
        color="black",
        font_weight="bold",
    ),
    size="3",
    color_scheme="green",
    high_contrast=True,
)
```

First, create or log in to your account using the following command.

```bash
reflex login
```

You will be prompted to your browser where you can authenticate through Github or Gmail.

```md alert info
You will need an invitation code! Contact us on Discord if you have an app ready to deploy, and we will give you a code.
```

```python eval
callout_root(
    callout_icon(icon(tag="lock_open_2", width=18, height=18)),
    callout_text(
        text("You will need an invitation code! Contact us on "),
        link("Discord", href=constants.DISCORD_URL),
        text(" if you have an app ready to deploy, and we will give you a code."),
        color="black",
        font_weight="bold",
    ),
    size="3",
    color_scheme="green",
    high_contrast=True,
)
```

### Deployment

Once you have successfully authenticated, you can deploy your apps.

```md alert warning
Make sure you have a `requirements.txt`  file at the top level app directory that contains all your python dependencies!
```

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        "Make sure you have a ",
        code("requirements.txt"),
        " file at the top level app directory that contains all your python dependencies !",
        color="black",
        weight="bold"),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

Navigate to the project directory that you want to deploy and type the following command:

```bash
reflex deploy
```

The command is by default interactive. It asks you a few questions for information required for the deployment.

**Name**: choose a name for the deployed app. This name will be part of the deployed app URL, i.e. `<app-name>.reflex.run`. The name should only contain domain name safe characters: no slashes, no underscores. Domain names are case insensitive. To avoid confusion, the name you choose here is also case insensitive. If you enter letters in upper cases, we automatically convert them to lower cases.

**Regions**: enter the region code here or press `Enter` to accept the default. The default code `sjc` stands for San Jose, California in the US west coast. Check the list of supported regions at [reflex deployments regions](#reflex-deployments-regions).

**Envs**: `Envs` are environment variables. You might not have used them at all in your app. In that case, press `Enter` to skip. More on the environment variables in the later section [Environment Variables](#environment-variables).

That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

```md alert info
Once your code is uploaded, the hosting service will start the deployment. Exiting from the command from that point on **does not** affect the deployment process. The command prints a message when you can close the command without affecting the deployment.
```

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        "Once your code is uploaded, the hosting service will start the deployment. Exiting from the command from that point on does not affect the deployment process. The command prints a message when you can close the command without affecting the deployment.",
        color="black",
        weight="bold"),
    size="3",
    color_scheme="green",
    high_contrast=True,
)
```

## Concepts

### Requirements

To be able to deploy your app, we ask that you prepare a `requirements.txt` file containing all the required Python packages for it. The hosting service runs a `pip install` command based on this file to prepare the instances that run your app. We recommend that  you use a Python virtual environment when starting a new app, and only install the necessary packages. This reduces the preparation time installing no more packages than needed, and your app is deployed faster. There are a lot of resources online on Python virtual environment tools and how to capture the packages in a `requirements.txt` file.

### Environment Variables

When deploying to Reflex's hosting service, the command prompt asks if you want to add any environment variables. These are encrypted and safely stored. We do not show the values of them in any CLI commands, only their names (or keys). We recommend that backend API keys or secrets are entered as `envs`. Make sure to enter the `Environment Variables` without any quotation marks.

However, if your app intentionally prints the values of these variables, the logs returned still contain the printed values. At the moment, the logs are not censored against anything resembling secrets. Only the app owner and Reflex team admins can access these logs.

The environment variables are key value pairs. You access their values by referencing their names as keys in `os.environ` in your app's backend. For example, if you set an env `ASYNC_DB_URL`, you are able to access it by `os.environ["ASYNC_DB_URL"]`. Some Python libraries automatically look for certain environment variables. For example, `OPENAI_API_KEY` for the `openai` python client. The `boto3` client credentials can be configured by setting `AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY`.

### Updating Deployment

To redeploy or update your app, navigate to the project directory and type `reflex deploy` again. This command communicates with the hosting service to automatically detects your existing app by the same name. This time the deploy command overwrites the app. You should see a prompt similar to `Overwrite deployment [ app-name ] ...`. This operation is a complete overwrite and not an incremental update.

## Hosting CLI Commands

All the `reflex` commands come with a help manual. The help manual provides additional options that may be useful. You type `--help` to see the help manual. Some commands are organized under a `subcommands` series. Here is an example below. Note that the help manual may look different depending on the version of `reflex` or the `reflex-hosting-cli`.

```python eval
doccmdoutput(
    command="reflex deployments --help",
    output="""Usage: reflex deployments [OPTIONS] COMMAND [ARGS]...

  Subcommands for managing the Deployments.

Options:
  --help  Show this message and exit.

Commands:
  build-logs  Get the build logs for a deployment.
  delete      Delete a hosted instance.
  list        List all the hosted deployments of the authenticated user.
  logs        Get the logs for a deployment.
  regions     List all the regions of the hosting service.
  status      Check the status of a deployment.
"""
)
```

`--loglevel` is another common `reflex` command option. When setting `--loglevel debug`, a command prints additional information, which can be helpful during debug.

### Authentication Commands

#### reflex login

When you type the `reflex login` command for the very first time, it opens the hosting service login page. We authenticate users through OAuth. At the moment the supported OAuth providers are Github and Gmail. You should be able to revoke such authorization on your Github and Google account settings page. We do not log into your Github or Gmail account. OAuth authorization provides us your email address and in case of Github your username handle. We use those to create an account for you. When you return, the email used in the original account creation is used to identify you as a user. If you have authenticated using different emails, those create separate accounts. To switch to another account, first log out using the `reflex logout` command. More details on the logout command are in [reflex logout](#reflex-logout) section.

```python eval
doccmdoutput(
    command="reflex login",
    output="""Opening https://control-plane.reflex.run ...
Successfully logged in.
""",
)
```

After authenticated, the browser redirects to the original hosting service page. It shows you have logged in. Now you can return to the terminal where you type the login command. It should print a message such as `Successfully logged in`.

Your access token is cached locally in the reflex support directory. For subsequent login commands, the cached token is validated first. If the token is still valid, the CLI command simply shows `You’re already logged in`. If the token is expired or simply not valid for any reason, the login command tries to open your browser again for web based authentication.

#### reflex logout

When you successfully authenticate with the hosting service, there is information cached in two different places: a file containing the access token in the reflex support folder, and cookies in your browser. The cookies include the access token, a refresh token, some unix epochs indicating when the access token expires. The logout command removes the cached information from these places.

### Deployment Commands

#### reflex deploy

This is the command to deploy a reflex app from its top level app directory. This directory contains a `rxconfig.py` where you run `reflex init` and `reflex run`. A `requirements.txt` file is required. The deploy command checks the existence of this file and also the content of it (this is available in more recent versions of `reflex-hosting-cli` such as `0.1.3`). The command prompts you for updates on the requirements when there are new packages or newer versions of packages detected in the Python environment.

```python eval
doccmdoutput(
    command="reflex deploy",
    output="""Name of deployment (todo-blue-ocean): todo
Region to deploy to (sjc): lax
Environment variables ...
  Env name (enter to skip):
No envs added. Continuing ...
-------------------------- Compiling production app and preparing for export. -------------------
Compiling:  ---------------------------------------- 100% 2/2 0:00:00
Creating Production Build:  ---------------------------------------- 100% 9/9 0:00:08
Zipping Frontend: --------------------------------------- 100% 19/19 0:00:00
Zipping Backend: ---------------------------------------- 100% 4/4 0:00:00
Uploading code ...
Deployment will start shortly.
Waiting for the new deployment to come up
Backend is up
frontend is up
Your site [ todo ] at ['lax'] is up: https://todo.reflex.run
""",
)
```

The deploy command is by default interactive and prompts you for information. To provide all the settings for your app in one shot without the interaction, add the `--no-interactive` option. Type `reflex deploy --help` to see the help command for explanation on each option. The deploy sequences are the same whether the command is interactive or not.

The non-interactive deploy command requires you to provide all the required information, such as the app name of your choice, the regions to deploy to, environmental variables if you have them.

```bash
reflex deploy --no-interactive -k todo -r sjc -r sea --env OPENAI_API_KEY=YOU-KEY-NO-EXTRA-QUOTES --env DB_URL=YOUR-EXTERNAL-DB-URI --env KEY3=THATS-ALOTOF-KEYS
```

#### reflex deployments list

List all your deployments.

```python eval
doccmdoutput(
    command="reflex deployments list",
    output="""key                           regions  app_name              reflex_version       cpus     memory_mb  url                                         envs
----------------------------  -------  --------------------  ----------------  -------   -----------  ------------------------------------------  ---------
webui-navy-star               ['sjc']  webui                 0.3.7                   1          1024  https://webui-navy-star.reflex.run          ['OPENAI_API_KEY']
chatroom-teal-ocean           ['ewr']  chatroom              0.3.2                   1          1024  https://chatroom-teal-ocean.reflex.run      []
sales-navy-moon               ['phx']  sales                 0.3.4                   1          1024  https://sales-navy-moon.reflex.run          []
simple-background-tasks       ['yul']  lorem_stream          0.3.7                   1          1024  https://simple-background-tasks.reflex.run  []
snakegame                     ['sjc']  snakegame             0.3.3                   1          1024  https://snakegame.reflex.run                []
basic-crud-navy-apple         ['dfw']  basic_crud            0.3.8                   1          1024  https://basic-crud-navy-apple.reflex.run    []
""",
)
```

#### reflex deployments status `app-name`

Get the status of a specific app, including backend and frontend.

```python eval
doccmdoutput(
    command="reflex deployments status clock-gray-piano",
    output="""Getting status for [ clock-gray-piano ] ...

backend_url                                reachable    updated_at
-----------------------------------------  -----------  ------------
https://rxh-prod-clock-gray-piano.fly.dev  False        N/A


frontend_url                               reachable    updated_at
-----------------------------------------  -----------  -----------------------
https://clock-gray-piano.reflex.run        True         2023-10-13 15:23:07 PDT
""",
)
```

#### reflex deployments logs `app-name`

Get the logs from a specific deployment.

The returned logs are the console messages. If you have `print` statements in your code, they show up in these logs. By default, the logs command return the latest 100 lines of logs and continue to stream any new lines.

We have added more options to this command including `from` and `to` timestamps and the limit on how many lines of logs to fetch. Accepted timestamp formats include the ISO 8601 format, unix epoch and relative timestamp. A relative timestamp is some time units ago from `now`. The units are `d (day), h (hour), m (minute), s (second)`. For example, `--from 3d --to 4h` queries from 3 days ago up to 4 hours ago. For the exact syntax in the version of CLI you use, refer to the help manual.

```python eval
doccmdoutput(
    command="reflex deployments logs todo",
    output="""Note: there is a few seconds delay for logs to be available.
2023-10-13 22:18:39.696028 | rxh-dev-todo | info | Pulling container image registry.fly.io/rxh-dev-todo:depot-1697235471
2023-10-13 22:18:41.462929 | rxh-dev-todo | info | Pulling container image registry.fly.io/rxh-dev-todo@sha256:60b7b531e99e037f2fb496b3e05893ee28f93a454ee618bda89a531a547c4002
2023-10-13 22:18:45.963840 | rxh-dev-todo | info | Successfully prepared image registry.fly.io/rxh-dev-todo@sha256:60b7b531e99e037f2fb496b3e05893ee28f93a454ee618bda89a531a547c4002 (4.500906837s)
2023-10-13 22:18:46.134860 | rxh-dev-todo | info | Successfully prepared image registry.fly.io/rxh-dev-todo:depot-1697235471 (6.438815793s)
2023-10-13 22:18:46.210583 | rxh-dev-todo | info | Configuring firecracker
2023-10-13 22:18:46.434645 | rxh-dev-todo | info | [    0.042971] Spectre V2 : WARNING: Unprivileged eBPF is enabled with eIBRS on, data leaks possible via Spectre v2 BHB attacks!
2023-10-13 22:18:46.477693 | rxh-dev-todo | info | [    0.054250] PCI: Fatal: No config space access function found
2023-10-13 22:18:46.664016 | rxh-dev-todo | info | Configuring firecracker
""",
)
```

#### reflex deployments build-logs `app-name`

Get the logs of the hosting service deploying the app.

```python eval
doccmdoutput(
    command="reflex deployments build-logs webcam-demo",
    output="""Note: there is a few seconds delay for logs to be available.
2024-01-08 11:02:46.109785 PST | fly-controller-prod | #8 extracting sha256:bd9ddc54bea929a22b334e73e026d4136e5b73f5cc29942896c72e4ece69b13d 0.0s done | None | None
2024-01-08 11:02:46.109811 PST | fly-controller-prod | #8 DONE 5.3s | None | None
2024-01-08 11:02:46.109834 PST | fly-controller-prod |  | None | None
2024-01-08 11:02:46.109859 PST | fly-controller-prod | #8 [1/4] FROM public.ecr.aws/p3v4g4o2/reflex-hosting-base:v0.1.8-py3.11@sha256:9e8569507f349d78d41a86e1eb29a15ebc9dece487816875bbc874f69dcf7ecf | None | None
...
...
2024-01-08 11:02:50.913748 PST | fly-controller-prod | #11 [4/4] RUN . /home/reflexuser/venv/bin/activate && pip install --no-color --no-cache-dir -q -r /home/reflexuser/app/requirements.txt reflex==0.3.4 | None | None
...
...
2024-01-08 11:03:07.430922 PST | fly-controller-prod | #12 pushing layer sha256:d9212ef47485c9f363f105a05657936394354038a5ae5ce03c6025f7f8d2d425 3.5s done | None | None
2024-01-08 11:03:07.881471 PST | fly-controller-prod | #12 pushing layer sha256:ee46d14ae1959b0cacda828e5c4c1debe32c9c4c5139fb670cde66975a70c019 3.9s done | None | None
...
2024-01-08 11:03:13.943166 PST | fly-controller-prod | Built backend image | None | None
2024-01-08 11:03:13.943174 PST | fly-controller-prod | Deploying backend image... | None | None
2024-01-08 11:03:13.943311 PST | fly-controller-prod | Running sys_run | None | None
...
2024-01-08 11:03:31.005887 PST | fly-controller-prod | Checking for valid image digest to be deployed to machines... | None | None
2024-01-08 11:03:31.005893 PST | fly-controller-prod | Running sys_run | None | None
2024-01-08 11:03:32.411762 PST | fly-controller-prod | Backend updated! | None | None
2024-01-08 11:03:32.481276 PST | fly-controller-prod | Deploy success (backend) | None | None
""",
)
```

The hosting service prints log messages when preparing and deploying your app. These log messages are called build logs. Build logs are useful in troubleshooting deploy failures. For example, if there is a package `numpz==1.26.3` (supposed to be `numpy`) in the `requirements.txt`, hosting service will be unable to install it. That package does not exist. We expect to find a few lines in the build logs indicating that the `pip install` command fails.

During the deploy command, we print a few lines of the deploy sequence "milestones" from the build logs, such as `Backend updated!`, `Deploy success (frontend)`.

#### reflex deployments delete `app-name`

Delete a specific deployment.

### Public Commands

These commands do not require authentication.

#### reflex deployments regions

List all the valid regions to select for a deployment.

```python eval
table_root(
    table_header(
        table_row(
            table_column_header_cell("Region Code"),
            table_column_header_cell("Region"),
        ),
    ),
    table_body(
        table_row(
            table_row_header_cell("alt"),
            table_cell("Atlanta, Georgia (US)"),
        ),
        table_row(
            table_row_header_cell("bog"),
            table_cell("Bogotá, Colombia"),
        ),
        table_row(
            table_row_header_cell("bos"),
            table_cell("Boston, Massachusetts (US)"),
        ),
        table_row(
            table_row_header_cell("cdg"),
            table_cell("Paris, France"),
        ),
        table_row(
            table_row_header_cell("den"),
            table_cell("Denver, Colorado (US)"),
        ),
        table_row(
            table_row_header_cell("dfw"),
            table_cell("Dallas, Texas (US)"),
        ),
        table_row(
            table_row_header_cell("eze"),
            table_cell("Ezeiza, Argentina"),
        ),
        table_row(
            table_row_header_cell("fra"),
            table_cell("Frankfurt, Germany"),
        ),
        table_row(
            table_row_header_cell("hkg"),
            table_cell("Hong Kong, Hong Kong"),
        ),
        table_row(
            table_row_header_cell("iad"),
            table_cell("Ashburn, Virginia (US)"),
        ),
        table_row(
            table_row_header_cell("lax"),
            table_cell("Los Angeles, California (US)"),
        ),
        table_row(
            table_row_header_cell("lhr"),
            table_cell("London, United Kingdom"),
        ),
        table_row(
            table_row_header_cell("mad"),
            table_cell("Madrid, Spain"),
        ),
        table_row(
            table_row_header_cell("mia"),
            table_cell("Miami, Florida (US)"),
        ),
        table_row(
            table_row_header_cell("ord"),
            table_cell("Chicago, Illinois (US)"),
        ),
        table_row(
            table_row_header_cell("scl"),
            table_cell("Santiago, Chile"),
        ),
        table_row(
            table_row_header_cell("sea"),
            table_cell("Seattle, Washington (US)"),
        ),
        table_row(
            table_row_header_cell("sin"),
            table_cell("Singapore, Singapore"),
        ),
        table_row(
            table_row_header_cell("sjc"),
            table_cell("San Jose, California (US)"),
        ),
        table_row(
            table_row_header_cell("syd"),
            table_cell("Sydney, Australia"),
        ),
        table_row(
            table_row_header_cell("waw"),
            table_cell("Warsaw, Poland"),
        ),
        table_row(
            table_row_header_cell("yul"),
            table_cell("Montréal, Canada"),
        ),
        table_row(
            table_row_header_cell("yyz"),
            table_cell("Toronto, Canada"),
        ),
    ),
    variant="surface",
)
```
