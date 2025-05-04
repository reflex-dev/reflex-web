# import reflex as rx
# from pcweb.components.docpage.navbar import navbar
# from pcweb.components.webpage.badge import badge
# from pcweb.pages.framework.index_colors import index_colors
# from pcweb.pages.framework.views.footer_index import footer_index
# from pcweb.components.icons import get_icon
# from pcweb.pages.hosting_countdown.semicircle_timer import semicircle_timer, ellipsis
# from pcweb.pages.hosting_countdown.timer import timer
# from pcweb.pages.hosting_countdown.animated_box import animated_box
# from pcweb.pages.hosting_countdown.waitlist import waitlist
# from pcweb.meta.meta import hosting_meta_tags


# @rx.page(route="/launch", title="Reflex · Launch", meta=hosting_meta_tags)
# def hosting_countdown() -> rx.Component:
#     """Get the Hosting landing page."""
#     return rx.box(
#         index_colors(),
#         navbar(),
#         rx.el.main(
#             rx.box(
#                 semicircle_timer(),
#                 ellipsis(),
#                 timer(),
#                 animated_box(),
#                 class_name="flex flex-col relative justify-center items-center pt-[13rem]",
#             ),
#             waitlist(),
#             get_icon(
#                 "bottom_logo",
#                 class_name="absolute left-1/2 bottom-0 transform -translate-x-1/2 z-[-1] md:w-auto w-[21.9375rem] md:h-auto h-[4.125rem]",
#             ),
#             class_name="flex flex-col w-full relative h-full max-w-[64.19rem] border-b border-slate-4 lg:border-x",
#         ),
#         footer_index(),
#         class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
#     )
