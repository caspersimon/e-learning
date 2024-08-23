"""Welcome to Reflex!."""

# Import all the pages.
from elearning.pages import *
from elearning.pages.xsettings import settings




import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""

pages = [
    {"title": "Introduction", "path": "/"},
    {"title": "Keeping people interested", "path": "/fundamentals"},
    {"title": "Practical examples", "path": "/in_practice"},
    {"title": "Downloading software", "path": "/software"},
    {"title": "Editing the video", "path": "/walkthrough"},
    {"title": "Finding music to use", "path": "/music"},
    {"title": "Downloading raw files", "path": "/DIY"},
    {"title": "Editing checklist", "path": "/checklist"},
    {"title": "Extra effects you can try", "path": "/extra"},
    {"title": "Improving microphone quality", "path": "/speech"},
    {"title": "Resetting FCP trial", "path": "/fcp_trial"},
]


# Create the app.
app = rx.App()
