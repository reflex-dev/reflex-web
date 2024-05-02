import reflex as rx

common_style = dict(
    width="100%",
    align_items="start",
)



def profileBar():
    return rx.vstack(
        rx.heading(
            "Account",
            color="#FAFAFA",
            font_weight="bold",
        ),
        rx.text(
            "Manage your account settings and set e-mail preferences.",
            color="#A1A1AA",
        ),
        padding_buttom="1px",
        **common_style,
    )


def username_field():
    return rx.vstack(
        rx.text("Username", color="#FAFAFA"),
        rx.input(
            placeholder="JohnDoe123",
            width="100%",
        ),
        rx.text(
            "Your username is how other community members will see you. This name will be used to credit you for things you share on Reflex. You can change it at any time.",
            color="#A1A1AA",
        ),
        padding_top="1px",
        **common_style,
    )

def notifiction_field():
    return rx.vstack(
        rx.text("Notifications", color="#FAFAFA"),
        rx.checkbox(
            "Email me when someone mentions me in a post",
            default_checked=True,
            spacing="2",
        ),
        rx.checkbox(
            "Email me when someone follows me",
            default_checked=True,
            spacing="2",
        ),
        rx.checkbox(
            "Email me when someone comments on my post",
            default_checked=True,
            spacing="2",
        ),
        rx.text(
            "You can manage verified email addresses in your email settings.",
            color="#A1A1AA",
        ),
        **common_style
    )

def location_field():
    return rx.vstack(
        rx.text("Location", color="#FAFAFA"),
        rx.input(placeholder="Enter your location", width="100%"),
        rx.text(
            "Let others know where you are based. You can provide your city, state, or country.",
            color="#A1A1AA",
        ),
        **common_style
    )

def bio_field():
    return rx.vstack(
        rx.text("Bio", color="#FAFAFA"),
        rx.text_area(placeholder="enter your bio", width="100%"),
        rx.text(
            "You can @mention other users and organizations to link to them.",
            color="#A1A1AA",
        ),
        **common_style
    )

def skill_level():
    return rx.vstack(
        rx.text("Skill Level", color="#FAFAFA"),
        rx.radio(
            ["1", "2", "3", "4", "5"],
            direction="row",
            spacing="8",
            size="3",
        ),
        rx.text(
            "Rate your skill level in the technology you are most comfortable with. This will help others understand your expertise.",
            color="#A1A1AA"
        ),
        **common_style
    )

def update_profile_button():
    return rx.box(
        rx.button(
            "Save Changes",
        ),
        padding_top="5px",
        padding_left="10px",
        padding_buttom="20px",
    )

def profile_form():
    return rx.scroll_area(
        rx.vstack(
            profileBar(),
            username_field(),
            location_field(),
            notifiction_field(),
            bio_field(),
            skill_level(),
            update_profile_button(),
            rx.box(height="15px"),
            width="100%",
            height="100%",
            align_items="left",
        ),
        width=["100%", "100%", "80%", "80%", "80%", "80%"],
        max_height="30em", 

    )