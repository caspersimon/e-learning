import reflex as rx
from elearning import styles
from elearning.templates import template
from elearning.my_functions import Texts

def checklist_text() -> rx.Component:
    return Texts.open_markdown("markdown_files/DIY/checklist.md")


def go_to_extra() -> rx.Component:
    return rx.button("Go to next chapter",
                     on_click=rx.redirect("/extra")
                     )


@template(route="/checklist", title="checklist")
def checklist() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        checklist_text(),
        go_to_extra()

    )
