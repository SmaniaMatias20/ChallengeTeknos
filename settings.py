import json

def load_data(file_path):
    try:
        with open(file_path, "r", encoding="UTF8") as archive:
            data = json.load(archive)
        return data.get("data", [])
    except json.decoder.JSONDecodeError:
        message = "Error al decodificar el archivo JSON."
        return message
    except FileNotFoundError:
        message = "El archivo no fue encontrado."
        return message
    except Exception:
        message = "Otro error inesperado."
        return message

def save_data(file_path, data):
    with open(file_path, "a", encoding="UTF8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii = False)

def update_data(file_path, data):
    with open(file_path, "w", encoding="UTF8") as archivo:
        json.dump(data, archivo, indent = 4) 


def filter_messages(file_path = "", from_user = "", to_user = "", subject = ""):
    archive = load_data(file_path)
    
    if isinstance(archive, list):
        filtered_messages = []

        for message in archive:
            from_match = from_user == "" or (message.get("from") and from_user in message["from"]["name"])
            to_match = to_user == "" or any(recipient["name"] == to_user for recipient in message.get("to", []))
            subject_match = subject == "" or (message.get("subject") and subject in message["subject"])

            if from_match and to_match and subject_match:
                filtered_messages.append(message)

        return filtered_messages

def delete_message(file_path, message_id):
    archive = load_data(file_path)
    print("hola")
    for message in archive:
        if message.get("id") == message_id:
            
            save_data("models/starred.json", message)

            # Antes de eliminar hacer un append a starred
            archive.remove(message)

            # Sobreescribir inbox
            update_data("models/inbox.json", archive)


            return {"message": "Message deleted successfully"}
    

def comparate_models(model_param):
    models = ["drafts","folders","important","inbox","sent","spam","starred","trash"]
    count = 0

    for model in models:
        if model_param == model:
            count += 1

    if count == 0:
        model_param = "inbox"
    
    return model_param






