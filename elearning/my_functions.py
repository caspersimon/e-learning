import reflex as rx
from elearning import styles
from typing import Union


class Texts:
    def open_text(name: str):
        with open(name, encoding="utf-8") as file:
            content = file.read()
            return content

    def open_markdown(name: str):
        with open(name, encoding="utf-8") as file:
            content = file.read()
            return rx.markdown(content, component_map=styles.markdown_style)


def video(path, width: int = 400, height : Union[int, str] = "auto") -> rx.Component:

    if type(height) == int:
        height = f"{height}px"

    video = rx.video(
        url=path,
        width=f"{width}px",
        height=height
    )

    return video


class Videos:

    def video_element(path, width: int = 300, textpath: str = "markdown_files/examples/explanation_studyroom_video.md") -> rx.Component:
        return rx.card(
            rx.flex(
                rx.box(
                    video(path, width),
                    flex_basis="33%"),
                rx.flex(
                    rx.stack(
                        Texts.open_markdown(textpath),
                        flex_direction="column",
                        padding="1em"
                    )
                ),
                flex_direction="row",
            )
        )

    def video_element_with_2_downloadbuttons(path,
                                             width: int = 300,
                                             textpath: str = "markdown_files/examples/explanation_studyroom_video.md",
                                             file1_path: str = "UvA.zip",
                                             file1_desc: str = "Download file 1",
                                             file2_path: str = "UvA.zip",
                                             file2_desc: str = "Download file 2"
                                             ) -> rx.Component:
        return rx.card(
            rx.flex(
                rx.box(
                    video(path, width),
                    flex_basis="33%"
                ),
                rx.flex(
                    rx.stack(
                        Texts.open_markdown(textpath),
                        rx.spacer(),
                        rx.flex(
                            rx.stack(
                                rx.button(
                                    file1_desc,
                                    on_click=rx.download(url=file1_path),
                                ),
                                rx.button(
                                    file2_desc,
                                    on_click=rx.download(url=file2_path),
                                ),

                                flex_direction="row",
                                padding_right="1em"
                            )
                        ),
                        flex_direction="column",
                        padding="1em"
                    )
                ),
                flex_direction="row",
                align="center"
            )
        )

    def two_videos_and_title(path1, path2, width: int = 300, title: str = "Example title") -> rx.Component:
        return rx.card(
            rx.heading(title, padding="1em"),
            rx.flex(
                video(path1, width),
                video(path2, width),
                flex_direction="row",
                padding="1em",
                spacing="3"
            )
        )

    def video_element_with_2_external_links(path,
                                             width: int = 300,
                                             textpath: str = "markdown_files/examples/explanation_studyroom_video.md",
                                             link1_url: str = "UvA.zip",
                                             link1_desc: str = "Download file 1",
                                             link2_url: str = "UvA.zip",
                                             link2_desc: str = "Download file 2"
                                             ) -> rx.Component:
        return rx.card(
            rx.flex(
                rx.box(
                    video(path, width),
                    flex_basis="33%"
                ),
                rx.flex(
                    rx.stack(
                        Texts.open_markdown(textpath),
                        rx.spacer(),
                        rx.flex(
                            rx.stack(
                                rx.button(
                                    link1_desc,
                                    on_click=rx.redirect(link1_url, external=True),
                                ),
                                rx.button(
                                    link2_desc,
                                    on_click=rx.redirect(link2_url, external=True),
                                ),

                                flex_direction="row",
                                padding_right="1em"
                            )
                        ),
                        flex_direction="column",
                        padding="1em"
                    )
                ),
                flex_direction="row",
                align="center"
            )
        )