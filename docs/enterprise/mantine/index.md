---
title: Mantine
order: 4
---

# Mantine

Mantine is a React component library that provides a set of high-quality components and hooks for building modern web applications. It is designed to be flexible, customizable, and easy to use, making it a popular choice among developers.

Some of those components have been integrated into Reflex Enterprise, allowing you to use them in your Reflex applications. The following components are available with enhanced documentation and examples:

## Input Components
- **[JsonInput](/docs/enterprise/mantine/json-input)** - Input and validate JSON data with real-time feedback
- **[Autocomplete](/docs/enterprise/mantine/autocomplete)** - Provide suggestions as users type with async data support
- **[ComboBox](/docs/enterprise/mantine/combobox)** - Flexible dropdown interface with searchable options
- **[Multiselect](/docs/enterprise/mantine/multi-select)** - Select multiple options with validation and limits
- **[TagsInput](/docs/enterprise/mantine/tags-input)** - Add and manage tags with validation and suggestions

## Display Components
- **[Tree](/docs/enterprise/mantine/tree)** - Display hierarchical data with interactive expand/collapse
- **[LoadingOverlay](/docs/enterprise/mantine/loading-overlay)** - Show loading states during async operations
- **[Spoiler](/docs/enterprise/mantine/spoiler)** - Hide/reveal content with customizable triggers
- **[Timeline](/docs/enterprise/mantine/timeline)** - Display chronological events and processes

## Progress & Feedback
- **RingProgress** - Circular progress indicators
- **SemiCircleProgress** - Semi-circular progress displays
- **NumberFormatter** - Format and display numbers with localization

## Layout & Structure
- **Pill** - Display tags and labels
- **PillsInput** - Input component for pill-style tags
- **Collapse** - Collapsible content sections

## When to Use Each Component

### For Data Input
- Use **JsonInput** when you need users to input structured JSON data
- Use **Autocomplete** for single selections with search functionality
- Use **ComboBox** for custom dropdown interfaces with complex options
- Use **Multiselect** when users need to choose multiple items from a list
- Use **TagsInput** for free-form tag entry with validation

### For Data Display
- Use **Tree** for hierarchical data like file systems or organizational structures
- Use **Timeline** for chronological events or process steps
- Use **Spoiler** to hide detailed content that users can reveal on demand

### For User Feedback
- Use **LoadingOverlay** during async operations to prevent user interaction
- Use progress components to show completion status of long-running tasks

## Common Patterns

### State Management
All Mantine components work best with proper Reflex state management:

```python
class MyState(rx.State):
    selected_value: str = ""
    
    @rx.event
    def handle_change(self, value: str):
        self.selected_value = value
```

### Validation
Most input components support validation patterns:

```python
@rx.event
def validate_input(self, value):
    if not value:
        self.error_message = "This field is required"
    else:
        self.error_message = ""
```

### Form Integration
Components integrate seamlessly with Reflex forms:

```python
rx.form(
    rxe.mantine.json_input(
        value=MyState.json_data,
        on_change=MyState.setvar("json_data"),
        error=MyState.form_errors.get("json", ""),
    ),
    on_submit=MyState.submit_form,
)
```

## Troubleshooting

### Common Issues Across Components

**Props not working as expected**
- Remember to use snake_case for all props (e.g., `max_length` instead of `maxLength`)

**State not updating**
- Ensure you're using proper event handlers with `on_change` or similar events
- Check that your state variables are properly typed

**Styling issues**
- Most components accept standard Reflex styling props
- Use component-specific props for advanced styling options

**Performance with large datasets**
- Implement pagination or virtualization for components handling large amounts of data
- Use debouncing for search functionality

For component-specific troubleshooting, refer to the individual component documentation pages.

