---
from datetime import datetime
---

Write normal *markdown code* while using Python expressions: This blog post was written on {datetime.now()}.


## Embed Reflex Components

```reflex
rx.alert(
    rx.alert_icon(),
    rx.alert_title(
        rx.markdown(
            "You can embed Reflex components in your blog posts!"
        ),
    ),
    status="success",
)
```
