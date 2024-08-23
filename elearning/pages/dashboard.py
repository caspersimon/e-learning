"""The dashboard page."""

from elearning.templates import template
from elearning import styles

import reflex as rx

from elearning.my_functions import Texts, Videos


def go_to_examples() -> rx.Component:
    return rx.button("Go to next chapter",
                     rx.icon("arrow-right"),
                     on_click=rx.redirect("/in_practice")
                     )


def studyroom_video() -> rx.Component:
    return Videos.video_element(path="/videos/studyroom.MP4", textpath="markdown_files/fundamentals/explanation_studyroom_video.md")


def main_text() -> rx.Component:
    return Texts.open_markdown("markdown_files/fundamentals/fundamentals.md")

@template(route="/fundamentals", title="Keeping People Interested")
def fundamentals() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.vstack(
        main_text(),
        studyroom_video(),
        go_to_examples(),
    )
