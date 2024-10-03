
import reflex as rx

from pcweb.utils import signup_for_newsletter


class IndexState(rx.State):
    """Hold the state for the home page."""

    # Whether the user signed up for the newsletter.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def signup_for_another_user(self):
        self.signed_up = False

    def signup(
        self,
        form_data: dict[str, str],
    ):
        """Sign the user up for the newsletter."""
        errors = signup_for_newsletter(form_data.get("input_email"))
        if errors is not None:
            return rx.toast.warning(
                            errors,
                            style={
                                "border": "1px solid #3C3646",
                                "background": "linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%)",
                            },
                        )
        self.signed_up = True
        return
