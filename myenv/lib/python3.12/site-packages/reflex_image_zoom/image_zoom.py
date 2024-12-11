"""Reflex custom component ImageZoom."""

import reflex as rx
from reflex.utils import imports

class ImageZoom(rx.Component):
    """ImageZoom component."""

    # The React library to wrap.
    library = "react-medium-image-zoom"

    # The React component tag.
    tag = "Zoom"

    # If the tag is the default export from the module, you must set is_default = True.
    # This is normally used when components don't have curly braces around them when importing.
    is_default = True

    def _get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            super()._get_imports(),
            {
                "": {imports.ImportVar(tag="react-medium-image-zoom/dist/styles.css")},
            },
        )

image_zoom = ImageZoom.create