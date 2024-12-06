from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

@component
def TodoList():
    return html.div(
        html.h1("My Todo List"),
        html.ul(
            html.li("Design a cool new app"),
            html.li("Build it"),
            html.li("Share it with the world!"),
        )
    )

app = FastAPI()
configure(app, TodoList)