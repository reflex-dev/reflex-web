import reflex as rx

from pcweb import styles


def format_segment(segment: str) -> str:
    if segment == "":
        return "Home"
    return " ".join(segment.split("-")).title()


class RouteState(rx.State):
    @rx.var
    def route_segments(self) -> list[tuple[str, str]]:
        segments = self.router.page.path.split("/")

        return [
            (format_segment(segment), "/".join(segments[:index + 1]))
            for index, segment in enumerate(segments)
        ]


def breadcrumbs() -> rx.Component:
    return rx.breadcrumb(
        rx.foreach(
            RouteState.route_segments,
            lambda segment, _: rx.breadcrumb_item(
                rx.breadcrumb_link(segment[0], href=segment[1])
            )
        )
    )