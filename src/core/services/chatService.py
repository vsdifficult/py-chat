import uuid
import bcrypt
import jwt
import random
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.repositories.chat_repository import ChatRepository
from src.models.dto.ChatDto import ChatDto, MessageDto, MessageRegisterDto, ChatRegisterDto

class ChatService: 
    def __init__(self):
        self.repo = ChatRepository()
    
    
