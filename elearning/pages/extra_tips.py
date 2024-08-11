"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import video, Texts, Videos

import reflex as rx

path = "markdown_files/extra"


# Importing the texts:
def intro_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/intro.md")


def handheld_text() -> rx.Component:
    return Texts.open_markdown(f"{path}/handheld.md")


def gaussian_text() ->rx.Component:
    return Texts.open_markdown(f"{path}/gaussian.md")


def transitions_text() ->rx.Component:
    return Texts.open_markdown(f"{path}/transitions.md")


# Importing the videos:
def handheld_videos() -> rx.Component:
    return Videos.two_videos_and_title(path1="/videos/8000_followers.mp4", path2="/videos/studyroom.mp4", title="Videos that used the handheld effect")


def gaussian_videos() -> rx.Component:
    return Videos.two_videos_and_title(path1="/videos/studyhack.MP4", path2="/videos/carina.MP4", title="Videos with gaussian blurs")


def go_to_speech() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/speech")
                     )


@template(route="/extra", title="4. Extra tips and tricks")
def extra_tips() -> rx.Component:

    return rx.vstack(
        intro_text(),
        handheld_text(),
        handheld_videos(),
        gaussian_text(),
        gaussian_videos(),
        transitions_text(),
        go_to_speech(),
        rx.spacer(),
    )

