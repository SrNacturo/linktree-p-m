import reflex as rx
from moure.components.navbar import navbar
from moure.components.footer import footer
from moure.views.header.header import header
from moure.views.links.links import links
import moure.styles.styles as styles
from moure.styles.styles import Size as Size

def index():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                footer(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                align_items="center",
                justify_content="space-between",
                margin_y=Size.BIG,
            ),
            width="100%",
        ),
        bg="#755c41",
        width="100%",
        height="100vh"
    )


app = rx.App(
    style=styles.BASE_STYLES,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
        "/botonchulo.css",
    ],

)

app.add_page(index)