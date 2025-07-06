import reflex as rx

def footer():
    return rx.el.footer(
        "© 2025 by diegucci",
        
        style={
            "position": "fixed",
            "bottom": "0",
            "left": "0",
            "width": "100%",
            "height": "50px",  # adjust as needed
            "background_color": "#3a2c1a",  # or any color
            "color": "white",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "z_index": "10",
        },
    )