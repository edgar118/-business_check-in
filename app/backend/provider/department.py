from backend.model.department import Department as DepartmentModel

class Department():
    def created(deparment, db):
        
        add_department = DepartmentModel(
            name = deparment.name,
        )

        db.add(add_department)
        db.commit()

        return {"message": f"Created {deparment.name}"}
