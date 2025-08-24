# # D:/lisan-tutor/api/models/transcript.py
# from sqlalchemy import Column, Integer, Text
# from api.database import Base

# class Transcript(Base):
#     __tablename__ = "transcripts"
#     id = Column(Integer, primary_key=True, index=True)
#     original_text = Column(Text)
#     translated_text = Column(Text, nullable=True)  # ❗ THIS LINE MUST EXIST


from sqlalchemy import Column, Integer, Text
from api.database import Base

class Transcript(Base):
    __tablename__ = "transcripts"
    id             = Column(Integer, primary_key=True, index=True)
    original_text  = Column(Text, nullable=False)
    translated_text = Column(Text, nullable=True)
    # … any other fields you have …
