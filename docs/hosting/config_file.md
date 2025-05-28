```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import hosting
from pcweb.pages import docs
from pcweb.styles.styles import get_code_style, cell_style
```

## What is reflex cloud config?

The following command:

```bash
reflex cloud config
```

generates a `cloud.yml` configuration file used to deploy your Reflex app to the Reflex cloud platform. This file tells Reflex how and where to run your app in the cloud.

## Configuration File Structure

The `cloud.yml` file uses YAML format and supports the following structure. **All fields are optional** and will use sensible defaults if not specified:

```yaml
# Basic deployment settings
name: my-app-prod                    # Optional: defaults to project folder name
description: 'Production deployment' # Optional: empty by default
project: my-client-project          # Optional: for organization

# Infrastructure settings
regions:                            # Optional: defaults to sjc: 1
  sjc: 1                           # San Jose (primary)
  lhr: 2                           # London (secondary)
vmtype: c2m2                       # Optional: defaults to c1m1

# Custom domain and environment
hostname: myapp.com                 # Optional: null uses default Reflex URL
envfile: .env.production           # Optional: defaults to .env

# Additional dependencies
packages:                          # Optional: empty by default
  - procps
  - imagemagick
```

## Configuration Options Reference

```python demo-only
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell(rx.text("Option", size="1", weight="bold", color=rx.color("slate", 11))),
            rx.table.column_header_cell(rx.text("Type", size="1", weight="bold", color=rx.color("slate", 11))),
            rx.table.column_header_cell(rx.text("Default", size="1", weight="bold", color=rx.color("slate", 11))),
            rx.table.column_header_cell(rx.text("Description", size="1", weight="bold", color=rx.color("slate", 11))),
            align="center"
        )
    ),
    rx.table.body(*[
        rx.table.row(
            rx.table.cell(rx.text(option, class_name="text-sm")),
            rx.table.cell(rx.text(type_, class_name="text-sm")),
            rx.table.cell(rx.text(default, class_name="text-sm")),
            rx.table.cell(rx.link(description, href=link, class_name="text-sm") if link else rx.text(description, size="1", weight="regular")),
            align="center"
        ) for option, type_, default, description, link in [
            ("name", "string", "folder name", "Deployment identifier in dashboard", None),
            ("description", "string", "empty", "Human-readable deployment description", None),
            ("regions", "object", "sjc: 1", "Region deployment mapping", "/docs/hosting/regions"),
            ("vmtype", "string", "c1m1", "Virtual machine specifications", "/docs/hosting/machine-types"),
            ("hostname", "string", "null", "Custom domain configuration", "/docs/hosting/custom-domains"),
            ("envfile", "string", ".env", "Environment variables file path", "/docs/hosting/secrets-environment-vars"),
            ("project", "string", "null", "Project organization", None),
            ("packages", "array", "empty", "Additional system packages", None),
        ]
    ]),
    variant="ghost",
    size="2",
    width="100%",
    max_width="800px",
)
```

## Detailed Configuration Options

### Regions

Available deployment regions with their codes:

- `sjc`: San Jose, California (US West)
- `lhr`: London, United Kingdom (Europe)
- `fra`: Frankfurt, Germany (Europe)
- `syd`: Sydney, Australia (Asia-Pacific)

Specify regions using the format `region: instance_count`:

```yaml
regions:
  sjc: 1    # Primary region with 1 instance
  lhr: 2    # Backup region with 2 instances for high availability
```

**Use Cases:**
- Single region: Cost-effective for regional applications
- Multi-region: Global applications requiring low latency and redundancy

### VM Types

Choose the appropriate virtual machine size based on your application needs:

### Custom Domains

Set `hostname` to use your own domain instead of the default Reflex Cloud URL:

```yaml
hostname: myapp.com
```

**Requirements:**
- Domain ownership verification
- DNS configuration (CNAME or A record)
- SSL certificate (handled automatically)

### Environment Variables

Specify the path to your environment variables file:

```yaml
envfile: .env.production  # Custom environment file
```

Example `.env` file structure:

```bash

DATABASE_URL=postgresql://user:pass@host:port/dbname

OPENAI_API_KEY=your_api_key_here
STRIPE_SECRET_KEY=sk_live_...

DEBUG=False
SECRET_KEY=your_secret_key_here
```

### Projects

Organize deployments using projects:

```yaml
project: client-alpha    # Groups related deployments
```

Projects help separate:
- Different clients or customers
- Development, staging, and production environments
- Team-based application ownership

### Packages

Install additional system packages your application requires:

```yaml
packages:
  - procps      # Process monitoring tools
  - imagemagick # Image processing
  - ffmpeg      # Media processing
```

## Multiple Configuration Examples

### Minimal Configuration
```yaml
# Uses all defaults - suitable for development
name: my-app-dev
```

### Production Configuration
```yaml
name: myapp-production
description: 'Main production deployment'
regions:
  sjc: 2
  lhr: 1
vmtype: c4m4
hostname: myapp.com
envfile: .env.production
project: myapp
packages:
  - imagemagick
  - redis-tools
```

### Multi-Environment Setup

**Development (`cloud-dev.yml`):**
```yaml
name: myapp-dev
description: 'Development environment'
vmtype: c1m1
envfile: .env.development
```

**Staging (`cloud-staging.yml`):**
```yaml
name: myapp-staging
description: 'Staging environment'
regions:
  sjc: 1
vmtype: c2m2
envfile: .env.staging
```

**Production (`cloud-prod.yml`):**
```yaml
name: myapp-production
description: 'Production environment'
regions:
  sjc: 2
  lhr: 1
vmtype: c4m4
hostname: myapp.com
envfile: .env.production
```

## Using Different Configuration Files

Deploy with specific configuration files:

```bash
# Use default cloud.yml
reflex deploy

# Use specific configuration file
reflex deploy --config cloud-prod.yml
reflex deploy --config cloud-staging.yml
```

## Deployment Workflow

1. **Generate base configuration:**
   ```bash
   reflex cloud config
   ```

2. **Customize the `cloud.yml` file** based on your requirements using the options above

3. **Create environment file** (if needed):
   ```bash
   touch .env
   # Add your environment variables
   ```

4. **Deploy your application:**
   ```bash
   reflex deploy
   ```

5. **Monitor deployment** through the (Reflex Cloud)[https://cloud.reflex.dev/] dashboard

## Summary

The `cloud.yml` configuration provides complete control over your Reflex Cloud deployments while maintaining simplicity. All configuration options are optional, allowing you to start with minimal setup and gradually add complexity as your application scales.

Key takeaways:
- Start with basic configuration and expand as needed
- Use multiple configuration files for different environments
- Leverage regions for global availability and redundancy
- Secure environment variables and never commit them to version control
