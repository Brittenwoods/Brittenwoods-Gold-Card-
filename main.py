
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Brittenwoods Gold Backend")
app.include_router(router)
