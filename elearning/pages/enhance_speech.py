"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts

import reflex as rx

path = "markdown_files/enhance_speech"


def enhance_speech_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/enhance_speech.md")


@template(route="/speech", title="Enhance Speech")
def enhance_speech() -> rx.Component:

    return rx.vstack(
        enhance_speech_text(),
        rx.spacer(),
    )

