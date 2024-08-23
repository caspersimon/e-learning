"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts

import reflex as rx

path = "markdown_files/enhance_speech"


def enhance_speech_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/enhance_speech.md")


def speech_video():
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/QAPATQkKexg?si=Imb2k5i3pCq-54EZ"
    )


def speech_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Improving speech: video tutorial"),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                speech_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


def go_to_reset_trial() -> rx.Component:
    return rx.button("Go to next chapter",
                     rx.icon("arrow-right"),
                     on_click=rx.redirect("/fcp_trial")
                     )


@template(route="/speech", title="Enhance Speech")
def enhance_speech() -> rx.Component:

    return rx.vstack(
        enhance_speech_text(),
        speech_card(),
        go_to_reset_trial(),
        rx.spacer(),
    )

