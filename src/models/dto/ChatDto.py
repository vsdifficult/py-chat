from pydantic import BaseModel
import uuid 
from datetime import datetime 

class ChatRegisterDto(BaseModel):
    user_id: uuid.UUID
    title: str

class ChatDto(BaseModel): 
    chat_id: uuid.UUID
    user_id: uuid.UUID
    title: str  
    messages: list 
    created_at: datetime.utcnow
    updated_at: datetime.utcnow

class MessageRegisterDto(BaseModel):
    chat_id: uuid.UUID
    user_id: uuid.UUID
    text: str

class MessageDto(BaseModel):
    message_id: uuid.UUID
    chat_id: uuid.UUID
    user_id: uuid.UUID
    content: str