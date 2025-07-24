import reflex as rx
from pcweb.pages.docs import getting_started


class CustomersState(rx.State):
    tags: list[str] = []

    @rx.event
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            self.tags.remove(tag)

    @rx.event
    def clear_tags(self):
        self.tags = []


def tag_item(tag: str):
    return rx.box(
        rx.text(
            tag,
            class_name="font-small shrink-0",
            color=rx.cond(
                CustomersState.tags.contains(tag),
                "var(--c-white-1)",
                "var(--c-slate-9)",
            ),
        ),
        class_name="flex items-center justify-center px-3 py-1.5 cursor-pointer transition-bg shrink-0",
        background_=rx.cond(
            CustomersState.tags.contains(tag),
            "var(--c-violet-9)",
            "var(--c-slate-2)",
        ),
        _hover={
            "background": rx.cond(
                CustomersState.tags.contains(tag),
                "var(--c-violet-9)",
                "var(--c-slate-3)",
            )
        },
        on_click=CustomersState.add_tag(tag),
    )


def all_tag():
    return rx.box(
        rx.text(
            "All",
            class_name="font-small shrink-0 text-slate-9",
        ),
        class_name="flex items-center justify-center px-3 py-1.5 cursor-pointer transition-bg shrink-0 bg-slate-1 hover:bg-slate-3",
        on_click=CustomersState.clear_tags(),
    )


def filtering_tags():
    return rx.box(
        # Glow
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="404" height="88" viewBox="0 0 404 88" fill="none">
  <path d="M3.05176e-05 44C3.05176e-05 68.3005 90.4385 88 202 88C313.562 88 404 68.3005 404 44C404 19.6995 313.562 0 202 0C90.4385 0 3.05176e-05 19.6995 3.05176e-05 44Z" fill="url(#paint0_radial_10972_6282)"/>
  <defs>
    <radialGradient id="paint0_radial_10972_6282" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(202 44) rotate(90) scale(44 202)">
      <stop stop-color="var(--c-violet-3)"/>
      <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>
""",
            class_name="w-[25.25rem] h-[5.5rem] shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[0] pointer-events-none -mt-2",
        ),
        rx.box(
            all_tag(),
            tag_item("Open Source"),
            tag_item("AI"),
            tag_item("Dev Tools"),
            tag_item("SaaS"),
            tag_item("Fintech"),
            class_name="shadow-large bg-slate-1 rounded-lg border border-slate-3 flex items-center divide-x divide-slate-3 mt-8 mb-12 relative overflow-hidden z-[1] overflow-x-auto",
        ),
        class_name="relative",
    )


def customers_list_item(
    company: str, link: str, tag: str, has_page: bool = False
) -> rx.Component:
    return rx.link(
        rx.box(
            rx.image(
                src=rx.color_mode_cond(
                    light=f"/customers/light/{company.lower()}/{company.lower()}_small.svg",
                    dark=f"/customers/dark/{company.lower()}/{company.lower()}_small.svg",
                ),
                alt=f"{company} logo",
                loading="lazy",
                class_name="h-5 w-auto shrink-0",
            ),
            rx.text(company, class_name="font-base font-semibold text-slate-12"),
            class_name="flex flex-row items-center gap-2.5 flex-1 justify-start",
        ),
        rx.text(
            tag, class_name="font-small-smbold text-slate-9 flex-1 flex justify-center"
        ),
        rx.cond(
            has_page,
            rx.box(
                rx.text(
                    "Read",
                    class_name="font-small text-slate-9",
                ),
                rx.icon(
                    tag="chevron-right",
                    stroke_width="2.25",
                    class_name="size-3.5 !text-slate-9",
                ),
                class_name="flex flex-row items-center gap-1.5 flex-1 justify-end",
            ),
            rx.box(
                rx.text(
                    "Visit",
                    class_name="font-small text-slate-8",
                ),
                rx.icon(
                    tag="arrow-up-right",
                    stroke_width="2.25",
                    class_name="size-3.5 !text-slate-8",
                ),
                class_name="flex flex-row items-center gap-1.5 flex-1 justify-end",
            ),
        ),
        href=link,
        underline="none",
        class_name="flex-row justify-between items-center w-full px-2.5 py-2 rounded-lg hover:bg-slate-3 transition-bg",
        display=rx.cond(
            CustomersState.tags.contains(tag) | (CustomersState.tags.length() == 0),
            "flex",
            "none",
        ),
    )


def your_company_item(
    company: str, link: str, tag: str, has_page: bool = False
) -> rx.Component:
    return rx.link(
        rx.box(
            rx.icon(
                tag="scan",
                size=21,
                stroke_width="2.5",
                class_name="!text-slate-12",
            ),
            rx.text(company, class_name="font-base font-semibold text-slate-12"),
            class_name="flex flex-row items-center gap-2.5 flex-1 justify-start",
        ),
        rx.text(
            tag, class_name="font-small-smbold text-slate-9 flex-1 flex justify-center"
        ),
        rx.box(
            rx.text(
                "Make the switch",
                class_name="font-small text-slate-12",
            ),
            rx.icon(
                tag="chevron-right",
                stroke_width="2.25",
                class_name="size-3.5 !text-slate-12",
            ),
            class_name="flex flex-row items-center gap-1.5 flex-1 justify-end",
        ),
        href=link,
        underline="none",
        class_name="flex flex-row justify-between items-center w-full px-2.5 py-2 rounded-lg hover:bg-slate-3 transition-bg",
    )


def customers_list() -> rx.Component:
    return rx.el.section(
        # Title
        rx.box(
            rx.el.h2(
                "From startups to global enterprises,",
                class_name="font-x-large text-slate-12",
            ),
            rx.el.h3(
                "ambitious builders choose Reflex",
                class_name="font-x-large text-slate-9",
            ),
            class_name="flex flex-col justify-center items-center w-full text-center text-balance",
        ),
        # Filtering tags
        filtering_tags(),
        # Customers list
        rx.box(
            # AutoDesk
            customers_list_item("AutoDesk", "/customers/autodesk", "SaaS", True),
            # Bayesline
            customers_list_item("Bayesline", "/customers/bayesline", "Fintech", True),
            # Ansa
            customers_list_item("Ansa", "/customers/ansa", "AI", True),
            # Seller X
            customers_list_item("SellerX", "/customers/sellerx", "AI", True),
            # Dell
            customers_list_item("Dell", "https://www.dell.com/", "Dev Tools"),
            # Your company
            your_company_item("Your company", getting_started.introduction.path, ""),
            class_name="flex flex-col max-w-[40rem] justify-center w-full items-center",
        ),
        class_name="flex flex-col max-w-[64.19rem] justify-center w-full lg:border-x border-slate-3 py-12 lg:py-20 items-center",
    )
