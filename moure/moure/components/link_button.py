import reflex as rx
import moure.styles.styles as styles

def link_button(title: str, body: str, url: str):
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="link",
                    width=styles.Size.BIG,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style, color="#f2e9dc"),
                    rx.text(body, style=styles.button_body_style, color="#f2e9dc"),
                ),
                align="center"
            ),
            font_family="Roboto Condensed",
            bg="#5f462b"
        ),
        href=url,
        is_external=True,
        width="100%"
    )
