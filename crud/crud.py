from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.employee_master import UserModel
from schemas.employee_master import Employee_create

async def post_employee_details(db: Session, data: Employee_create):
    post_employee_details = UserModel(**data.dict())
    db.add(post_employee_details)
    db.commit()
    db.refresh(post_employee_details)
    return post_employee_details