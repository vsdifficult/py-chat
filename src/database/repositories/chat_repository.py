from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.entities.ChatEnitty import ChatEntity
from src.models.entities.MessageEntity import MessageEntity
from src.models.dto.ChatDto import ChatDto, MessageDto, MessageRegisterDto, ChatRegisterDto
from datetime import datetime 

import uuid 

class ChatRepository: 
    
    async def get_by_user_id(self, session: AsyncSession, user_id: uuid.uuid4) -> list[ChatDto]: 
        query = select(ChatEntity).where(ChatEntity.user_id == user_id)
        result = await session.execute(query)
        
        chats = result.scalars().all()
        
        return [ChatDto(chat.id, chat.user_id, chat.title, chat.created_at, chat.updated_at, chat.messages) for chat in chats]
        
    async def get_by_id(self, session: AsyncSession, chat_id: uuid.uuid4) -> list[ChatDto]: 
        query = select(ChatEntity).where(ChatEntity.id == chat_id)
        result = await session.execute(query)
        
        chats = result.scalars().all()
        
        return [ChatDto(chat.id, chat.user_id, chat.title, chat.created_at, chat.updated_at, chat.messages) for chat in chats]
    
    async def create(self, session: AsyncSession, dto: ChatRegisterDto) -> uuid.uuid4: 
        chat = ChatEntity(
            id = uuid.uuid4(), 
            user_id = dto.user_id, 
            title = dto.title, 
            created_at = datetime.now(), 
            updated_at = datetime.now()
        )
        session.add(chat)
        await session.commit()

        return chat.id 
    
    async def delete(self, session: AsyncSession, chat_id: uuid.uuid4) -> bool | None: 
        query = select(ChatEntity).where(ChatEntity.id == chat_id)
        result = await session.execute(query)
        chat = result.scalars().first()
        session.delete(chat)
        await session.commit()
        return True


class MessageRepository: 
    
    async def get_by_user_id(self, session: AsyncSession, user_id: uuid.uuid4) -> list[MessageDto]: 
        query = select(MessageEntity).where(MessageEntity.user_id == user_id)
        result = await session.execute(query)
        
        messages = result.scalars().all()
        
        return [MessageDto(message.id, message.user_id, message.content, message.chat_id) for message in messages]
        
    async def get_by_id(self, session: AsyncSession, chat_id: uuid.uuid4) -> list[MessageDto]: 
        query = select(MessageEntity).where(MessageEntity.id == chat_id)
        result = await session.execute(query)
        
        messages = result.scalars().all()
        
        return [MessageDto(message.id, message.user_id, message.content, message.chat_id) for message in messages]
    
    async def create(self, session: AsyncSession, dto: MessageRegisterDto) -> uuid.uuid4: 
        message = MessageEntity(
            id = uuid.uuid4(), 
            user_id = dto.user_id, 
            title = dto.title, 
            created_at = datetime.now(), 
            updated_at = datetime.now()
        )
        session.add(message)
        await session.commit()

        return message.id 
    
    async def delete(self, session: AsyncSession, chat_id: uuid.uuid4) -> bool | None: 
        query = select(MessageEntity).where(MessageEntity.id == chat_id)
        result = await session.execute(query)
        message = result.scalars().first()
        session.delete(message)
        await session.commit()
        return True
  