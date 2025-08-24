# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker, declarative_base
# #D:\lisan-tutor\api\database.py
# DB_USER = "root"
# DB_PASSWORD = "urooj#123"
# DB_HOST = "localhost"
# DB_NAME = "lisan_db"  # ✅ choose your preferred name

# # Step 1: Connect to MySQL without specifying a database
# temp_engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306")

# # Step 2: Create the database if it doesn't exist
# with temp_engine.connect() as conn:
#     conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
#     conn.commit()

# # Step 3: Now connect to the newly created database
# DB_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
# engine = create_engine(DB_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()




from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session
from contextlib import contextmanager

# Database configuration
DB_USER = "root"
DB_PASSWORD = "urooj#123"
DB_HOST = "localhost"
DB_NAME = "lisan_db"

# Step 1: Connect to MySQL without specifying a database
temp_engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306")

# Step 2: Create the database if it doesn't exist
with temp_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    conn.commit()

# Step 3: Now connect to the newly created database
DB_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# ✅ ADD THIS FUNCTION to provide a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
