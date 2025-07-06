import reflex as rx
import moure.styles.styles as styles

def title(text:str):
    return rx.heading(
        text,
        style=styles.title_style,
        color="#f2e9dc",
        font_family="Roboto Condensed"
    )