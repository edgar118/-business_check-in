from pydantic import BaseModel, root_validator
from datetime import datetime
from typing import Optional

class User(BaseModel):
    name: str 
    role: str
    document_id: int
    department_id: int
    user_type_id: int
    
    class Config:
        orm_mode = True

class UpdateUser(BaseModel):
    name: str 
    role: str
    department_id: int
    user_type_id: int
    
    class Config:
        orm_mode = True

class UserType(BaseModel):
    name: str

class EntryRegisterCreate(BaseModel):
    user_id: int
    time: datetime

    class Config:
        orm_mode = True

class EntryExitRegisterCreate(BaseModel):
    user_id: int
    time: datetime
    reason: Optional[str] = None
    
    class Config:
        orm_mode = True