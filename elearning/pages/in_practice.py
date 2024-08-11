"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts, Videos

import reflex as rx


def main_text() -> rx.Component:
    return Texts.open_markdown("markdown_files/examples/in_practice.md")


def main_text2() -> rx.Component:
    return Texts.open_markdown("markdown_files/examples/in_practice2.md")




def studyhack_video() -> rx.Component:
    return Videos.video_element(path="/videos/studyhack.mp4", textpath="markdown_files/examples/explanation_studyhack_video.md")


def study_adviser_video() -> rx.Component:
    return Videos.video_element(path="/videos/study_advisers_v2.mp4", textpath="markdown_files/examples/study_advisers.md")


def go_to_software() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/software")
                     )

# The videos that are used:



@template(route="/in_practice", title="2. Practical tips")
def in_practice() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        main_text(),
        studyhack_video(),
        main_text2(),
        study_adviser_video(),
        go_to_software(),
    )

