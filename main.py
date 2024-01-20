from fastapi import FastAPI, Query
from objects.class_message import *
from settings import *

# http://127.0.0.1:8000
app = FastAPI()

@app.get("/{models}")
def get_folders(models: str):
    """
    Brief: 
        - Verifica y obtiene las distintas carpetas.
    Parametros:
        - models (str): El nombre de la carpeta proporcionado en la URL.
    Retorno:
        - La carpeta solicitada por parametro.
    """
    model = verify_models(models)
    folders = load_data(f"models/{model}.json")

    return folders

@app.get("/folders/messages/{models}")
def get_messages(models: str, from_user: str = Query("", alias="from"), to_user: str = Query("", alias="to"), subject: str = Query("", alias="subject")):   
    """
    Brief: 
        Obtiene mensajes filtrados según los parámetros especificados.
    Parametros:
        - models (str): El nombre de la carpeta proporcionado en la URL.
        - from_user (str, opcional): Filtro por remitente.
        - to_user (str, opcional): Filtro por destinatario.
        - subject (str, opcional): Filtro por asunto.
    Retorno:
        - El mensaje filtrado.
    """
    model = verify_models(models)
    message = filter_messages(f"models/{model}.json", from_user, to_user, subject)

    return message

@app.post("/folders/messages/create/{models}")
def create_message(models, message: Message):
    """
    Brief: 
        Crea un mensaje y lo guarda en la carpeta proporcionada en la URL.
    Parametros:
        - models (str): El nombre de la carpeta proporcionado en la URL.
        - message (Message): Datos del mensaje a crear.
    Retorno:
        - El mensaje de confirmacion/error.
    """
    model = verify_models(models)

    result = save_data(f"models/{model}.json", dict(message))

    return result


@app.delete("/folders/messages/delete/{models}/{message_id}")
def delete_message_by_id_endpoint(models: str, message_id: str):
    """
    Brief: 
        Elimina un mensaje según el ID proporcionado en la URL.
    Parametros:
        - models (str): El nombre de la carpeta proporcionado en la URL.
        - message_id (str): El ID del mensaje a eliminar.
    Retorno:
        - El mensaje de confirmacion/error.
    """
    model = verify_models(models)
    result = delete_message(f"models/{model}.json", model, message_id) 

    return result


















