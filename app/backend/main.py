# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends
from backend.core.config import engine, Base
from backend.routers import department
from backend.routers import user

app = FastAPI()
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    print("Running default data version scripts")

app.include_router(department.router, prefix="/department", tags=['deparment'])
app.include_router(user.router, prefix="/user", tags=['user'])