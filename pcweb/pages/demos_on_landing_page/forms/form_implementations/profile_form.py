import reflex as rx

common_style = dict(
    width="100%",
    align_items="start",
    padding="5px 10px",
)



def profileBar():
    return rx.vstack(
        rx.text(
            "Profile",
            color="#FAFAFA",
        ),
        rx.text(
            "This is how others will see you on the site.",
            color="#A1A1AA",
        ),
        padding_buttom="1px",
        **common_style,
    )


def username_field():
    return rx.vstack(
        rx.text("Username", color="#FAFAFA"),
        rx.chakra.input(
            placeholder="profile",
            width="100%",
        ),
        rx.text(
            "This is your public display name. It can be your real name or a pseudonym. You can only change this once every 90 days.",
            color="#A1A1AA",
        ),
        padding_top="1px",
        **common_style,
    )

def email_field():
    return rx.vstack(
        rx.text("Email", color="#FAFAFA"),
        rx.chakra.input(placeholder="enter your email for display", width="100%"),
        rx.text(
            "You can manage verified email addresses in your email settings.",
            color="#A1A1AA",
        ),
        **common_style
    )

def location_field():
    return rx.vstack(
        rx.text("Location", color="#FAFAFA"),
        rx.chakra.input(placeholder="Enter your location", width="100%"),
        rx.text(
            "Let others know where you are based. You can provide your city, state, or country.",
            color="#A1A1AA",
        ),
        **common_style
    )

def bio_field():
    return rx.vstack(
        rx.text("Bio", color="#FAFAFA"),
        rx.chakra.text_area(placeholder="enter your bio"),
        rx.text(
            "You can @mention other users and organizations to link to them.",
            color="#A1A1AA",
        ),
        **common_style
    )

def personal_website_field():
    return rx.vstack(
        rx.text("Personal Website", color="#FAFAFA"),
        rx.chakra.input(placeholder="input your personal website", width="100%"),
        rx.text(
            "Add links to your website, blog, or social media profiles.",
            color="#A1A1AA"
        ),
        **common_style
    )

def social_media_links_field():
    return rx.vstack(
        rx.text("Social Media Links", color="#FAFAFA"),
        rx.chakra.input(placeholder="Enter your Twitter handle", width="100%"),
        rx.chakra.input(placeholder="Enter your LinkedIn profile URL", width="100%"),
        rx.chakra.input(placeholder="Enter your GitHub username", width="100%"),
        rx.text(
            "Connect your social media profiles to showcase your online presence and engage with the community.",
            color="#A1A1AA",
        ),
        **common_style
    )

def update_profile_button():
    return rx.box(
        rx.chakra.button(
            "Update profile",
            bg="#FAFAFA",
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
            bio_field(),
            personal_website_field(),
            social_media_links_field(),
            update_profile_button(),
            rx.box(height="15px"),
            width="100%",
            height="100%",
            align_items="left",
        ),
        width="80%",
        height="100%",
    )