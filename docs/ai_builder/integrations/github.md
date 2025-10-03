---
tags: DevTools
description: Integrate with GitHub to automate workflows and interact with your code repositories.
---

# Connecting to Github

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

The Github integration is important to make sure that you don't lose your progress. It also allows you to revert to previous versions of your app.


```python eval
rx.image(
    src="/ai_builder/connecting_to_github.gif",
    height="auto",
    padding_bottom="2rem",
)
```

The GitHub integration allows you to:

- Save your app progress
- Work on your code locally and push your local changes back to Reflex.Build


## Github Commit History

The commit history is a great way to see the changes that you have made to your app. You can also revert to previous versions of your app from here.

```python eval
image_zoom(rx.image(src="/ai_builder/github_commit_history.png"))
```
