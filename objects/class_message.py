from pydantic import BaseModel

class Message(BaseModel):
    id: str
    from_user: dict
    to_user: list[dict]
    subject: str
    body: str
    time: str
    read: bool
    starred: bool
    important: bool
    has_attachments: bool
    labels: list

    
        