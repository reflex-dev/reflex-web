# Configuration

Reflex apps can be configured using a configuration file, environment variables, and command line arguments.

## Configuration File

Running `reflex init` will create an `rxconfig.py` file in your root directory.
You can pass keyword arguments to the `Config` class to configure your app.

For example:

```python
# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="my_app_name",
    # Connect to your own database.
    db_url="postgresql://user:password@localhost:5432/my_db",
    # Change the frontend port.
    frontend_port=3001,
)
```


## Configuration Options

### app_name
**Type:** `str` (required)
**Description:** The name of your app. This should match the name of your app directory.

```python
config = rx.Config(app_name="my_awesome_app")
```

### app_module_import
**Type:** `str | None` (default: `None`)
**Description:** The path to the app module if different from the default.

### loglevel
**Type:** `LogLevel` (default: `LogLevel.DEFAULT`)
**Description:** The log level to use for the application.

```python
import reflex as rx
config = rx.Config(
    app_name="myapp",
    loglevel=rx.constants.LogLevel.DEBUG
)
```

## Server Configuration

### frontend_port
**Type:** `int | None` (default: `None`)
**Description:** The port to run the frontend on. In dev mode, the next available port will be used if this is taken.

```python
config = rx.Config(
    app_name="myapp",
    frontend_port=3001
)
```

### frontend_path
**Type:** `str` (default: `""`)
**Description:** The path to run the frontend on. For example, `"/app"` will run the frontend on `http://localhost:3000/app`.

### backend_port
**Type:** `int | None` (default: `None`)
**Description:** The port to run the backend on. In dev mode, the next available port will be used if this is taken.

### backend_host
**Type:** `str` (default: `"0.0.0.0"`)
**Description:** The host the backend will be hosted on.

### api_url
**Type:** `str` (default: auto-generated)
**Description:** The backend URL the frontend will connect to. This must be updated if the backend is hosted elsewhere or in production.

### deploy_url
**Type:** `str | None` (default: auto-generated)
**Description:** The URL the frontend will be hosted on.

## Database Configuration

### db_url
**Type:** `str | None` (default: `"sqlite:///reflex.db"`)
**Description:** The database URL used by `rx.Model`. Supports SQLite, PostgreSQL, and other SQL databases.

```python
# SQLite (default)
config = rx.Config(
    app_name="myapp",
    db_url="sqlite:///reflex.db"
)

# PostgreSQL
config = rx.Config(
    app_name="myapp",
    db_url="postgresql://user:password@localhost:5432/mydatabase"
)
```

### async_db_url
**Type:** `str | None` (default: `None`)
**Description:** The async database URL used by `rx.Model` for asynchronous database operations.

## Redis Configuration

### redis_url
**Type:** `str | None` (default: `None`)
**Description:** The Redis URL for caching and session management.

```python
config = rx.Config(
    app_name="myapp",
    redis_url="redis://localhost:6379"
)
```

## State Management

### state_manager_mode
**Type:** `StateManagerMode` (default: `StateManagerMode.DISK`)
**Description:** Indicates which type of state manager to use.

### redis_lock_expiration
**Type:** `int` (default: from constants)
**Description:** Maximum expiration lock time for Redis state manager.

### redis_lock_warning_threshold
**Type:** `int` (default: from constants)
**Description:** Maximum lock time before warning for Redis state manager.

### redis_token_expiration
**Type:** `int` (default: from constants)
**Description:** Token expiration time for Redis state manager.

## Frontend Configuration

### frontend_packages
**Type:** `list[str]` (default: `[]`)
**Description:** Additional frontend packages to install.

```python
config = rx.Config(
    app_name="myapp",
    frontend_packages=["react-icons", "framer-motion"]
)
```

### react_strict_mode
**Type:** `bool` (default: `True`)
**Description:** Whether to use React strict mode.

### cors_allowed_origins
**Type:** `Sequence[str]` (default: `("*",)`)
**Description:** List of origins that are allowed to connect to the backend API.

```python
config = rx.Config(
    app_name="myapp",
    cors_allowed_origins=["http://localhost:3000", "https://mydomain.com"]
)
```

## Build Configuration

### bun_path
**Type:** `ExistingPath` (default: from constants)
**Description:** The path to the Bun executable.

### static_page_generation_timeout
**Type:** `int` (default: `60`)
**Description:** Timeout in seconds for production build of frontend pages.

### Monitoring & Debugging

### telemetry_enabled
**Type:** `bool` (default: `True`)
**Description:** Whether to enable telemetry collection.

### enable_pyleak_monitoring
**Type:** `bool` (default: `False`)
**Description:** Enable PyLeak monitoring for detecting event loop blocking and resource leaks.

### pyleak_blocking_threshold
**Type:** `float` (default: `0.1`)
**Description:** Threshold in seconds for detecting event loop blocking operations.

### pyleak_thread_grace_period
**Type:** `float` (default: `0.2`)
**Description:** Grace period in seconds for thread leak detection cleanup.

## Environment Configuration

### env_file
**Type:** `str | None` (default: `None`)
**Description:** Path to file containing key-value pairs to override in the environment (dotenv format).

```python
config = rx.Config(
    app_name="myapp",
    env_file=".env.local"
)
```

## State & Behavior Settings

### state_auto_setters
**Type:** `bool` (default: `True`)
**Description:** Whether to automatically create setters for state base vars.

### show_built_with_reflex
**Type:** `bool | None` (default: `None`)
**Description:** Whether to display the sticky "Built with Reflex" badge on all pages.

### is_reflex_cloud
**Type:** `bool` (default: `False`)
**Description:** Whether the app is running in the Reflex Cloud environment.

## Plugin Configuration

### plugins
**Type:** `list[Plugin]` (default: `[]`)
**Description:** List of plugins to use in the app.

```python
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="myapp",
    plugins=[SitemapPlugin()]
)
```

### disable_plugins
**Type:** `list[str]` (default: `[]`)
**Description:** List of fully qualified import paths of plugins to disable.

```python
config = rx.Config(
    app_name="myapp",
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]
)
```

## extra_overlay_function
**Type:** `str | None` (default: `None`)
**Description:** Extra overlay function to run after the app is built.

## Database Helper Classes

### DBConfig

Reflex provides helper classes for database configuration:

```python
import reflex as rx

# PostgreSQL
db_config = rx.DBConfig.postgresql(
    database="mydb",
    username="user",
    password="password",
    host="localhost",
    port=5432
)

config = rx.Config(
    app_name="myapp",
    db_url=db_config.get_url()
)

# SQLite
db_config = rx.DBConfig.sqlite(database="myapp.db")
config = rx.Config(
    app_name="myapp",
    db_url=db_config.get_url()
)
```

## Environment Variables

You can override any configuration value by setting environment variables with the `REFLEX_` prefix and the parameter name in uppercase.

For example:

```bash
# Override frontend_port
REFLEX_FRONTEND_PORT=3001 reflex run

# Override database URL
REFLEX_DB_URL="postgresql://user:pass@localhost/db" reflex run

# Override log level
REFLEX_LOGLEVEL=debug reflex run

```

## Command Line Arguments

You can also override configuration values using command line arguments:

```bash
reflex run --frontend-port 3001 --backend-port 8001
```

## Customizable App Data Directory

The `REFLEX_DIR` environment variable can be set to specify where Reflex writes helper tools like Bun and NodeJS.

By default, platform-specific directories are used:

- **Windows:** `C:/Users/<username>/AppData/Local/reflex`
- **macOS:** `~/Library/Application Support/reflex`
- **Linux:** `~/.local/share/reflex`

```bash
export REFLEX_DIR="/custom/path/to/reflex"
reflex run
```

## Complete Configuration Example

Here's a comprehensive example showing various configuration options:

```python
# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="my_production_app",

    # Server configuration
    frontend_port=3000,
    backend_port=8000,
    frontend_path="/app",

    # Database
    db_url="postgresql://user:password@localhost:5432/myapp",

    # Redis for caching
    redis_url="redis://localhost:6379",

    # Frontend packages
    frontend_packages=["react-icons", "framer-motion"],

    # CORS settings
    cors_allowed_origins=["https://mydomain.com", "https://www.mydomain.com"],

    # Environment
    env_file=".env.production",

    # Disable telemetry
    telemetry_enabled=False,

    # Hide Reflex badge
    show_built_with_reflex=False,

    # Enable monitoring
    enable_pyleak_monitoring=True,
    pyleak_blocking_threshold=0.05,
)
```

This configuration system provides flexible ways to customize your Reflex application for different environments and use cases.
