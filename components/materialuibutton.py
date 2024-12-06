from reactpy import component , web, html
from fastapi import FastAPI
from reactpy.backend.fastapi import configure

mui = web.module_from_url(
    "https://cdn.jsdelivr.net/npm/@mui/material@5.15.7/umd/material-ui.production.min.js"
)

# Export the Button component
Button = web.export(mui, "Button")

@component
def MaterialUIButton():
    def handle_click(event):
        print("Material-UI Button clicked!")

    return html.div(
        Button(
            {
                "variant": "contained",
                "color": "primary",
                "onClick": handle_click,
            },
            "Click Me!"
        )
    )

app=FastAPI()
configure(app,MaterialUIButton)