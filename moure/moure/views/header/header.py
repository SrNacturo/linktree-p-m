import reflex as rx

def header():
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="DF", text_align="center"),
            rx.avatar(fallback="VS", text_align="center")
        ),
        rx.text(
            "@panceta&morcilla", 
            text_align="center", 
            color="#f2e9dc"
        ),
        rx.text(
            "¡Hola, somos Diego Fernández y Victor Sánchez!", 
            text_align="center", 
            color="#f2e9dc"
        ),
        rx.text(
            "Somos jugadores de Flesh and Blood y nos dedicamos a organizar ligas online a nivel nacional", 
            text_align="center", 
            color="#f2e9dc"
        ),
        font_family="Roboto Condensed",
        align="center"
    )