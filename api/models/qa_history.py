from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from api.database import Base

class QAHistory(Base):
    __tablename__ = "qa_history"

    id         = Column(Integer, primary_key=True, index=True)
    question   = Column(Text, nullable=False)
    answer     = Column(Text, nullable=False)
    asked_at   = Column(DateTime(timezone=True), server_default=func.now())
