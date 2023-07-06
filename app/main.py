from fastapi import FastAPI

from . import models
from .database import engine

from .routers import user, auth

# Hardcode - every time empty db will be created (if it doesn't exist) --> add migration
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Salary Checker"
)

app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return 'Sus'

