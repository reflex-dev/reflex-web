from typing import Generator

import reflex as rx

PIXEL_SCRIPT_KOALA: str = """
!function(t){if(window.ko)return;window.ko=[],["identify","track","removeListeners","on","off","qualify","ready"].forEach(function(t){ko[t]=function(){var n=[].slice.call(arguments);return n.unshift(t),ko.push(n),ko}});var n=document.createElement("script");n.async=!0,n.setAttribute("src","https://cdn.getkoala.com/v1/pk_733c6bff981543743bd2d53b4d7e95cc9b3f/sdk.js"),(document.body || document.head).appendChild(n)}();
"""


def get_pixel_website_trackers() -> Generator[rx.Component, None, None]:
    yield rx.script(
        PIXEL_SCRIPT_KOALA,
    )
