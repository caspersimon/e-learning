"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts, Videos

import reflex as rx

path = "markdown_files/software"


def text() -> rx.Component:
    return Texts.open_markdown(f"{path}/fcpx.md")

def go_to_walkthrough() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/walkthrough")
                     )

def download_templates() -> rx.Component:
    return rx.button(
        "Download templates",
        on_click=rx.download(url="/UvA.zip"),
    )

def text_reset_trial() ->rx.Component:
    return Texts.open_markdown("markdown_files/fcp_trial/reset_trial.md")


@template(route="/software", title="Downloading software")
def software() -> rx.Component:

    return rx.vstack(
        text(),
        download_templates(),
        go_to_walkthrough(),
        rx.spacer(),
    )

@template(route="/fcp_trial", title="Resetting the trial period")
def software() -> rx.Component:

    return rx.vstack(
        text_reset_trial(),
        rx.spacer(),
    )