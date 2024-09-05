---
author: Nikhil Rao
date: 2023-06-28
title: Pynecone is now Reflex
description: We have some exciting news to share about the next stage of our company!
image: /reflex_banner.png
meta: [
    {"name": "keywords", "content": ""},
]
---

```python exec
from pcweb import constants
import reflex as rx
```

We have some exciting news to share about the next stage of our company!

### Pynecone is rebranding to Reflex.

This name aligns with our goal of creating a web framework easy and intuitive, while remaining flexible and powerful to support any app.

We will continue to grow Reflex as an open source project to include all the features of web development. We're also working on our hosting service that will be available later this year.

### Key Changes

* Our main website will change from [{constants.PYNECONE_URL}]({constants.PYNECONE_URL}) to [{constants.REFLEX_URL}]({constants.REFLEX_URL}).
* Our Python package will change from `pip install pynecone` to `pip install reflex`.
* Our library will change `import pynecone as pc` to `import reflex as rx`.
* Our Github repo will switch from [{constants.OLD_GITHUB_URL}]({constants.OLD_GITHUB_URL}) to [{constants.GITHUB_URL}]({constants.GITHUB_URL}).

### Migrating Existing Projects

If you have an existing Pynecone project, run `reflex init` from a directory that has a `pcconfig.py` file, you will have the option to migrate your project.

### Next Steps

If you have any issues through the migration, please come join our [Discord]({constants.DISCORD_URL}).
We will post the latest news there as well as on our [Twitter]({constants.TWITTER_URL}).

Thanks for supporting us through this change. We're excited to start this new chapter and see what the community builds with Reflex!