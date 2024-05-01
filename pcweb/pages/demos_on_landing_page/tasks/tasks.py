import reflex as rx


class TaskState(rx.State):
    task_filter: str

    tasks: list[dict[str, str]] = [
        {
            "id": "3f8c327e-7dbb-4a52-b18b-45c6152a8f39",
            "title": "Optimize database queries by analyzing performance metrics",
            "status": "In Progress",
            "priority": "Medium",
            "opacity": "1",
        },
        {
            "id": "789456ad-9cde-4f5b-a12e-789012345678",
            "title": "Implement user authentication with multi-factor authentication support",
            "status": "Completed",
            "priority": "High",
            "opacity": "1",
        },
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "title": "Write comprehensive unit tests for API endpoints to ensure robustness",
            "status": "Cancelled",
            "priority": "Medium",
            "opacity": "1",
        },
        {
            "id": "abcdef12-3456-7890-abcd-ef1234567890",
            "title": "Fix critical bug in registration form causing data loss for users",
            "status": "Backlog",
            "priority": "Low",
            "opacity": "1",
        },
        {
            "id": "1a2b3c4d-5e6f-7a8b-9c0d-1a2b3c4d5e6f",
            "title": "Optimize database queries by indexing frequently accessed columns",
            "status": "In Progress",
            "priority": "High",
            "opacity": "1",
        },
        {
            "id": "67890abc-def1-2345-6789-0abcdef12345",
            "title": "Update user interface with modern design principles for enhanced user experience",
            "status": "In Progress",
            "priority": "Medium",
            "opacity": "1",
        },
        {
            "id": "0a1b2c3d-4e5f-6a7b-8c9d-0a1b2c3d4e5f",
            "title": "Implement pagination to data tables for improved data presentation",
            "status": "Completed",
            "priority": "Low",
            "opacity": "1",
        },
        {
            "id": "4f5e6d7c-8b9a-0c1d-2e3f-4f5e6d7c8b9a",
            "title": "Refactor CSS styles to follow BEM methodology for better maintainability",
            "status": "In Progress",
            "priority": "Medium",
            "opacity": "1",
        },
        {
            "id": "2e3f4a5b-6c7d-8e9f-0a1b-2e3f4a5b6c7d",
            "title": "Add input validation to form inputs to prevent invalid data submission",
            "status": "Cancelled",
            "priority": "High",
            "opacity": "1",
        },
        {
            "id": "8d9e0f1a-2b3c-4d5e-6f7a-8d9e0f1a2b3c",
            "title": "Optimize server response time by implementing asynchronous processing",
            "status": "Backlog",
            "priority": "High",
            "opacity": "1",
        },
        {
            "id": "6f7a8b9c-0d1e-2f3a-4b5c-6f7a8b9c0d1e",
            "title": "Fix compatibility issues with Internet Explorer 11 for broader browser support",
            "status": "In Progress",
            "priority": "Low",
        },
        {
            "id": "9e8d7c6b-5a4f-3e2d-1c0b-9e8d7c6b5a4f",
            "title": "Design new landing page with interactive elements to engage users",
            "status": "Backlog",
            "priority": "Medium",
        },
        {
            "id": "5a4b3c2d-1e9f-7a8b-6c5d-3a2b1e9f7a8b",
            "title": "Test application on different browsers to ensure cross-compatibility",
            "status": "In Progress",
            "priority": "High",
        },
        {
            "id": "1e9f7a8b-6c5d-3a2b-1e9f-7a8b6c5d3a2b",
            "title": "Fix broken links in documentation for better accessibility",
            "status": "In Progress",
            "priority": "Low",
        },
        {
            "id": "6c5d3a2b-1e9f-7a8b-6c5d-3a2b1e9f7a8b",
            "title": "Update privacy policy to comply with new regulations",
            "status": "Completed",
            "priority": "Low",
        },
        {
            "id": "3a2b1e9f-7a8b-6c5d-3a2b-1e9f7a8b6c5d",
            "title": "Refactor error handling to provide more detailed error messages",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "1b2c3d4e-5f6a-7b8c-9d0a-1b2c3d4e5f6a",
            "title": "Write documentation for new feature to assist users with its usage",
            "status": "Completed",
            "priority": "High",
        },
        {
            "id": "7b8c9d0a-1b2c-3d4e-5f6a-7b8c9d0a1b2c",
            "title": "Fix layout issues on mobile devices for improved mobile experience",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "5f6a7b8c-9d0a-1b2c-3d4e-5f6a7b8c9d0a",
            "title": "Optimize images for better performance and faster loading times",
            "status": "Backlog",
            "priority": "Low",
        },
        {
            "id": "4e5f6a7b-8c9d-0a1b-2c3d-4e5f6a7b8c9d",
            "title": "Implement caching mechanism for frequently accessed data",
            "status": "In Progress",
            "priority": "High",
        },
        {
            "id": "3d4e5f6a-7b8c-9d0a-1b2c-3d4e5f6a7b8c",
            "title": "Refactor user profile page to provide a more intuitive user experience",
            "status": "Completed",
            "priority": "Medium",
        },
    ]

    copy_tasks: list[dict[str, str]] = [
        {
            "id": "3f8c327e-7dbb-4a52-b18b-45c6152a8f39",
            "title": "Optimize database queries by analyzing performance metrics",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "789456ad-9cde-4f5b-a12e-789012345678",
            "title": "Implement user authentication with multi-factor authentication support",
            "status": "Completed",
            "priority": "High",
        },
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "title": "Write comprehensive unit tests for API endpoints to ensure robustness",
            "status": "Cancelled",
            "priority": "Medium",
        },
        {
            "id": "abcdef12-3456-7890-abcd-ef1234567890",
            "title": "Fix critical bug in registration form causing data loss for users",
            "status": "Backlog",
            "priority": "Low",
        },
        {
            "id": "1a2b3c4d-5e6f-7a8b-9c0d-1a2b3c4d5e6f",
            "title": "Optimize database queries by indexing frequently accessed columns",
            "status": "In Progress",
            "priority": "High",
        },
        {
            "id": "67890abc-def1-2345-6789-0abcdef12345",
            "title": "Update user interface with modern design principles for enhanced user experience",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "0a1b2c3d-4e5f-6a7b-8c9d-0a1b2c3d4e5f",
            "title": "Implement pagination to data tables for improved data presentation",
            "status": "Completed",
            "priority": "Low",
        },
        {
            "id": "4f5e6d7c-8b9a-0c1d-2e3f-4f5e6d7c8b9a",
            "title": "Refactor CSS styles to follow BEM methodology for better maintainability",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "2e3f4a5b-6c7d-8e9f-0a1b-2e3f4a5b6c7d",
            "title": "Add input validation to form inputs to prevent invalid data submission",
            "status": "Cancelled",
            "priority": "High",
        },
        {
            "id": "8d9e0f1a-2b3c-4d5e-6f7a-8d9e0f1a2b3c",
            "title": "Optimize server response time by implementing asynchronous processing",
            "status": "Backlog",
            "priority": "High",
        },
        {
            "id": "6f7a8b9c-0d1e-2f3a-4b5c-6f7a8b9c0d1e",
            "title": "Fix compatibility issues with Internet Explorer 11 for broader browser support",
            "status": "In Progress",
            "priority": "Low",
        },
        {
            "id": "9e8d7c6b-5a4f-3e2d-1c0b-9e8d7c6b5a4f",
            "title": "Design new landing page with interactive elements to engage users",
            "status": "Backlog",
            "priority": "Medium",
        },
        {
            "id": "5a4b3c2d-1e9f-7a8b-6c5d-3a2b1e9f7a8b",
            "title": "Test application on different browsers to ensure cross-compatibility",
            "status": "In Progress",
            "priority": "High",
        },
        {
            "id": "1e9f7a8b-6c5d-3a2b-1e9f-7a8b6c5d3a2b",
            "title": "Fix broken links in documentation for better accessibility",
            "status": "In Progress",
            "priority": "Low",
        },
        {
            "id": "6c5d3a2b-1e9f-7a8b-6c5d-3a2b1e9f7a8b",
            "title": "Update privacy policy to comply with new regulations",
            "status": "Completed",
            "priority": "Low",
        },
        {
            "id": "3a2b1e9f-7a8b-6c5d-3a2b-1e9f7a8b6c5d",
            "title": "Refactor error handling to provide more detailed error messages",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "1b2c3d4e-5f6a-7b8c-9d0a-1b2c3d4e5f6a",
            "title": "Write documentation for new feature to assist users with its usage",
            "status": "Completed",
            "priority": "High",
        },
        {
            "id": "7b8c9d0a-1b2c-3d4e-5f6a-7b8c9d0a1b2c",
            "title": "Fix layout issues on mobile devices for improved mobile experience",
            "status": "In Progress",
            "priority": "Medium",
        },
        {
            "id": "5f6a7b8c-9d0a-1b2c-3d4e-5f6a7b8c9d0a",
            "title": "Optimize images for better performance and faster loading times",
            "status": "Backlog",
            "priority": "Low",
        },
        {
            "id": "4e5f6a7b-8c9d-0a1b-2c3d-4e5f6a7b8c9d",
            "title": "Implement caching mechanism for frequently accessed data",
            "status": "In Progress",
            "priority": "High",
        },
        {
            "id": "3d4e5f6a-7b8c-9d0a-1b2c-3d4e5f6a7b8c",
            "title": "Refactor user profile page to provide a more intuitive user experience",
            "status": "Completed",
            "priority": "Medium",
        },
    ]

    def filter_tasks(self, name: str):
        if name == "All":
            self.copy_tasks = self.tasks
        else:
            self.copy_tasks = [task for task in self.tasks if task["status"] == name]

    def filter_tasks_by_input(self, value: str):
        self.task_filter = value

        self.copy_tasks = [
            task
            for task in self.tasks
            if self.task_filter.lower() in task["title"].lower()
        ]


def render_title():
    return rx.vstack(
        rx.heading("Welcome back!", size="7", color="#FFFFFF", text_align="start"),
        rx.heading(
            "Here's a list of your tasks!",
            size="2",
            color="#9c9d9d",
            text_align="start",
            weight="light",
        ),
        width="100%",
        align_items="start",
    )


def render_filter_bar():
    def create_filter(name: str):
        return rx.hstack(
            rx.text(name, color="white"),
            justify_content="space-between",
            align_items="center",
            padding="0.25em 0.5em",
            border="1px dashed #a1a1a9",
            border_radius="8px",
            on_click=TaskState.filter_tasks(name),
            cursor="pointer",
            _hover={"bg": "#a1a1a9"},
            transition="all 550ms ease",
        )

    return rx.hstack(
        rx.chakra.input(
            value=TaskState.task_filter,
            placeholder="Filter tasks...",
            bg="transparent",
            on_change=TaskState.filter_tasks_by_input,
            color="white",
            flex=["100%", "100%", "100%", "100%", "30%"],
        ),
        rx.hstack(
            create_filter("All"),
            create_filter("Completed"),
            create_filter("In Progress"),
            create_filter("Cancelled"),
            create_filter("Backlog"),
            flex=["100%", "100%", "100%", "100%", "60%"],
            padding="0.25em 0em",
            display="flex",
            flex_wrap="wrap",
            gap="0.65em 0.45em",
        ),
        width="100%",
        padding_top="2em",
        padding_bottom="0.5em",
        display="flex",
        flex_wrap="wrap",
        justify_content="center",
    )


def render_task_data(data: dict[str, str]):
    def create_filter(name: str, tag: str):
        return rx.hstack(
            rx.icon(tag=tag, color="#a1a1a9", transform="scale(0.75)"),
            rx.text(name, color="white"),
            align_items="center",
            justify_content="center",
        )

    def create_priority(name: str, tag: str):
        return rx.hstack(
            rx.icon(tag=tag, color="#a1a1a9", transform="scale(0.75)"),
            rx.text(name, color="white"),
            align_items="center",
            justify_content="center",
        )

    return rx.hstack(
        rx.hstack(
            rx.text(data["title"], color="white"),
            flex=["100%", "100%", "100%", "100%", "65%"],
            justify_content="start",
        ),
        rx.hstack(
            rx.hstack(
                rx.match(
                    data["status"],
                    ("Completed", create_filter(data["status"], "circle-check")),
                    ("In Progress", create_filter(data["status"], "timer")),
                    ("Cancelled", create_filter(data["status"], "circle-x")),
                    ("Backlog", create_filter(data["status"], "circle-help")),
                ),
                flex=["none", "none", "none", "none", "15%"],
                display="flex",
            ),
            rx.hstack(
                rx.match(
                    data["priority"],
                    ("High", create_priority(data["priority"], "square-arrow-up")),
                    ("Medium", create_priority(data["priority"], "square-arrow-right")),
                    ("Low", create_priority(data["priority"], "square-arrow-down")),
                ),
                flex=["none", "none", "none", "none", "15%"],
                display="flex",
            ),
            flex=["100%", "100%", "100%", "100%", "30%"],
        ),
        width="100%",
        border_bottom="2px solid #262628",
        display="flex",
        flex_wrap="wrap",
        padding="0.5em 0em",
        _hover={"border_bottom": "0.75px solid #a1a1a9"},
        transition="all 550ms ease",
    )


def task():
    return rx.vstack(
        render_title(),
        render_filter_bar(),
        rx.vstack(
            rx.foreach(
                TaskState.copy_tasks,
                render_task_data,
            ),
            border="0.75px solid gray",
            padding="1em 1em",
            width="100%",
            border_radius="8px",
            overflow="auto",
            height="70vh",
        ),
        width="100%",
        padding="1.5em 1.5em",
        height="75vh",
    )
