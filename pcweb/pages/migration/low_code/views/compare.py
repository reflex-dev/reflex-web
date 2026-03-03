from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "Architecture and state management.",
        "icon": "SquareArrowExpand02Icon",
        "description": 'Streamlit uses a "script rerun" model where every widget change re-executes the entire Python script from top to bottom. Dash uses a callback-based architecture that becomes "callback spaghetti" as apps grow. Gradio is designed specifically for ML model demos. Reflex takes a declarative, state-driven approach where you define state classes and UI components in Python, and changes propagate reactively via WebSockets. Only affected components re-render.',
        "pros": [
            "Your app only updates the parts that changed — no unnecessary reruns, so it stays fast even with large data",
            "User sessions remember where they are — multi-step workflows, background tasks, and real-time updates all work without extra effort",
            "The event-driven model keeps your code clean and organized, even as your app gets more complex",
        ],
        "cons": [
            "Streamlit reruns your entire script every time a user clicks anything, leading to memory leaks and slowdowns that make it unreliable for long-term use",
            "Dash works fine for small apps, but as they grow the logic gets spread across many separate callback functions with no native support for object-oriented state, making it hard to follow and maintain",
            "Gradio is built for ML model demos — it's not a general-purpose app framework",
        ],
    },
    {
        "title": "Real-time and interactivity.",
        "icon": "ZapIcon",
        "description": "Streamlit has no server push — real-time or background updates need client polling or workarounds. Dash has no native server-push feature. Gradio's interactivity is limited to input-output pairs for ML model inference. Reflex uses automatic WebSocket sync where state changes on the server instantly propagate to the browser.",
        "pros": [
            "Changes on the server show up instantly in the browser — no refresh needed, no extra setup",
            "Live dashboards, real-time data feeds, and collaborative features just work out of the box",
            "Fully event-based — your app can react to specific user actions like edits, clicks, and selections as they happen",
        ],
        "cons": [
            "Streamlit can't push updates to the user — nothing happens in the browser until the user clicks something to trigger a full script rerun",
            "Dash has no built-in way to push live updates — getting real-time data requires workarounds like constant polling or adding custom extensions",
            "Gradio only handles simple input-in, output-out interactions for ML models — it's not built for apps that need to respond to complex user actions",
        ],
    },
    {
        "title": "Code structure and maintainability.",
        "icon": "SourceCodeSquareIcon",
        "description": "Real Reflex projects cut approximately 50% of the code compared to equivalent Dash apps. Reflex's Python class-based state model keeps code organized. In Dash, the callback model fragments logic across scattered decorator functions. In Streamlit, the linear script model breaks down when you need complex page flows or shared state across views.",
        "pros": [
            "Clean Python class structure keeps your code organized and easy to follow, even as apps grow to multiple pages and features",
            "Real projects with complexity use roughly half the code compared to the same app built in Dash",
            "Teams that tried other Python frameworks found Reflex significantly cleaner to maintain and extend",
        ],
        "cons": [
            "Dash scatters your logic across many separate callback functions that become harder to trace as the app grows",
            "Streamlit's simple script approach works at first but falls apart when you need complex page flows or shared state across views",
            "Gradio's simple interface definitions can't support complex multi-page app structures",
        ],
    },
    {
        "title": "Customization and UI components.",
        "icon": "WebDesign01Icon",
        "description": "Streamlit has a customization ceiling — deep CSS or HTML tweaks are difficult, and building truly bespoke widgets requires writing a Streamlit Component in React and TypeScript. Dash has a robust set of components but custom ones still require React. Gradio's customization is similarly limited. Reflex lets you wrap any React component directly from Python with fine-grained CSS control.",
        "pros": [
            "No limits on what you can build — use any React component in pure Python with full control over styling and layout",
            "Complete design flexibility without ever leaving the Python ecosystem",
        ],
        "cons": [
            "Most low-code Python frameworks offer very basic layout and styling options with little flexibility",
            "Lack of customization is one of the most commonly cited frustrations across low-code Python tools — building anything beyond the default look typically requires dropping into React, TypeScript, or JavaScript",
        ],
    },
    {
        "title": "Built-in functionality.",
        "icon": "Settings01Icon",
        "description": "Streamlit and Dash both lack built-in essentials for production apps — no auth, background tasks, or ORM. Gradio is focused narrowly on ML model demos. Reflex ships with ORM, database migrations, background jobs, file uploads, and role-based auth out of the box.",
        "pros": [
            "Authentication, database management, background jobs, file uploads, and role-based access all come built in",
            "Everything you need to go from prototype to production without stitching together a patchwork of separate tools",
            "SSO and user management are included — no third-party libraries or workarounds needed",
        ],
        "cons": [
            "Streamlit has no built-in auth, database access, or background processing — even simple things like a loading button require workarounds",
            "The Dash open-source package has no auth, no background tasks, and no database layer — each one needs a separate library",
            "Gradio is focused narrowly on ML demos and lacks general-purpose app features entirely",
        ],
    },
    {
        "title": "Deployment and the prototype-to-production gap.",
        "icon": "UserSwitchIcon",
        "description": "Low-code Python frameworks are good for getting a first version up quickly, but not designed to take apps to production. Streamlit apps hit out-of-memory errors under load. Open-source Dash runs on Flask and requires manual infrastructure setup. Gradio struggles to scale for production. Reflex compiles to a FastAPI backend with a React frontend — production-ready and container-friendly from day one.",
        "pros": [
            "Compiles to a FastAPI backend with a React frontend on an async web server — production-ready and container-friendly from the start",
            "Fits into Git, pull requests, automated testing, and CI/CD from day one — no separate production rewrite needed",
            "What you build is what you ship — you're in production without having to rebuild",
        ],
        "cons": [
            "All low-code tools are seen as prototyping tools — teams build a first version, then have to rebuild the real thing from scratch when it's time to ship to production",
            "Streamlit apps hit out-of-memory errors under load with even moderately large datasets, and its rerun model fundamentally limits production scalability",
            "Open-source Dash runs on Flask and requires manual infrastructure setup to scale",
        ],
    },
]


def compare():
    return common_compare(
        kicker="Compare",
        heading_lines=[
            "How You Benefit ",
            "With Reflex vs. ",
            "Streamlit, Dash, Gradio",
        ],
        description="Streamlit, Dash, and Gradio get you prototyping fast. Reflex lets you finish. Here's how Reflex compares to the leading low-code Python frameworks.",
        top_left_title="Reflex",
        top_right_title="Streamlit, Dash, Gradio",
        comparison_items=COMPARISON_ITEMS,
    )


__all__ = ["compare"]
