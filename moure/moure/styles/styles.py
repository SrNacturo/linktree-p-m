import reflex as rx
from enum import Enum



# Constants
MAX_WIDTH = "350px"


# Sizes
class Size(Enum):
    SMALL="0.5EM"
    MEDIUM="0.85EM"
    DEFAULT="1EM"
    BIG="2EM"

# Styles
BASE_STYLES = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL,
        "border_radius": Size.SMALL
    },

    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    },
}

title_style= dict(
    size="md",
    width="100%",
    padding_top=Size.DEFAULT
)

button_title_style = dict(
    font_size=Size.DEFAULT
)

button_body_style = dict(
    font_size=Size.MEDIUM
)