# Built with Reflex Badge

The "Built with Reflex" badge appears in the bottom right corner of apps using reflex-enterprise components.

## Removing the Badge

To remove the badge, you need a paid tier:
- **Cloud**: Pro tier or higher
- **Self-hosted**: Team tier or higher

## Configuration

```python
import reflex_enterprise as rxe

config = rxe.Config(
    show_built_with_reflex=False,  # Requires paid tier
)
```