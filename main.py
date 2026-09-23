from fastapi import FastAPI
from routers.student_routes import router

app = FastAPI(title="Student CRUD API")

app.include_router(router)