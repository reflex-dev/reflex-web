# Environment Variables (Secrets)

```python exec
import reflex as rx
```

It is possible to add environment variables to your app. This is useful for storing secrets such as API keys, and other sensitive information.

## Adding Environment Variables

You can add environment variables to your app by clicking the `Secrets` button at the bottom of the chat input box, as seen below:

```python eval
rx.image(
    src="/ai_builder/secrets_and_custom_packages.gif",
    height="auto",
    padding_bottom="2rem",
)
```

After you add the environment variables the AI now has context of these and you can prompt it to use them in your code.

You can also add environment variables after your app is built, by again clicking the `Secrets` button at the bottom of the chat input box on the generation page.