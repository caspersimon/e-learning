"""Sidebar component for the app."""

from elearning import styles, elearning

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.color_mode_cond(
            rx.image(src="/uva_black.jpg", height="2em"),
            rx.image(src="/uva_white.JPG", height="2em"),
        ),
        rx.spacer(),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding_x="1em",
        padding_y="2em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.link(
            rx.text("Settings"),
            href="/settings/",
            color_scheme="gray",
        ),

        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text,
            ),
            bg=rx.cond(
                active,
                rx.color("accent", 2),
                "transparent",
            ),
            border=rx.cond(
                active,
                f"1px solid {rx.color('accent', 6)}",
                f"1px solid {rx.color('gray', 6)}",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            padding="1em",
        ),
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            sidebar_header(),

            # The first three items:

            rx.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["path"].strip("/").capitalize()),
                        url=page["path"],
                    )
                    for page in elearning.pages[0:3] if page["path"] != "/settings"
                ],

                # Items under header "Getting Started"
                rx.heading("Getting Started", size="5"),
                *[
                    sidebar_item(
                        text=page.get("title", page["path"].strip("/").capitalize()),
                        url=page["path"],
                    )
                    for page in elearning.pages[3:6] if page["path"] != "/settings"
                ],

                # Items under header "DIY"
                rx.heading("DIY", size="5"),
                *[
                    sidebar_item(
                        text=page.get("title", page["path"].strip("/").capitalize()),
                        url=page["path"],
                    )
                    for page in elearning.pages[6:8] if page["path"] != "/settings"
                ],

                # Items under header "Extra Material"
                rx.heading("Extra Material", size="5"),
                *[
                    sidebar_item(
                        text=page.get("title", page["path"].strip("/").capitalize()),
                        url=page["path"],
                    )
                    for page in elearning.pages[8:] if page["path"] != "/settings"
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding_top="1em",
                padding_x="1em"
            ),
            rx.spacer(),
            sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
