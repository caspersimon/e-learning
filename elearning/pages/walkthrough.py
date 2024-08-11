"""The home page of the app."""

from elearning import styles
from elearning.templates import template

import reflex as rx


def main_text() -> rx.Component:
    with open("markdown_files/walkthrough/walkthrough.md", encoding="utf-8") as walkthrough:
        content = walkthrough.read()
    return rx.markdown(content, component_map=styles.markdown_style)


def go_to_music() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/music")
                     )


@template(route="/walkthrough", title="Full walkthrough")
def walkthrough() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        main_text(),
        go_to_music(),
        rx.spacer(),
    )

