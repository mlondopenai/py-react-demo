from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure
from components.todolist import TodoList
from components.photo import Photo
from components.gallery import Gallery
from components.button import PrintButton
from components.state import State
from components.statefullist import ArtistList
from components.materialuibutton import MaterialUIButton

@component
def App():
    return html.div(
        HelloWorld(),  # Each component is correctly passed as a child
        TodoList(),
        Photo(),
        Gallery(),
        PrintButton("Play", "Playing"),
        PrintButton("Pause", "Paused"),
        State(),
        ArtistList(),
        MaterialUIButton(),
    )

@component
def HelloWorld():
    return html.div(
        html.h1("Hello, world!")
    )



app = FastAPI()
configure(app, App)