import reflex as rx
from moure.components.link_button import link_button
from moure.components.title import title

def links():
    return rx.vstack(
        title("Redes"),
        link_button(
            "X", 
            "Publicaciones todos los lunes", 
            "https://x.com/LigaIberiaFAB"
        ),
        link_button(
            "Youtube", 
            "Partidas en directo", 
            "https://www.youtube.com/@LigaIberiaFAB"
        ), 
        link_button(
            "Discord", 
            "Servidor de la comunidad española", 
            "https://discord.gg/hBSJNsjyaT"
        ),
        align="center",
        width="100%",
    )