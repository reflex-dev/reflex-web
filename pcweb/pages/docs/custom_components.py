import reflex as rx
from pcweb.templates.docpage import docpage, h1_comp, text_comp
import httpx
import datetime

# every app must have at least one tag in order to be rendered
components_list = [
    {
        "package_name": "reflex-motion",
        "tags": [],
        "description": "A motion library for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-chat",
        "tags": [],
        "description": "A chat component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-local-auth",
        "tags": [],
        "description": "Local authentication for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-image-zoom",
        "tags": [],
        "description": "A zoomable image component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-webcam",
        "tags": [],
        "description": "A webcam component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-spline",
        "tags": [],
        "description": "A wrapper for the Spline design tool.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-color-picker",
        "tags": [],
        "description": "A color picker component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-simpleicons",
        "tags": [],
        "description": "SVG icons from the most popular brands.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },

]

def fetch_url(url):
    """Helper function to fetch data from a given URL."""
    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {url}: {response.status_code} - {response.text}")
            return None
        
def get_downloads(package_name):
    """Fetch the total downloads for the last month for a given package."""
    today = datetime.date.today()
    first_day_of_current_month = datetime.date(today.year, today.month, 1)
    last_day_of_last_month = first_day_of_current_month - datetime.timedelta(days=1)

    start_date = "2024-01-01"
    end_date = last_day_of_last_month.strftime('%Y-%m-%d')

    url = f"https://pypistats.org/api/packages/{package_name}/recent?start_date={start_date}&end_date={end_date}"
    data = fetch_url(url)

    if data:
        return data.get('data', {}).get('last_month', 0)
    return 0

def get_package_info(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch package info: {response.status_code} - {response.text}")
            return {}


def add_item(category):

    package_info = get_package_info(category["package_name"])
    name = ' '.join(word.title() for word in category["package_name"].split('-')[1:])

    return rx.flex(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        name,
                        size="3",
                    ),
                    rx.box(
                        flex_grow=1,
                    ),
                    rx.badge(
                        str(get_downloads(category["package_name"])), 
                        rx.icon(
                            tag="download",
                            size=12
                        ),
                        padding_x=".5em",
                        font_size="0.75em",
                        border_radius="6px",
                        justify="center",
                    ),
                    width="100%",
                    justify_content="center"
                ),
                rx.text(
                    category["description"],
                    color=rx.color("mauve", 11),
                    size="1", 
                ),
                align_items="start",
                width="100%",
            ),
            width="100%",
            height="5em",
            align_items="start",
        ),
        rx.box(
            flex_grow=1,
        ),
        rx.text(
            "pip install " + category["package_name"],
            width="100%",
            font_size="0.75em",
            border_radius= "4px;",
            border= f"1px solid {rx.color('violet', 5)}",
            background=  rx.color("violet", 3),
            color= rx.color("violet", 9),
            padding_x=".25em",
        ),
        rx.hstack(
            rx.text(
                "Author: " + package_info.get("info", {}).get("author", "Unknown"),
                font_size="0.75em",
            ),
            rx.spacer(),
            rx.link(
                rx.icon(
                    tag="external-link",
                    size=16,
                    color=rx.color("mauve", 9),
                ),
                href=package_info.get("info", {}).get("package_url", "#"),
            ),
            width = "100%",
            justify="center",
            padding_top=".5em",
        ),
        direction="column",
        border_radius="8px",
        height="9em",
        box_shadow=" 0px 0px 0px 1px #E8E9EB, 0px 4px 4px -4px rgba(194, 198, 215, 0.30), 0px 1px 4px -1px rgba(135, 144, 181, 0.40); #FFFFFF",
        padding=".75em",
    )

grid_layout=[1, 2, 2, 3, 3]

def component_grid(): 
    return rx.chakra.responsive_grid(
            *[
                add_item(category)
                for category in components_list
            ],
            columns=grid_layout,
            gap=4,
        )


@docpage()
def custom_components() -> rx.Component:
    return rx.flex(
        h1_comp(text="Custom Components"),
        text_comp(
            text="Reflex has a growing ecosystem of custom components that you can use to build your apps. Below is a list of some of the custom components available for Reflex."
        ),  
        component_grid(),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
