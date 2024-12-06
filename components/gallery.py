from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure
from components.photo import Photo

@component
def Gallery():
    return html.section(
        html.h1("Photo Gallery"),
        Photo("Landscape", image_id=830),
        Photo("City", image_id=274),
        Photo("Puppy", image_id=237),
    )

app=FastAPI()
configure(app, Gallery)