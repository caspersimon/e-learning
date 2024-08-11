from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts, Videos

import reflex as rx


def intro_text() -> rx.Component:
    return Texts.open_markdown("markdown_files/DIY/DIY_intro.md")



def download_800_library() -> rx.Component:
    return rx.button(
        "Download finished project",
        on_click=rx.download(url="raw_video_files/8000_video_library.zip"),
    )


def video_8000() -> rx.Component:
    return Videos.video_element_with_2_external_links(
        path="/videos/8000_followers.MP4",
        textpath="markdown_files/DIY/8000_video_description_DIY.md",
        link1_desc="Download raw",
        link1_url="https://amsuni-my.sharepoint.com/:u:/g/personal/j_c_s_eikmans_uva_nl/ETaQqVSqp65FuqO1JKlvFFUBdYWhjfb3gDNiYzVqzNqyHQ?e=wO7b8s",
        link2_desc="Download finished",
        link2_url="https://amsuni-my.sharepoint.com/:u:/g/personal/j_c_s_eikmans_uva_nl/ERZBFb9m87dJg_WolTs-GQ0B0jhnA8a-3CIV2yxQS9Pwog?e=UrOdUb",
        )


def video_vacancy() -> rx.Component:
    return Videos.video_element_with_2_external_links(
        path="/videos/vacancy.mp4",
        textpath="markdown_files/DIY/recruitment_video.md",
        link1_desc="Download raw",
        link1_url="https://amsuni-my.sharepoint.com/:u:/g/personal/j_c_s_eikmans_uva_nl/ESjyKERoDGNKoGZYlbiFZ_oBOXNZN2W5YsgLTmY2bxd9dw?e=k5SmKW",
        link2_desc="Download finished",
        link2_url="https://amsuni-my.sharepoint.com/:u:/g/personal/j_c_s_eikmans_uva_nl/EQxXwtdJc6xDq1hDf0KXSGwBvICUsb3qL3XBCxhqiaSNYw?e=DNtD1e",
        )


def go_to_extra() -> rx.Component:
    return rx.button("Go to Extra Effects You Can Try",
                     on_click=rx.redirect("/extra")
                     )


@template(route="/DIY", title="DIY")
def DIY() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        intro_text(),
        rx.spacer(),
        video_8000(),
        video_vacancy(),
        go_to_extra()

    )

