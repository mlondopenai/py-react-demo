from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure


@component
def Photo(alt_text="Puppy", image_id=237):
    return html.img(
        {
            "src": f"https://picsum.photos/id/{image_id}/500/200",
            "style": {"width": "50%"},
            "alt": alt_text,
        }
    )

app= FastAPI()
configure(app,Photo)