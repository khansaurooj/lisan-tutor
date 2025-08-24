# api/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base

class User(Base):
    __tablename__ = "users"
    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    # one user → many translations
    translations = relationship(
        "TranslationHistory",
        back_populates="user",
        cascade="all, delete-orphan"
    )
