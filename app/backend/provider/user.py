from fastapi import HTTPException, status
from sqlalchemy import and_
from sqlalchemy import func
from datetime import time

from backend.model.user import User as UserModel
from backend.model.EntryExitRegister import EntryExitRegister
from backend.model.user_type import UserType
from backend.core.config import PersonType

class Employee():

    def user_exist_document(id, db):
        user_exist = db.query(UserModel).filter(UserModel.document_id == id).first()

        return user_exist
    
    def user_exist_id(id, db):
        user_exist = db.query(UserModel).filter(UserModel.id == id).first()

        return user_exist
    
    def created_user_type(type, db):
        
        db_item = UserType(**type.dict())
        db.add(db_item)
        db.commit()

        return {"message": f"Created {type.name}"}
    
    def created(employee, db):

        if Employee.user_exist_document(employee.document_id, db):
            raise HTTPException(status_code=404, detail="User already exist")
        
        db_item = UserModel(**employee.dict())

        db.add(db_item)
        db.commit()

        return {"message": f"Created {employee.name}"}
    
    def update(user, id, db):
                 
        if not Employee.user_exist_id(id, db) :
            raise HTTPException(status_code=404, detail="User not found")
        
        db_item = db.query(UserModel).filter(UserModel.id == id).update(user.dict(exclude_unset=True))
        db.commit()

        return {"message": f"update"}
    
    def delete(id, db):

        db_item = Employee.user_exist_id(id, db)            
        if not db_item:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(db_item)
        db.commit()
        
        return {"message": f"user delete"}
    
    def get_user(
            db, 
            start_date,
            end_date,
            user_type,
            department_id
        ):

        query = db.query(UserModel)

        conditions = []
        if start_date:
            conditions.append(UserModel.created_at >= start_date)
        if end_date:
            conditions.append(UserModel.created_at <= end_date)
        if user_type:
            query = query.join(UserType)
            conditions.append(UserType.id == user_type)
        if department_id:
            conditions.append(UserModel.department_id == department_id)

        if conditions:
            query = query.filter(and_(*conditions))

        users = query.all()

        if not users:
            raise HTTPException(status_code=404, detail="User not found")

        return users 

    def register_entry_time(entry_date, db):

        employee = db.query(UserModel).filter(UserModel.id == entry_date.user_id).first()

        if not employee:
            raise HTTPException(status_code=404, detail="User not found")

        db_entry_exit = EntryExitRegister(
            user_id=entry_date.user_id,
            entry_time=entry_date.time,
            person_type=employee.user_type.name,
        )

        db.add(db_entry_exit)
        db.commit()
        db.refresh(db_entry_exit)
        
        return {"message": f"add entry {entry_date.time}"}

    def register_exit_time(entry_date, db):

        external = db.query(UserModel).filter(UserModel.id == entry_date.user_id).first()
        if not external:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        db_exit_date = db.query(EntryExitRegister).filter(
            and_(
                EntryExitRegister.user_id == entry_date.user_id,
                EntryExitRegister.exit_time==None
            )).first()
        
        time_only = entry_date.time
        if time_only.time() < time(16, 0):
            if entry_date.reason not in ["Cita médica", "Calamidad", "Diligencia personal"]:
                raise HTTPException(status_code=400, detail="Invalid reason. Must be one of: Cita médica, Calamidad, Diligencia personal.")
            db_exit_date.reason = entry_date.reason
    
        if db_exit_date is None:
            raise HTTPException(status_code=400, detail="user need entry time")
        
        if db_exit_date:
            db_exit_date.exit_time = entry_date.time
            db_exit_date.is_archived = True
            db.commit()
        else:
            db_exit_date = EntryExitRegister(
                user_id=entry_date.user_id,
                exit_time=entry_date.time,
                person_type=str(PersonType.EMPLOYEE),
            )
            db.add(db_exit_date)
            db.commit()
            

        return {"message": f"add exit {entry_date.time}"}
    
    def calcule_time(id, db):
        records = db.query(EntryExitRegister).filter(
            EntryExitRegister.user_id == id,
        ).count()             

        total = 0

        records = db.query(EntryExitRegister).filter(
            EntryExitRegister.user_id == id
            ).all()
        
        for x in records:
            entry = x.entry_time
            exit = x.exit_time
            diferencia = exit - entry

            total += diferencia.total_seconds() / 3600
            
        return {"message": f"hours worked {total}"}      
    
    def count_in_company(db):
        records = db.query(EntryExitRegister).filter(
            EntryExitRegister.exit_time == None,
        ).count()

        return {"message": f"total employed in company {records}"}
