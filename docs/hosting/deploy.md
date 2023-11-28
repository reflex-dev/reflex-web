```python exec
import reflex as rx
```

# Reflex Hosting Service

```md alert info
# Hosting is in Alpha
Please reach out to us on Discord if you have an app ready to deploy and we will give you an invitation code.
```

So far, we've been running our apps locally on our own machines.
But what if we want to share our apps with the world?  This is where
deployment comes in.

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring your infrastructure.

(This tutorial assumes you’ve successfully `reflex init` and `reflex run` your app)

### Authentication

First, create or log in to your account using the following command. (Requires Reflex > v0.3.1)

```bash
reflex login
```

You will be prompted to your browser where you can create an account using Github or Gmail for authentication.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.alert_description("You will need an invitation code! Contact us on Discord if you have an app ready to deploy, and we will give you a code."
    ),
    status="info",
    width="100%",
    margin_bottom="1rem",
)
```

### Deployment

Once you have successfully logged in to your account, you can deploy your apps.

TODO: style the sentence below.
Make sure you include a requirements.txt with all your dependencies!

Navigate to the project you want to deploy and type the following command:

```bash
reflex deploy
```

**Name**: choose a name that will be the start of your url, i.e. `<your-app-name>.reflex.run`. The name should only contain domain name safe characters, so no slashes, no underscores. It is also case insensitive, use all lower cases.

**Regions**: check the list of regions you can select from [reflex deployments regions](https://www.notion.so/reflex-deployments-regions-a066211142b945a8bc86697326994dbd?pvs=21)

That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

Once your app is deployed, you will see a URL with your live site.

Please follow the hosting guide here to deploy your app **(invitation code needed)**: [Reflex Hosting](https://reflex-dev.notion.site/Reflex-Hosting-Documentation-57a4dd55d6234858bbae0be75be79ce7?pvs=4)
