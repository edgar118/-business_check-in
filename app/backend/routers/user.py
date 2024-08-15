from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from backend.schemas.user import User as UserSchema
from backend.schemas.user import UserCreated
from backend.schemas.user import UpdateUser
from backend.schemas.user import EntryExitRegisterCreate, UserType, EntryRegisterCreate
from backend.provider.user import Employee
from backend.core.config import get_db


router = APIRouter()

@router.post('/type')
def user_type(
   usertype: UserType,
   db:Session=Depends(get_db),

):  
    return Employee.created_user_type(usertype, db)


@router.post('/')
def create(
   user: UserCreated,
   db:Session=Depends(get_db),

):  
    return Employee.created(user, db)

@router.put('/{id}')
def update(
   user: UpdateUser,
   id:int,
   db:Session=Depends(get_db),

):  
    return Employee.update(user, id, db)


@router.delete('/{id}')
def delete(
   id:int,
   db:Session=Depends(get_db),

):  
    return Employee.delete(id, db)

@router.get('/', response_model=List[UserSchema])
def get_user(
    start_date: Optional[datetime] = Query(None, description="Filter by start date"),
    end_date: Optional[datetime] = Query(None, description="Filter by end date"),
    user_type: Optional[int] = Query(None, description="Filter by user type"),
    department_id: Optional[int] = Query(None, description="Filter by department ID"),
    db: Session = Depends(get_db),
):
    return Employee.get_user(
        db, 
        start_date,
        end_date,
        user_type,
        department_id
    )

@router.get('/type')
def get_user_type(
    db:Session=Depends(get_db)

):  
    return Employee.get_user_type(
            db
    )

@router.post("/entry")
def register_entry_time(
    entry_date: EntryRegisterCreate,
    db: Session = Depends(get_db)
    ):
    return Employee.register_entry_time(entry_date, db)

@router.post("/exit")
def register_exit_time(
    exit_date: EntryExitRegisterCreate,
    db: Session = Depends(get_db)
    ):
    return Employee.register_exit_time(exit_date, db)

@router.get("/check_in", response_model=List[UserSchema])
def check_in(
    db: Session = Depends(get_db)
    ):
    return Employee.check_in(db)

@router.get("/calculate/{id}")
def register_entry_time(
    id: int,
    db: Session = Depends(get_db)
    ):
    return Employee.calcule_time(id, db)

@router.get("/count_in_company")
def count_in_company(
    db: Session = Depends(get_db)
    ):
    return Employee.count_in_company(db)