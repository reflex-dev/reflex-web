```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```


# Tokens

A token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the `--token` flag. A good use case would be for GitHub actions (you store this token in the secrets).

Tokens are found on the Project List page under the tab `Tokens`. If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below.

```python eval
image_zoom(rx.image(src="/hosting_tokens.png", alt="Adding tokens to Reflex Cloud"))
```
