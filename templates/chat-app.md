---
title: Chat App
description: "Real-time chat application with multiple rooms using Reflex and ChatGPT"
author: "Reflex"
image: "chat-app.webp"
demo: "https://chat.reflex.run/"
source: "https://github.com/reflex-dev/reflex-chat"
meta: [
    {"name": "keywords", "content": ""},
]
template: "chat"
---
# Chat App

The following is a python chat app. It is 100% Python-based, including the UI, all using Reflex. Easily create and delete chat sessions. The application is fully customizable and no knowledge of web dev is required to use it and it has responsive design for various devices.

## Usage

To run this app locally, install Reflex and run:

```bash
git clone https://github.com/reflex-dev/reflex-chat.git
```

```bash
cd reflex-chat
```

Set up your OpenAI API key:
```bash
export OPEN_AI_KEY=your-openai-api-key
```

Install the dependencies and run the app:

```bash
pip install -r requirements.txt
```

```bash
reflex run
```

## Customizing the Inference

You can customize the app by modifying the `chat/state.py` file replacing `model = self.openai_process_question` with that of other LLM providers and writing your own process question function.
