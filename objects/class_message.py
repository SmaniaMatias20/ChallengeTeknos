from pydantic import BaseModel, Field

class Message(BaseModel):
    """
    Brief:
        Representa un mensaje con sus atributos específicos.
    Atributos:
        - id (str): Identificador único del mensaje.
        - from_user (dict): Información sobre el remitente.
        - to_user (list[dict]): Lista de destinatarios con su información.
        - subject (str): Asunto del mensaje.
        - body (str): Cuerpo del mensaje.
        - time (str): Fecha del mensaje.
        - read (bool): Indica si el mensaje ha sido leído.
        - starred (bool): Indica si el mensaje está marcado como destacado.
        - important (bool): Indica la importancia del mensaje.
        - has_attachments (bool): Indica si el mensaje tiene archivos adjuntos.
        - labels (list): Lista de etiquetas asociadas al mensaje.
    """
    id: str
    from_user: dict = Field(alias = "from") 
    to_user: list[dict] = Field(alias = "to")
    subject: str
    body: str
    time: str
    read: bool
    starred: bool
    important: bool
    has_attachments: bool
    labels: list


    
        