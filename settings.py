import json

def load_data(file_path):
    try:
        with open(file_path, "r", encoding="UTF8") as archive:
            data = json.load(archive)
        return data.get("data", [])
    except json.decoder.JSONDecodeError:
        return "Error decoding the JSON file."
    except FileNotFoundError:
        return "File not found."
    except Exception:
        return "Another unexpected error."

def save_data(file_path, data): 
    with open(file_path, "r", encoding="UTF8") as archivo:
        archive = json.load(archivo)

    archive["data"].append(data)
    new_archive = archive.get("data", [])

    for data in new_archive:
        new_id = data.get("id")

    result = verify_id(file_path, new_id)

    # Si result es False
    if result:
        update_data(file_path, new_archive)
        return {"message": "Message created successfully"}
    else:
        return {"message": "The id already exists"}




def update_data(file_path, archive):
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


def filter_messages(file_path = "", from_user = "", to_user = "", subject = ""):
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
            # from_match = from_user == "" or (message.get("from") and from_user in message["from"]["name"])
            # subject_match = subject == "" or (message.get("subject") and subject in message["subject"])

            if from_match and to_match and subject_match:
                filtered_messages.append(message)

        return filtered_messages

def delete_message(file_path, models, message_id):
    archive = load_data(file_path)

    for message in archive:
        if message.get("id") == message_id:
            
            if models != "starred":
                save_data("models/starred.json", message)

            archive.remove(message)

            update_data(f"models/{models}.json", archive)


            return {"message": "Message deleted successfully"}

    return {"message": "The ID has not been found."}   

def verify_models(model_param):
    models = ["drafts","folders","important","inbox","sent","spam","starred","trash"]
    

    for model in models:
        if model_param == model:
            return model_param

    return "inbox"

def verify_id(file_path, id):
    archive = load_data(file_path)

    if isinstance(archive, list):

        for message in archive:
            if message.get("id") == id:
                return False
        
        return True








