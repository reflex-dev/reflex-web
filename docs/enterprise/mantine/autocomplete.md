---
title: Autocomplete
---

# Autocomplete

`rxe.mantine.autocomplete` - Input with suggestions dropdown for enhanced user experience.

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def basic_autocomplete():
    return rxe.mantine.autocomplete(
        data=["Apple", "Banana", "Cherry", "Date"],
        placeholder="Type a fruit",
    )
```

## With Value

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def valued_autocomplete():
    return rxe.mantine.autocomplete(
        data=["Python", "JavaScript", "TypeScript", "Java"],
        value="Python",
        placeholder="Pre-filled value",
    )
```

## With Limit

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def limited_autocomplete():
    return rxe.mantine.autocomplete(
        data=["Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust"],
        limit=3,
        placeholder="Max 3 suggestions",
    )
```

## Dynamic Data

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def dynamic_autocomplete():
    return rxe.mantine.autocomplete(
        data=["React", "Vue", "Angular", "Svelte", "Next.js", "Nuxt.js"],
        placeholder="Search frameworks",
    )
```

## With Error State

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def error_state_autocomplete():
    return rxe.mantine.autocomplete(
        data=["JavaScript", "TypeScript", "Python", "Java"],
        error="Example validation error",
        placeholder="Shows error state",
    )
```

## Loading State

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def loading_autocomplete():
    return rxe.mantine.autocomplete(
        data=["United States", "United Kingdom", "Canada", "Australia"],
        loading=True,
        placeholder="Loading suggestions...",
    )
```


## Disabled

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def disabled_autocomplete():
    return rxe.mantine.autocomplete(
        data=["Option 1", "Option 2", "Option 3"],
        disabled=True,
        placeholder="Disabled autocomplete",
    )
```

## Styled

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def styled_autocomplete():
    return rxe.mantine.autocomplete(
        data=["React", "Vue", "Angular", "Svelte"],
        label="Framework",
        description="Choose your preferred framework",
        placeholder="Type to search",
        size="lg",
        radius="xl",
    )
```

## API Reference

### Props

| Prop | Type | Description |
|------|------|-------------|
| `data` | `list[str]` | Suggestions to display |
| `value` | `str` | Current input value |
| `placeholder` | `str` | Placeholder text |
| `limit` | `int` | Max suggestions to show |
| `loading` | `bool` | Show loading state |
| `disabled` | `bool` | Disable the input |
| `error` | `str` | Error message to display |
| `label` | `str` | Label text |
| `description` | `str` | Description text |
| `size` | `str` | Input size (`xs`, `sm`, `md`, `lg`, `xl`) |
| `radius` | `str` | Border radius (`xs`, `sm`, `md`, `lg`, `xl`) |

## Troubleshooting

### Common Issues

**No suggestions appearing:**
- Verify `data` prop contains valid strings
- Check if `limit` prop is set too low
- Ensure data is not empty

**Performance with large datasets:**
- Use `limit` prop to restrict visible suggestions
- Implement async loading for better UX
- Consider server-side filtering for very large datasets

**Styling issues:**
- Use `size` and `radius` props for consistent styling
- Check that `label` and `description` props are properly set
- Verify error styling with `error` prop
