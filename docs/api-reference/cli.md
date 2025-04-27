# CLI

The `reflex` command line interface (CLI) is a tool for creating and managing Reflex apps.

To see a list of all available commands, run `reflex --help`.

```bash
$ reflex --help

Usage: reflex [OPTIONS] COMMAND [ARGS]...

  Reflex CLI to create, run, and deploy apps.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  cloud      The Hosting CLI.
  component  CLI for creating custom components.
  db         Subcommands for managing the database schema.
  deploy     Deploy the app to the Reflex hosting service.
  export     Export the app to a zip file.
  init       Initialize a new Reflex app in the current directory.
  login      Authenticate with experimental Reflex hosting service.
  logout     Log out of access to Reflex hosting service.
  rename     Rename the app in the current directory.
  run        Run the app in the current directory.
  script     Subcommands for running helper scripts.
```

## Init

The `reflex init` command creates a new Reflex app in the current directory.
If an `rxconfig.py` file already exists already, it will re-initialize the app with the latest template.

```bash
$ reflex init --help
Usage: reflex init [OPTIONS]

  Initialize a new Reflex app in the current directory.

Options:
  --name APP_NAME                 The name of the app to initialize.
  --template [demo|sidebar|blank]
                                  The template to initialize the app with.
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
```

## Run

The `reflex run` command runs the app in the current directory.

By default it runs your app in development mode.
This means that the app will automatically reload when you make changes to the code.
You can also run in production mode which will create an optimized build of your app.

You can configure the mode, as well as other options through flags.

```bash
$ reflex run --help
Usage: reflex run [OPTIONS]

  Run the app in the current directory.

Options:
  --env [dev|prod]                The environment to run the app in.
                                  [default: Env.DEV]
  --frontend-only                 Execute only frontend.
  --backend-only                  Execute only backend.
  --frontend-port TEXT            Specify a different frontend port.
                                  [default: 3000]
  --backend-port TEXT             Specify a different backend port.  [default:
                                  8000]
  --backend-host TEXT             Specify the backend host.  [default:
                                  0.0.0.0]
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
```

## Export

You can export your app's frontend and backend to zip files using the `reflex export` command.

The frontend is a compiled NextJS app, which can be deployed to a static hosting service like Github Pages or Vercel.
However this is just a static build, so you will need to deploy the backend separately.
See the self-hosting guide for more information.

## Rename

The `reflex rename` command allows you to rename your Reflex app. This updates the app name in the configuration files.

```bash
$ reflex rename --help
Usage: reflex rename [OPTIONS] NEW_NAME

  Rename the app in the current directory.

Options:
  --loglevel [debug|default|info|warning|error|critical]
                                  The log level to use.
  --help                          Show this message and exit.
```

## Cloud

The `reflex cloud` command provides access to the Reflex Cloud hosting service. It includes subcommands for managing apps, projects, secrets, and more.

```bash
$ reflex cloud --help
Usage: reflex cloud [OPTIONS] COMMAND [ARGS]...

  The Hosting CLI.

  This CLI is used to manage the Reflex cloud hosting service. It provides
  commands for managing apps, projects, secrets, and VM types/regions.

Options:
  --help  Show this message and exit.

Commands:
  apps     Commands for managing apps.
  config   Generate a configuration file for the cloud deployment.
  project  Commands for managing projects.
  regions  List all the regions of the hosting service.
  secrets  Commands for managing secrets.
  vmtypes  Retrieve the available VM types.
```

### Cloud Apps

The `reflex cloud apps` subcommand provides tools for managing your deployed applications.

```bash
$ reflex cloud apps --help
Usage: reflex cloud apps [OPTIONS] COMMAND [ARGS]...

  Commands for managing apps.

Options:
  --help  Show this message and exit.

Commands:
  build-logs  Retrieve the build logs for a specific deployment.
  delete      Delete an application.
  history     Retrieve the deployment history for a given application.
  list        List all the hosted deployments of the authenticated user.
  logs        Retrieve logs for a given application.
  scale       Scale an application by changing the VM type or...
  start       Start a stopped application.
  status      Retrieve the status of a specific deployment.
  stop        Stop a running application.
```

### Cloud Project

The `reflex cloud project` subcommand allows you to manage your Reflex Cloud projects.

```bash
$ reflex cloud project --help
Usage: reflex cloud project [OPTIONS] COMMAND [ARGS]...

  Commands for managing projects.

Options:
  --help  Show this message and exit.

Commands:
  create          Create a new project.
  get-select      Get the currently selected project.
  invite          Invite a user to a project.
  list            List all the projects of the authenticated user.
  role-permissions  List all the permissions for each role.
  select          Select a project.
  usage           Get the usage of a project.
  users           List all the users in a project.
```

### Cloud Secrets

The `reflex cloud secrets` subcommand allows you to manage environment variables for your deployed applications.

```bash
$ reflex cloud secrets --help
Usage: reflex cloud secrets [OPTIONS] COMMAND [ARGS]...

  Commands for managing secrets.

Options:
  --help  Show this message and exit.

Commands:
  delete  Delete a secret.
  list    List all the secrets of a project.
  update  Update a secret.
```

## Script

The `reflex script` command provides access to helper scripts for Reflex development.

```bash
$ reflex script --help
Usage: reflex script [OPTIONS] COMMAND [ARGS]...

  Subcommands for running helper scripts.

Options:
  --help  Show this message and exit.
```
