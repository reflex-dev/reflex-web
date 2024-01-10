# Reflex Hosting Service

```python exec
import reflex as rx
from pcweb import constants
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
        color="black",
        weight="bold"),
    size="3",
    color_scheme="blue",
    high_contrast=True,
)
```

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring your infrastructure.

(This tutorial assumes you’ve successfully `reflex init` and `reflex run` your app)

### Authentication

First, create or log in to your account using the following command. (Requires Reflex > `v0.3.1`)

```bash
reflex login
```

You will be prompted to your browser where you can create an account using Github or Gmail for authentication.

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

**Name**: choose a name that will be the start of your url, i.e. `<your-app-name>.reflex.run`. The name should only contain domain name safe characters, so no slashes, no underscores. It is also case insensitive, use all lower cases.

**Regions**: check the list of regions you can select from [reflex deployments regions](https://www.notion.so/reflex-deployments-regions-a066211142b945a8bc86697326994dbd?pvs=21)

That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

Once your app is deployed, you will see a URL with your live site.

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

#### reflex deployments list

List all your deployments.

#### reflex deployments status `app-name`

#### reflex deployments logs `app-name`

#### reflex deployments build-logs `app-name`

#### reflex deployments delete `app-name`


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
