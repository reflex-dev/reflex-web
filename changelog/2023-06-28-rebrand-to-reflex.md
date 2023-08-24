---
author: Nikhil Rao
date: 2023-06-28
title: "Pynecone is now Reflex"
description: "We have some exciting news to share about the next stage of our company!"
image: reflex_banner.png
---

We have some exciting news to share about the next stage of our company!

### Pynecone is rebranding to Reflex.

This name aligns with our goal of creating a web framework easy and intuitive, while remaining flexible and powerful to support any app.

We will continue to grow Reflex as an open source project to include all the features of web development. We're also working on our hosting service that will be available later this year.

### Key Changes

```reflex
rx.unordered_list(
    rx.list_item("Our main website will change from ", doclink("https://pynecone.io", href="https://pynecone.io"), " to ", doclink("https://reflex.dev", href="https://reflex.dev"), "."),
    rx.list_item("Our Python package will change from ", rx.code("pip install pynecone"), " to ", rx.code("pip install reflex"), "."),
    rx.list_item("Our library will change from ", rx.code("import pynecone as pc"), " to ", rx.code("import reflex as rx"), "."),
    rx.list_item("Our Github repo will switch from ", doclink("https://github.com/pynecone-io/pynecone", href="https://github.com/pynecone-io/pynecone"), " to ", doclink("https://github.com/reflex-dev/reflex", href="https://github.com/reflex-dev/reflex"), "."),
    spacing="0em"
)
```

### Migrating Existing Projects

```reflex
doctext("If you have an existing Pynecone project, run ", rx.code("reflex init"), " from a directory that has a ", rx.code("pcconfig.py"), " file, you will have the option to migrate your project.")
```

### Next Steps

```reflex
doctext("If you have any issues through the migration, please come join our ", doclink("Discord", href=constants.DISCORD_URL), ". We will post the latest news there as well as on our ", doclink("Twitter", href=constants.TWITTER_URL), ".")
```

Thanks for supporting us through this change. We're excited to start this new chapter and see what the community builds with Reflex!

```reflex
rx.box("", height="8em")
```
