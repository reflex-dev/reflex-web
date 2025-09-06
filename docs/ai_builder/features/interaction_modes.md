# Interaction Modes

Reflex Build gives you two ways to interact with the AI while creating your application: **Agent mode** and **Chat mode**.
You can switch between these modes from the dropdown at the bottom of the workspace.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom

def interaction_mode_image():
    return rx.el.div(
        image_zoom(
            rx.image(
                src=rx.color_mode_cond(
                    "/ai_builder/features/interaction_modes_light.png",
                    "/ai_builder/features/interaction_modes_dark.png",
                ),
                class_name="p-2 rounded-md h-auto",
                border=f"0.81px solid {rx.color('slate', 5)}",
            ),
            class_name="rounded-md overflow-hidden",
        ),
        class_name="w-full flex flex-col rounded-md cursor-pointer",
    )
```

```python eval

rx.el.div(interaction_mode_image())

```

## Agent Mode

In **Agent mode**, the AI acts as a proactive builder:

- **Plans ahead**: It breaks down your request into steps and explains its approach before making changes.
- **Applies changes directly**: Generates and edits files in your project automatically.
- **Optimized for workflows**: Best for building features, scaffolding components, or setting up integrations.

Use Agent mode when you want the AI to **take initiative** and help build out your app.


## Chat Mode

In **Chat mode**, the AI behaves more like a traditional conversational assistant:

- **Answers questions**: Provides explanations, references, and guidance without editing code.
- **Lightweight**: Great for quick clarifications, debugging help, or brainstorming ideas.
- **Safer experimentation**: No automatic file changes — you stay in full control.

Use Chat mode when you want to **ask questions** or get **advice without altering your codebase**.


## When to Use Each

- **Build a new feature or component** → Use **Agent**
- **Set up integrations (DB, etc.)** → Use **Agent**
- **Understand Reflex concepts** → Use **Chat**
- **Debug an error in your code** → Start with **Chat**, then switch to **Agent**
- **Explore ideas or best practices** → Use **Chat**


## Switching Modes

1. Look for the **mode selector** at the bottom of the workspace.
2. Choose **Agent** or **Chat** depending on your current task.
3. You can switch modes at any time without losing context.


## Best Practices

- **Start in Chat** to clarify your goal → **switch to Agent** to implement.
- Review the AI’s suggested changes before committing.
- If Agent output feels too heavy, fall back to Chat for lighter interaction.
