"""Hugeicons Icon component."""

from reflex.components.component import Component
from reflex.utils import format
from reflex.vars.base import Var


class HugeIconComponent(Component):
    """Huge Icon Component."""

    library = "hugeicons-react@0.3.0"


class HugeIcon(HugeIconComponent):
    """A HugeIcon component."""

    tag = "None"

    # The size of the icon in pixels.
    size: Var[int] = 16

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Initialize the Icon component.

        Run some additional checks on Icon component.

        Args:
            *children: The positional arguments
            **props: The keyword arguments

        Raises:
            AttributeError: The errors tied to bad usage of the Icon component.
            ValueError: If the icon tag is invalid.

        Returns:
            The created component.

        """
        if children:
            if len(children) == 1 and isinstance(children[0], str):
                props["tag"] = children[0]
                children = []
            else:
                raise AttributeError(
                    f"Passing multiple children to Icon component is not allowed: remove positional arguments {children[1:]} to fix"
                )
        if "tag" not in props:
            raise AttributeError("Missing 'tag' keyword-argument for HugeIcon")

        if not isinstance(props["tag"], str):
            raise ValueError(f"Invalid icon tag: {props['tag']}.")

        props["tag"] = format.to_title_case(format.to_snake_case(props["tag"])) + "Icon"
        props["alias"] = f"Huge{props['tag']}"
        props.setdefault("stroke_width", 2)
        return super().create(*children, **props)


hi = HugeIcon.create
