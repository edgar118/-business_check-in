# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends
from backend.core.config import engine, Base
from backend.routers import department
from backend.routers import user
from fastapi.middleware.cors import CORSMiddleware

prev = '/api/v1'
app = FastAPI()


origins = [
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes. Cambia esto a los orígenes específicos si es necesario
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.). Cambia según tus necesidades
    allow_headers=["*"],  # Permite todos los encabezados. Cambia según tus necesidades
)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    print("Running default data version scripts")

app.include_router(department.router, prefix=f"{prev}/department", tags=['deparment'])
app.include_router(user.router, prefix=f"{prev}/user", tags=['user'])