import reflex as rx

from pcweb.components.new_button import button
from pcweb.components.user_input import input

TAGS = {
    "Category": [
        "AI/ML",
        "Dashboard",
        "Chat",
        "Data Visualization",
        "Image Generation",
        "API Tools",
        "Sports",
        "DevOps",
    ],
}

ITEMS_PER_PAGE = 12


class TemplatesState(rx.State):
    query: rx.Field[str] = rx.field("")
    checked_tags: rx.Field[set[str]] = rx.field(set())
    page: rx.Field[int] = rx.field(1)
    total_pages: rx.Field[int] = rx.field(1)

    def _get_all_filtered_templates(self) -> list[str]:
        from pcweb.pages.gallery.apps import gallery_apps_data

        filtered = []
        for (path, folder), document in gallery_apps_data.items():
            if folder != "templates/":
                continue

            app_metadata = document.metadata
            app_title = app_metadata.get("title", "")
            app_description = app_metadata.get("description", "")
            app_tags = app_metadata.get("tags", [])


            # Text search filtering
            if self.query.strip():
                query_lower = self.query.lower()
                if not (
                    query_lower in app_title.lower()
                    or query_lower in app_description.lower()
                ):
                    continue

            # Tag filtering
            if self.checked_tags and not (set(app_tags) & self.checked_tags):
                continue

            filtered.append(app_title)

        return filtered

    @rx.event
    def clear_filters(self):
        self.checked_tags = set()
        self.page = 1

    @rx.var
    def filtered_templates(self) -> list[str]:
        all_filtered = self._get_all_filtered_templates()
        self.total_pages = (
            (len(all_filtered) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
            if all_filtered
            else 1
        )
        start = (self.page - 1) * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE
        return all_filtered[start:end]

    @rx.event
    def set_query(self, value: str):
        self.query = value
        self.page = 1

    @rx.event
    def toggle_template(self, value: str):
        if value in self.checked_tags:
            self.checked_tags.remove(value)
        else:
            self.checked_tags.add(value)
        self.page = 1

    @rx.event
    def prev_page(self):
        if self.page > 1:
            self.page -= 1

    @rx.event
    def next_page(self):
        if self.page < self.total_pages:
            self.page += 1


def pagination() -> rx.Component:
    return rx.box(
        rx.box(
            button(
                icon=rx.icon(tag="chevron-left", size=16, class_name="!text-slate-10"),
                disabled=TemplatesState.page == 1,
                variant="secondary",
                size="icon-sm",
                on_click=TemplatesState.prev_page,
            ),
            button(
                icon=rx.icon(tag="chevron-right", size=16, class_name="!text-slate-10"),
                disabled=TemplatesState.page == TemplatesState.total_pages,
                variant="secondary",
                size="icon-sm",
                on_click=TemplatesState.next_page,
            ),
            class_name="flex flex-row items-center gap-2",
        ),
        rx.text(
            f"{TemplatesState.page} of {TemplatesState.total_pages}",
            class_name="text-sm text-slate-12 font-medium",
        ),
        class_name="flex flex-row items-center gap-6 mt-10",
    )


def checkbox_item(text: str, value: str):
    return rx.box(
        rx.checkbox(
            checked=TemplatesState.checked_tags.contains(value),
            on_change=TemplatesState.toggle_template(value),
            color_scheme="violet",
            key=value,
        ),
        rx.text(
            text,
            class_name="text-sm font-medium text-slate-12 font-sans cursor-pointer",
        ),
        on_click=TemplatesState.toggle_template(value),
        class_name="flex flex-row items-center gap-2 px-3 py-2 rounded-md bg-slate-3 hover:bg-slate-4 transition-colors cursor-pointer",
    )


def filter_section(title: str, content: list[str]):
    return rx.accordion.item(
        rx.accordion.trigger(
            rx.el.h3(
                title, class_name="font-semibold text-base text-slate-12 text-start"
            ),
            rx.icon(
                tag="chevron-down",
                size=19,
                class_name="!text-slate-11 group-data-[state=open]:rotate-180 transition-transform",
            ),
            class_name="hover:!bg-transparent !p-[0.5rem_0rem] !justify-between gap-4 group !mb-2",
        ),
        rx.accordion.content(
            rx.box(
                *[checkbox_item(item, item) for item in content],
                class_name="flex flex-col gap-2",
            ),
            class_name="before:!h-0 after:!h-0 radix-state-open:animate-accordion-down radix-state-closed:animate-accordion-up transition-all !px-0",
        ),
        value=title,
        class_name="!p-0 w-full !bg-transparent !rounded-none !shadow-none",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.el.h4(
                    "Filter Templates",
                    class_name="text-base font-semibold text-slate-12",
                ),
                rx.cond(
                    TemplatesState.checked_tags,
                    rx.el.p(
                        f"Clear filters ({TemplatesState.checked_tags.length()})",
                        on_click=TemplatesState.clear_filters,
                        class_name="text-sm text-slate-9 underline hover:text-slate-11 transition-colors cursor-pointer",
                    ),
                ),
                class_name="flex flex-row items-center gap-2 justify-between",
            ),
            input(
                icon="search-01",
                placeholder="Search...",
                class_name="w-full",
                on_change=TemplatesState.set_query.debounce(300),
                clear_button_event=TemplatesState.set_query(""),
            ),
            class_name="flex flex-col gap-2",
        ),
        rx.accordion.root(
            *[filter_section(title, content) for title, content in TAGS.items()],
            default_value=list(TAGS.keys())[0],
            collapsible=True,
            class_name="!p-0 w-full !bg-transparent !rounded-none !shadow-none flex flex-col gap-4",
        ),
        class_name="flex flex-col gap-4",
    )
