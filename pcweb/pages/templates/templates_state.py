import dataclasses
from typing import TypedDict

import reflex as rx

from pcweb.constants import REFLEX_BUILD_URL


@dataclasses.dataclass
class Template:
    title: str
    id: str
    description: str
    difficulty: str
    tags: list[str]
    about: str | None = None
    requirements: list[str] | None = None
    key_features: list[str] | None = None
    tech_stack: list[str] | None = None
    faq: list[dict[str, str]] | None = None
    social: list[dict[str, str]] | None = None
    prompt: str | None = None


class TagWithCount(TypedDict):
    label: str
    count: int


class TemplatesState(rx.State):
    _templates: rx.Field[list[Template]] = rx.field(default_factory=list)
    active_template: rx.Field[Template | None] = rx.field(default=None)
    related_templates: rx.Field[list[Template]] = rx.field(default_factory=list)
    query: rx.Field[str] = rx.field(default="")
    tags: rx.Field[list[TagWithCount]] = rx.field(default_factory=list)
    checked_tags: rx.Field[set[str]] = rx.field(default_factory=set)

    def _matches_query(self, template: Template) -> bool:
        query = self.query.strip().lower()
        if not query:
            return True
        return query in template.title.lower() or query in template.description.lower()

    def _matches_tags(self, template: Template) -> bool:
        if not self.checked_tags:
            return True
        return bool(set(template.tags) & self.checked_tags)

    @rx.var
    def filtered_templates(self) -> list[Template]:
        return [
            template
            for template in self._templates
            if self._matches_query(template) and self._matches_tags(template)
        ]

    @rx.event
    def load_templates(self):
        self.query = ""
        self.checked_tags = set()
        # Create fake templates
        self._templates = [
            Template(
                title="Admin Dashboard Pro",
                id="765ed5f4-d9fc-478d-b44a-a2c7a7787927",
                description="A comprehensive admin panel template with user management, analytics dashboards, real-time monitoring, and customizable widgets. Perfect for internal tools and SaaS.",
                difficulty="Beginner",
                tags=["Tag 1", "Tag 2"],
                about="About the template",
                requirements=["Requirement 1", "Requirement 2"],
                key_features=["Key feature 1", "Key feature 2"],
                tech_stack=["Tech stack 1", "Tech stack 2"],
                faq=[{"q": "Question 1", "a": "Answer 1"}],
                social=[
                    {
                        "name": "John Doe",
                        "role": "Product Manager",
                        "text": "This is a test testimonial",
                    },
                    {
                        "name": "Jane Doe",
                        "role": "Product Manager",
                        "text": "This is a test testimonial",
                    },
                ],
            )
        ]
        self.active_template = self._templates[0]
        self.related_templates = [self._templates[0]]
        tag_counts: dict[str, int] = {}
        for template in self._templates:
            for tag in template.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        self.tags = sorted(
            [{"label": tag, "count": n} for tag, n in tag_counts.items()],
            key=lambda x: (-x["count"], x["label"]),
        )

    @rx.event(debounce=300, temporal=True)
    def set_query(self, value: str):
        self.query = value

    @rx.event
    def toggle_tag(self, value: str, checked: bool):
        if checked:
            self.checked_tags.add(value)
        else:
            self.checked_tags.discard(value)

    @rx.event
    def redirect_to_template(self, template_id: str):
        # Get the prompt from the template id
        for template in self._templates:
            if template.id == template_id:
                prompt = template.prompt
                break
        return rx.redirect(f"{REFLEX_BUILD_URL.strip('/')}/?prompt={prompt}")
