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
deployment comes in.

```md alert info
# Hosting is in Alpha
Please reach out to us on Discord if you have an app ready to deploy and we will give you an invitation code.
```

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        text("Hosting is in Alpha. Please reach out to us on "),
        link("Discord", href=constants.DISCORD_URL),
        text(" if you have an app ready to deploy and if we will give you an invitation code."),
        color_scheme="black",
        weight="bold"
    ),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring your infrastructure.

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
        weight="bold"
    ),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

### Authentication

First, create or log in to your account using the following command. (Requires `Reflex >= v0.3.2`)

```bash
reflex login
```

You will be prompted to your browser where you can authenticate through Github or Gmail.

```python eval
callout_root(
    callout_icon(icon(tag="lock_open_2", width=18, height=18)),
    callout_text(
        text("You will need an invitation code! Contact us on "),
        link("Discord", href=constants.DISCORD_URL),
        text(" if you have an app ready to deploy, and we will give you a code."),
    ),
    size="3",
    color_scheme="green",
    high_contrast=True,
)
```

### Deployment

Once you have successfully logged in to your account, you can deploy your apps.

```python eval
callout_root(
    callout_icon(icon(tag="info_circled", width=18, height=18)),
    callout_text(
        "Make sure you have a requirements.txt containing all your python dependencies at the top level app directory!",
        color="black",
        weight="bold"),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

Navigate to the project you want to deploy and type the following command:

```bash
reflex deploy
```

**Name**: choose a name for the deployed app. This name will be part of the deployed app URL, i.e. `<your-app-name>.reflex.run`. The name should only contain domain name safe characters: no slashes, no underscores. It is also case insensitive, so simply use all lower cases.

**Regions**: check the list of regions you can select from [reflex deployments regions](#reflex-deployments-regions)

That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

## Concepts

### Environment Variables

When deploying to Reflex hosting service, you will be asked if you want to add any environment variables. These are encrypted and safely stored. We will not show you the values of them any CLI commands, only the key names. Make sure to enter the Environment Variables without any quotation marks.

Anything like backend API keys or secrets should be entered here and referenced in your app as an environment variable `os.environ` in the backend python code.

### Redeployment

To redeploy your app, navigate to your project directory and type `reflex deploy` again. This command communicates with the hosting service to automatically detects your existing app under the same name. If your current directory has a `rxconfig` that says your app name is `abc-app`, and you have already deployed an `abc-app`, and this time the deploy command overwrites it. You should see a prompt similar to `Overwriting your app abc-app ... `. This is a complete overwrite and not an incremental update.

## Hosting CLI Commands

All the commands come with help manual. Type `--help` to see it, for example, `reflex deploy --help`. The help manual provides additional options that may be useful.

### Authentication Commands

#### reflex login

1. User types the command for the very first time, CLI opens the hosting service URL login page for user to use one of the OAuth providers to authorize and log in.
2. After user authorizes OAuth access, the page redirects back to a page on the hosting service website. It shows elements only relevant to authenticated users, such as logout button. Note that we are frequently improving our website, the exact view for authenticated user may be different than described here.
3. Your access token is cached locally in the reflex support directory. For subsequent login commands, as long as the access token is valid, the CLI shows “**You’re already logged in**” without opening up your browser again.
4. Cont’d from 3: if the validation fails, the CLI shows 1) “**Session expired**” 2) “**User is banned**” 3) “**Access denied**” (for other cases we have no need to distinguish a bad token or just that user needs to re-authenticate) and CLI  will be opening the browser for re-authentication.
5. If for any reason, there is no cached token on user machine, but the user session is still active on the browser, the hosting service login page will skip the step of redirecting to OAuth provider and show the same page described above in step 2.

```python eval
doccmdoutput(
    command="reflex login",
    output="""Opening https://control-plane.reflex.run ...
Successfully logged in.
""",
)
```

#### reflex logout

1. User types this command, if no token is cached, CLI shows “**Login info not found**”
2. If a token is found, (behind the scene: CLI makes a request to hosting service to delete/deactivate the access token. If the hosting service responds success, ) CLI shows “Successfully logged out”. (If hosting service responds with any error), CLI shows “**Unable to log out, please try again later**” (retryable errors), “**You’re not logged in**”. In all cases, the cached login config is deleted from user machine.

### Deployment Commands

#### reflex deploy

Summary

1. User types `reflex deploy` command.
2. If not in the reflex app root directory (with the rxconfig file), alert “**You must be in the top level directory of your app to deploy**”
3. If not `reflex init` before, it asks the user to run `reflex init` first, this is the same as `reflex run` command
4. If the user does not have `requirements.txt` in the directory, alert.
5. If not all the dependencies are installed, CLI accepts the import errors and alerts the user, “**Did you forget to install all dependencies?**”
6. **Example 1** shows the sequences of a successful deployment.
7. The deploy command by default interacts with the user and prompts for information. To provide all the settings for your app in a one shot without this interaction, use the `--no-interactive` flag. Type `reflex deploy --help` to see the help command for explanation on each flag. There is an example below: example 2. The deploy sequences are the same regardless the command is interactive or not. Example 2 skips the deploy sequences.

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

The non-interactive deploy command requires user to provide all the required information, such as the app name of your choice, the regions to deploy to, environmental variables if you have them.

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

Get the status of a specific app.

```python eval
doccmdoutput(
    command="reflex deployments status clock-gray-piano",
    output="""Getting status for [ clock-gray-piano ] ...

backend_url                               reachable    updated_at
----------------------------------------  -----------  ------------
https://rxh-dev-clock-gray-piano.fly.dev  False        N/A


frontend_url                                 reachable    updated_at
-------------------------------------------  -----------  -----------------------
https://clock-gray-piano.dev.reflexcorp.run  True         2023-10-13 15:23:07 PDT
""",
)
```

#### reflex deployments logs `app-name`

Get the logs from a specified deployment.

```python eval
doccmdoutput(
    command="reflex deployments logs todo",
    output="""Note: there is a few seconds delay for logs to be available.
2023-10-13 22:18:39.696028 | rxh-dev-todo | info | Pulling container image registry.fly.io/rxh-dev-todo:depot-1697235471
2023-10-13 22:18:41.462929 | rxh-dev-todo | info | Pulling Gcontainer image registry.fly.io/rxh-dev-todo@sha256:60b7b531e99e037f2fb496b3e05893ee28f93a454ee618bda89a531a547c4002
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

#### reflex deployments delete `app-name`

Delete a specified deployment.

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
