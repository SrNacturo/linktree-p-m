import reflex as rx
from moure.styles.styles import Size as Size
import moure.styles.styles as styles

def navbar():
    return rx.hstack(
        rx.image(
            src="/images/panceta&morcilla.png",
            max_width="150px",
            padding=Size.SMALL,
            margin_left=Size.SMALL,
        ),
        position="sticky",
        bg="#3a2c1a",
        z_index="999",
        top="0",
    )