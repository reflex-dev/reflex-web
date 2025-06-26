---
order: 2
---

```python exec
from pcweb.pages import docs
```

# Single port proxy

> Available starting from Team tier.

By using the config option `use_single_port` you can configure your backend to proxy any request it received and cannot handle to the frontend. This results in a single port deployment, where the frontend and backend are both served on the same port.

## Tier Requirements

In order to use this feature, you need to be on the Team tier.

- Cloud deployment:
    - The cloud platform does not support this feature, so it will be ignored even if provided.
- Self-hosted deployment:
    - You need to be on the Team tier.

## Example of Configuration File

```python
import reflex_enterprise as rxe

config = rxe.Config(
    app_name="my_single_port_app",
    use_single_port=True,
)
```

By defining the `use_single_port` option to `True`, both frontend and backend will be available on `backend_port`.

[Home Page](/{docs.index.route})
