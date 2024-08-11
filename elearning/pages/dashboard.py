"""The dashboard page."""

from elearning.templates import template
from elearning import styles

import reflex as rx

from elearning.my_functions import Texts, Videos


def go_to_examples() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/in_practice")
                     )


def studyroom_video() -> rx.Component:
    return Videos.video_element(path="/videos/studyroom.mp4", textpath="markdown_files/fundamentals/explanation_studyroom_video.md")



@template(route="/fundamentals", title="Keeping People Interested")
def fundamentals() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("markdown_files/fundamentals/fundamentals.md", encoding="utf-8") as fundamentals:
        content = fundamentals.read()
    return rx.vstack(
        rx.markdown(content, component_map=styles.markdown_style),
        studyroom_video(),
        go_to_examples(),
    )
