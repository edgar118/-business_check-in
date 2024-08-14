from pydantic import BaseModel, root_validator
from datetime import datetime
from typing import Optional, List


class EntryExitRegisterSchema(BaseModel):
    id: Optional[int] = None
    person_type: Optional[str] = None
    entry_time: Optional[datetime] = None
    exit_time: Optional[datetime] = None
    user_id: Optional[int] = None
    is_archived: Optional[bool] = None
    reason: Optional[str] = None

class User(BaseModel):
    name: str 
    role: str
    document_id: int
    department_id: int
    user_type_id: int

    entry_exit_register: List[Optional[EntryExitRegisterSchema]] = []
    
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