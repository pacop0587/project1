#User Model
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.v1.utils.db import Base

class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key = True)
    # email = Column(String, unique = True, index = True)
    # password = Column(String)
    # is_active = Column(Boolean, default = True)

    # todos = relationship("Todo", back_populates = True)
    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str]
    password:Mapped[str] = mapped_column(String(30))
    is_active:Mapped[bool] = mapped_column(Boolean, default=True)