
#****************************************************************************
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from api.database import Base, engine

# Routers
from api.routes import asr, translation, tts, qa, video

# DB setup
from api.database import SessionLocal, engine, Base
from api import models

# Create DB tables
# In Python shell or script

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# App initialization
app = FastAPI(
    title="Lisan Tutor",
    description="Audio ➔ Text ➔ Translation ➔ Audio ➔ QA ➔ Video pipeline",
    version="1.0.0"
)

# CORS (for frontend-backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (JS, CSS, images)
# app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
# 
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Setup Jinja2 for index.html
templates = Jinja2Templates(directory="frontend")

# Include API routers
app.include_router(asr.router)
app.include_router(translation.router)

app.include_router(tts.router)
app.include_router(qa.router)
app.include_router(video.router)

# Serve frontend index.html on root
@app.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Database connection test
@app.get("/db-test")
def test_db():
    db = SessionLocal()
    try:
        db.execute("SELECT 1")
        return {"status": "Connected to DB!"}
    except Exception as e:
        return {"error": str(e)}
    finally:
         db.close()



