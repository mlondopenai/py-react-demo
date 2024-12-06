from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

@component
def PrintButton(display_text, message_text):
    def handle_event(event):
        print(message_text)

    return html.button({"on_click": handle_event, "style":{
        "backgroundColor": '#007bff',
        "color": '#fff',
        "padding": '10px 20px',
        "border": 'none',
        "borderRadius": '4px',
        "fontSize": '16px',
        "cursor": 'pointer',
        "boxShadow": '0 2px 4px rgba(0, 0, 0, 0.1)'}}, display_text)

#We could do this as well: html.button({"onClick": lambda event: print(message_text)}, "Click me!")

app=FastAPI()
configure(app, PrintButton)