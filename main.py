from fastapi import FastAPI, Query
from settings import *

app = FastAPI()

@app.get("/folders")
def get_folders():
    folders = load_data("models/folders.json")
    return folders

@app.get("/folders/messages")
def get_messages(models: str = Query("", alias="models"), from_user: str = Query("", alias="from"), to_user: str = Query("", alias="to"), subject: str = Query("", alias="subject")):

    model = comparate_models(models)

    message = filter_messages(f"models/{model}.json", from_user, to_user, subject)
    return message


@app.delete("/folders/messages/delete/{message_id}")
def delete_message_by_id_endpoint(message_id):
    
    # Call the function to delete the message by ID
    result = delete_message("models/inbox.json", message_id)
    return result










# # @app.post("/message/create")
# # def create_message():
# #     return "Mensaje creado"

# @app.delete("/messages/delete/{id}")
# def delete(id: int):
#     delete_message(id)
#     return "Mensaje Eliminado"







# # http://127.0.0.1:8000











