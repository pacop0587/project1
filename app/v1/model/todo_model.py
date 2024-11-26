#TodoList Model
from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relatioship, Mapped, mapped_column
from sqlalchemy.sql import func
from .user_model import User
from datetime import datetime

from app.v1.utils.db import Base

class Todo(Base):
    __tablename__ = 'todos'

    # id = Column(Integer, primary_key = True)
    # title = Column(String, index = True)
    # created_at = Column(DateTime(Timezone = True), default = func.now())
    # description = Column(String, index = True)
    # is_done = Column(Boolean, default = False)
    # user_id = Column(Integer, ForeignKey('user_id'))

    # user = relatioship("User", back_populate = 'todos')

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(40))
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    description:Mapped[str] = mapped_column(String(100))
    is_done:Mapped[bool] = mapped_column(Boolean, default=False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))

