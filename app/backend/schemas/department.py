from pydantic import BaseModel
from typing import Optional

class Department(BaseModel):
    name: str 
    
    class Config:
        orm_mode = True