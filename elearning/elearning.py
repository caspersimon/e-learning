"""Welcome to Reflex!."""

# Import all the pages.
from elearning.pages import *
from elearning.pages.xsettings import settings




import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""

pages = [
    {"title": "Introduction", "path": "/"},
    {"title": "Keeping People Interested", "path": "/fundamentals"},
    {"title": "Practical Examples", "path": "/in_practice"},
    {"title": "Downloading Software", "path": "/software"},
    {"title": "Editing the Video", "path": "/walkthrough"},
    {"title": "Finding music to use", "path": "/music"},
    {"title": "Downloading raw files", "path": "/DIY"},
    {"title": "Editing checklist", "path": "/checklist"},
    {"title": "Extra Effects you can try", "path": "/extra"},
    {"title": "Improve microphone quality", "path": "/speech"},
    {"title": "Reset FCP trial", "path": "/fcp_trial"},
]


# Create the app.
app = rx.App()
