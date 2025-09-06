import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from src.database import Base
from datetime import datetime

class MessageEntity(Base):
    __tablename__ = 'messages'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    chat_id = Column(String(36), ForeignKey('chats.id'))
    user_id = Column(String(36), ForeignKey('users.id'))
    content = Column(String(255))

    user = relationship("UserEntity")

    def __repr__(self): 
        return 