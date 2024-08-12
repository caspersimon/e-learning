"""The home page of the app."""

from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts, Videos

import reflex as rx


def main_text() -> rx.Component:
    with open("markdown_files/walkthrough/walkthrough.md", encoding="utf-8") as walkthrough:
        content = walkthrough.read()
    return rx.markdown(content, component_map=styles.markdown_style)


# defining video components

def zoomin_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/aerEMTYFMS4?si=snSkWT7ct2Tt0Ap-",
    )


def cuts_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/E6CLzoaUkFM?si=tJFI5daew3Svoozt"
    )


def walkthrough_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/FAhXNF9R1-s?si=rZ9xlEbUFvYCl1Wr"
    )


def importing_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/wc3nRrvdIYw?si=jsvhFulqkwzIet7F"
    )


def keyframe_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/iTIuduDKVuA?si=c__GP6VaT-LwLmSx"
    )


def texts_video() -> rx.Component:
    return rx.video(
        url="https://www.youtube-nocookie.com/embed/E6cGiHchZnI?si=ZchszbhlRc78ztDv"
    )


# Cuts part:
def dialog_jcuts() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("How does this work in other software?")),
        rx.dialog.content(
            Texts.open_markdown("markdown_files/walkthrough/jcuts_compare.md"),
            rx.box(
                rx.dialog.close(
                    rx.button("Close", size="2"),
                ),
                padding_top="1em"
            )
        ),
    )


def cuts_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Rough cut and J-cuts"),
                dialog_jcuts(),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                cuts_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


# Texts part:
def dialog_texts() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("How does this work in other software?")),
        rx.dialog.content(
            Texts.open_markdown("markdown_files/walkthrough/texts_compare.md"),
            rx.image(src="/titleplus.png", width="300px", height="auto"),
            Texts.open_markdown("markdown_files/walkthrough/text_compare_2.md"),
            rx.box(
                rx.dialog.close(
                    rx.button("Close", size="2"),
                ),
                padding_top="1em"
            )
        ),
    )


def texts_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Adding texts"),
                dialog_texts(),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                texts_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        rx.box(
            rx.markdown(
                "The safe zones used in this video are from [this website](https://rayhollister.com/tiktok-safe-area-templates/)"
            ),
            padding_left="1em"
        ),
        width="100%",
    )


# Importing media part:
def importing_media_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Setting up your library and importing media"),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                importing_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


def navigating_fcp_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Navigating FCP"),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                walkthrough_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


def dialog_zoomin() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("How does this work in other software?")),
        rx.dialog.content(
            Texts.open_markdown("markdown_files/walkthrough/zoomin_compare.md"),
            rx.box(
                rx.dialog.close(
                    rx.button("Close", size="2"),
                ),
                padding_top="1em"
            )
        ),
    )


def zoomin_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Zooming in using adjustment Layers"),
                dialog_zoomin(),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                zoomin_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


# Keyframe part:
def dialog_keyframes() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("How does this work in other software?")),
        rx.dialog.content(
            Texts.open_markdown("markdown_files/walkthrough/keyframes_compare.md"),
            rx.box(
                rx.dialog.close(
                    rx.button("Close", size="2"),
                ),
                padding_top="1em"
            )
        ),
    )


def keyframes_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.stack(
                rx.heading("Music and keyframes"),
                dialog_keyframes(),
                flex_direction="row",
                padding="1em",
                flex_grow="0"
            )
        ),
        rx.flex(
            rx.box(
                keyframe_video(),
                flex_basis="100%",
                flex_shrink="0",
                flex_grow=1,
            ),
            padding="1em",
            flex_direction="row",
        ),
        width="100%",
    )


def go_to_music() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/music")
                     )


@template(route="/walkthrough", title="Full walkthrough")
def walkthrough() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        main_text(),
        importing_media_card(),
        navigating_fcp_card(),
        cuts_card(),
        texts_card(),
        zoomin_card(),
        keyframes_card(),
        go_to_music(),
        rx.spacer(),
    )

