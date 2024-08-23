"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts

import reflex as rx

path = "markdown_files/music"


def main_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/music.md")


def go_to_diy() -> rx.Component:
    return rx.button("Go to next chapter",
                     rx.icon("arrow-right"),
                     on_click=rx.redirect("/DIY")
                     )


@template(route="/music", title="Music")
def music_page() -> rx.Component:

    return rx.vstack(
        main_text(),
        go_to_diy(),
        rx.spacer(),
    )

