from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.academy_routes import router as academy_router

app = FastAPI()

app.include_router(user_router)
app.include_router(academy_router)

@app.get("/")

def root():
    return "Hello World"