import json

def load_data(file_path: str):
    """
    Brief: 
        Carga datos desde un archivo JSON.
    Parametros:
        - file_path (str): La ruta del archivo que se cargará.
    Retorno:
        Lista de datos cargados desde el archivo.
    """
    try:
        with open(file_path, "r", encoding="UTF8") as archive:
            data = json.load(archive)
        return data.get("data", [])
    except json.decoder.JSONDecodeError:
        print("Error decoding the JSON file.")
    except FileNotFoundError:
        print("File not found.")
    except Exception:
        print("Another unexpected error.")

def save_data(file_path: str, data: dict): 
    """
    Brief: 
        Guarda datos en un archivo JSON.
    Parametros:
        - file_path (str): La ruta del archivo que se actualizará.
        - data (dict): Los datos que se agregarán al archivo.
    Retorno:
        Un diccionario con un mensaje de confirmación o error.
    """
    result = False
    
    try:
        archive = load_data(file_path)
        if data.get("from_user") or data.get("to_user"):
            modify_data = {"id": data.pop("id"), "from": data.pop("from_user"), "to": data.pop("to_user")} 
            modify_data.update(data)
            archive.append(modify_data)
        else:
            archive.append(data)

        # Verificamos el nuevo ID
        for data in archive:
            new_id = data.get("id")
        result = verify_id(file_path, new_id)
    except Exception:
        print("The file was not loaded correctly.")


    if result:
        update_data(file_path, archive)
        return {"message": "Message created successfully"}
    else:
        return {"message": "The id already exists"}

def update_data(file_path: str, archive: dict):
    """
    Brief: 
        Actualiza los datos en un archivo JSON con la información proporcionada.
    Parametros:
        - file_path (str): La ruta del archivo que se actualizará.
        - archive (list): Lista de datos que se utilizarán para la actualización.
    Retorno:
        Sin retorno.
    """
    new_data = {"data" : archive}

    try:
        with open(file_path, "w", encoding="UTF8") as archivo:
            json.dump(new_data, archivo, indent=4)
    except json.decoder.JSONDecodeError:
        print("Error decoding the JSON file.")
    except FileNotFoundError:
        print("File not found.")
    except Exception:
        print("Another unexpected error.") 


def filter_messages(file_path = "", from_user: str = "", to_user: str = "", subject: str = ""):
    """
    Brief: 
        Filtra mensajes en base a criterios específicos.
    Parametros:
        - file_path (str): La ruta del archivo que contiene los datos (opcional).
        - from_user (str): Filtra mensajes por el remitente (opcional).
        - to_user (str): Filtra mensajes por el destinatario (opcional).
        - subject (str): Filtra mensajes por el asunto (opcional).
    Retorno:
        Lista de mensajes que cumplen con los criterios de filtrado.
    """
    archive = load_data(file_path)
    
    if isinstance(archive, list):
        filtered_messages = []

        for message in archive:
            if from_user == "" or (message.get("from") and from_user in message["from"]["name"]):
                from_match = True
            else: 
                from_match = False

            if subject == "" or (message.get("subject") and subject in message["subject"]):
                subject_match = True
            else:
                subject_match = False

            to_match = to_user == "" or any(recipient["name"] == to_user for recipient in message.get("to", []))

            if from_match and to_match and subject_match:
                filtered_messages.append(message)

        return filtered_messages

def delete_message(file_path, models, message_id: str):  #################### Probar
    """
    Brief: 
        Elimina un mensaje del archivo y, opcionalmente, lo guarda en la archivo 'starred'.
    Parametros:
        - file_path (str): La ruta del archivo que contiene los datos.
        - models (str): El nombre del archivo proporcionado en la URL.
        - message_id (str): El ID del mensaje a eliminar.
    Retorno:
        Un mensaje de confirmación o error.
    """
    archive = load_data(file_path)

    for message in archive:
        if message.get("id") == message_id:
            
            if models != "trash":
                save_data("models/trash.json", message)

            archive.remove(message)
            update_data(file_path, archive) 

            return {"message": "Message deleted successfully"}

    return {"message": "The ID has not been found."}   

def verify_models(model_param):
    """
    Brief: 
        Verifica si el archivo proporcionado es válido.
    Parametros:
        - model_param (str): El nombre del archivo a verificar.
    Retorno:
        El nombre del modelo si es válido, o el modelo por defecto 'inbox' si no es válido.
    """
    models = ["drafts","folders","important","inbox","sent","spam","starred","trash"]
    

    for model in models:
        if model_param == model:
            return model_param

    return models[3]

def verify_id(file_path: str, id: str):
    """
    Brief: 
        Verifica la existencia de un ID en el archivo proporcionado.
    Parametros:
        - file_path (str): La ruta del archivo que contiene los datos.
        - id (str): El ID a buscar en el archivo.
    Retorno:
        True si el ID no se encuentra, False si se encuentra.
    """
    archive = load_data(file_path)

    if isinstance(archive, list):

        for message in archive:
            if message.get("id") == id:
                return False
        
        return True








