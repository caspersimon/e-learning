"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import video, Texts, Videos

import reflex as rx

path = "markdown_files/extra"


# Importing the texts:
def intro_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/intro.md")


def compound_clips_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/compound_clips.md")


def handheld_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/handheld.md")


def gaussian_text() ->rx.Component:
    return Texts.open_markdown(f"{path}/gaussian.md")


def transitions_text() ->rx.Component:
    return Texts.open_markdown(f"{path}/transitions.md")


# Importing the videos:
def handheld_videos() -> rx.Component:
    return Videos.two_videos_and_title(path1="/videos/8000_followers.mp4", path2="/videos/studyroom.MP4", title="Videos that used the handheld effect")


def gaussian_videos() -> rx.Component:
    return Videos.two_videos_and_title(path1="/videos/studyhack.MP4", path2="/videos/carina.MP4", title="Videos with gaussian blurs")


def compound_clips_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/Uqpsc3faGDs?si=xNaEH2ZX0YDtfKJX"
    )


def compound_clips_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Compound clips"),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                compound_clips_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


# TODO: change to the correct link
def transitions_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/aerEMTYFMS4?si=snSkWT7ct2Tt0Ap-",
    )


def transitions_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Tutorial: how to create custom transitions"),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                rx.text("dit is nog een placeholder video!"),
                transitions_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


def go_to_speech() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/speech")
                     )


@template(route="/extra", title="Extra tips and tricks")
def extra_tips() -> rx.Component:

    return rx.vstack(
        intro_text(),
        compound_clips_text(),
        compound_clips_card(),
        handheld_text(),
        handheld_videos(),
        gaussian_text(),
        gaussian_videos(),
        transitions_text(),
        transitions_card(),
        go_to_speech(),
        rx.spacer(),
    )

