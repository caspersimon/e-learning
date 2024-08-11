"""The home page of the app."""

from elearning import styles
from elearning.templates import template
import reflex as rx

from elearning.my_functions import Texts


def main_text() -> rx.Component:
    return Texts.open_markdown("markdown_files/part1.md")

def go_to_fundamentals() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/fundamentals")
                     )


@template(route="/", title="Introduction")
def index() -> rx.Component:
    """The home

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        main_text(),
        rx.spacer(),
        go_to_fundamentals(),
    )

