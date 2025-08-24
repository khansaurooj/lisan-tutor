# api/models/translation_history.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

class TranslationHistory(Base):
    __tablename__ = "translation_history"
    id              = Column(Integer, primary_key=True)
    original_text   = Column(Text)
    translated_text = Column(Text)
    source_lang     = Column(String(50))
    target_lang     = Column(String(50))
    user_id         = Column(Integer, ForeignKey("users.id"), nullable=False)

    # each history entry → exactly one user
    user = relationship("User", back_populates="translations")
