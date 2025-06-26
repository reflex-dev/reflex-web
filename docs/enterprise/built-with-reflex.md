---
order: 1
---

```python exec
from pcweb.pages import docs
```

# Build with Reflex Badge

The option `show_built_with_reflex` allows you to toggle the "Built with Reflex" badge. This badge is displayed on the bottom right corner of the frontend.

By default, the badge will always be displayed. To hide it, set `show_built_with_reflex` to `False`.

## Tier Requirements

- If you are deploying on Reflex Cloud, you need to be on the Pro tier. 
- If you are self-hosting, you need to be on the Team tier.

## Example of Configuration File

```python
import reflex_enterprise as rxe

config = rxe.Config(
    name="my_app",
    show_built_with_reflex=False,
)
```

[Home Page](/)
