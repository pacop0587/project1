from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relatioship
from sqlalchemy.sql import func
from .user_model import User

from app.v1.utils.db import Base

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key = True)
    title = Column(String, index = True)
    created_at = Column(DateTime(Timezone = True), default = func.now())
    description = Column(String, index = True)
    is_done = Column(Boolean, default = False)
    user_id = Column(Integer, ForeignKey('user_id'))

    user = relatioship("User", back_populate = 'todos')