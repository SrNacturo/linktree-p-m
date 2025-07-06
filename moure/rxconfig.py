import reflex as rx

config = rx.Config(
    app_name="moure",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)