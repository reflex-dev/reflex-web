import dataclasses
import json
from typing import TypedDict

import reflex as rx
from reflex.utils import console

from pcweb.constants import REFLEX_BUILD_URL, REFLEX_DOMAIN_URL
from pcweb.pages.templates.templates_client import (
    fetch_all_templates,
    fetch_template_detail,
)


@dataclasses.dataclass
class Template:
    id: str
    name: str
    url: str | None = None
    priority: int = 0
    tags: list[str] = dataclasses.field(default_factory=list)
    enabled_integrations: list[str] = dataclasses.field(default_factory=list)
    difficulty: str | None = None
    description: str | None = None
    about: str | None = None
    requirements: list[str] | None = None
    key_features: list[str] | None = None
    tech_stack: list[str] | None = None
    faq: list[dict[str, str]] | None = None
    quotes: list[dict[str, str]] | None = None
    prompt: str | None = None
    last_modified: str | None = None


class TagWithCount(TypedDict):
    label: str
    count: int


def _parse_template(data: dict) -> Template:
    return Template(
        id=str(data.get("id", "")),
        name=str(data.get("name", "")).replace("_", " ").title(),
        url=data.get("url"),
        priority=data.get("priority", 0),
        tags=data.get("tags") or [],
        enabled_integrations=data.get("enabled_integrations") or [],
        difficulty=data.get("difficulty") or "beginner",
        description=data.get("description"),
        about=data.get("about"),
        requirements=data.get("requirements") or ["Python 3.10+"],
        key_features=data.get("key_features"),
        tech_stack=data.get("tech_stack") or ["Reflex"],
        faq=data.get("faq"),
        quotes=data.get("quotes"),
        prompt=data.get("prompt"),
        last_modified=str(data["last_modified"]) if data.get("last_modified") else None,
    )


def _parse_templates_map(data: list[dict]) -> dict[str, Template]:
    return {str(item.get("id", "")): _parse_template(item) for item in data}


def _compute_tags(templates: list[Template]) -> list[TagWithCount]:
    tag_counts: dict[str, int] = {}
    for template in templates:
        for tag in template.tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    return sorted(
        [{"label": tag, "count": n} for tag, n in tag_counts.items()],
        key=lambda x: (-x["count"], x["label"]),
    )


class TemplatesState(rx.State):
    _all_templates: rx.Field[dict[str, Template]] = rx.field(default_factory=dict)
    active_template: rx.Field[Template | None] = rx.field(default=None)
    related_templates: rx.Field[list[Template]] = rx.field(default_factory=list)
    query: rx.Field[str] = rx.field(default="")
    is_loading: rx.Field[bool] = rx.field(default=False)
    tags: rx.Field[list[TagWithCount]] = rx.field(default_factory=list)
    checked_tags: rx.Field[set[str]] = rx.field(default_factory=set)

    def _matches_query(self, template: Template) -> bool:
        query = self.query.strip().lower()
        if not query:
            return True
        return (
            query in template.name.lower()
            or query in (template.description or "").lower()
        )

    def _matches_tags(self, template: Template) -> bool:
        if not template.tags:
            return True
        if not self.checked_tags:
            return False
        return bool(set(template.tags) & self.checked_tags)

    @rx.var
    def faq_jsonld(self) -> str:
        t = self.active_template
        if not t or not t.faq:
            return ""
        data = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "name": t.name,
                    "description": t.description or "",
                    "url": f"{REFLEX_DOMAIN_URL.rstrip('/')}/templates/{t.id}",
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": item["question"],
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": item["answer"],
                            },
                        }
                        for item in t.faq
                    ],
                },
            ],
        }
        return json.dumps(data)

    @rx.var
    def filtered_templates(self) -> list[Template]:
        return [
            template
            for template in self._all_templates.values()
            if self._matches_query(template) and self._matches_tags(template)
        ]

    @rx.event(background=True)
    async def load_templates(self):
        async with self:
            if self._all_templates:
                self.query = ""
                self.checked_tags = {t["label"] for t in self.tags}
                return
            self.query = ""
            self.checked_tags = set()
        async with self:
            self.is_loading = True
        try:
            data = await fetch_all_templates()
            templates = _parse_templates_map(data)
            tags = _compute_tags(list(templates.values()))

            async with self:
                self._all_templates = templates
                self.tags = tags
                self.checked_tags = {t["label"] for t in tags}
        except Exception as e:
            console.error(f"Failed to load templates: {e}")
        finally:
            async with self:
                self.is_loading = False

    @rx.event(background=True)
    async def prefetch_template(self, template_id: str):
        async with self:
            active = self.active_template
            on_detail_page = "template_id" in self.router.page.params

        if on_detail_page or (active and active.id == template_id):
            return

        try:
            data = await fetch_template_detail(template_id)
            template = _parse_template(data)
            async with self:
                self.active_template = template
        except Exception as e:
            console.error(f"Prefetch failed for {template_id}: {e}")

    @rx.event(background=True)
    async def load_template_details(self, template_id: str = ""):
        async with self:
            template_id = template_id or self.router._page.params.get("template_id", "")
            active = self.active_template
            all_templates = dict(self._all_templates)

        if not template_id:
            async with self:
                self.active_template = None
                self.related_templates = []
            return

        try:
            if active and active.id == template_id:
                template = active
            else:
                data = await fetch_template_detail(template_id)
                template = _parse_template(data)

            if not all_templates:
                all_data = await fetch_all_templates()
                all_templates = _parse_templates_map(all_data)

            all_templates[template_id] = template

            active_tags = set(template.tags)
            others = [t for t in all_templates.values() if t.id != template_id]
            others.sort(key=lambda t: -len(active_tags & set(t.tags)))
            related = others[:3]

            async with self:
                self.active_template = template
                self.related_templates = related
                self._all_templates = all_templates
        except Exception as e:
            console.error(f"Failed to load template {template_id}: {e}")

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
        template = self._all_templates.get(template_id)
        if not template:
            return
        if template.prompt:
            return rx.redirect(
                f"{REFLEX_BUILD_URL.rstrip('/')}/?prompt={template.prompt}",
                is_external=True,
            )
        return rx.redirect(
            f"{REFLEX_BUILD_URL.rstrip('/')}/gen/{template_id}", is_external=True
        )
