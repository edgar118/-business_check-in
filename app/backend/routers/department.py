from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schemas.department import Department  as DeparmentSchema
from backend.provider.department import Department
from backend.core.config import get_db


router = APIRouter()

@router.post('/')
def create(
   deparment: DeparmentSchema,
   db:Session=Depends(get_db),

):  
    return Department.created(deparment, db)
     