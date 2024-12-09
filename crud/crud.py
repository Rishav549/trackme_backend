from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.employee_master import UserModel
from schemas.employee_master import Employee_create
from schemas.attendance import Attendance_create
from models.attendance import AttendanceModel
from schemas.monitor import Monitor_create
from models.monitor import MonitorModel

async def post_employee_details(db: Session, data: Employee_create):
    post_employee_details = UserModel(**data.dict())
    db.add(post_employee_details)
    db.commit()
    db.refresh(post_employee_details)
    return post_employee_details

async def get_employee(skip:int, limit: int, db: Session):
    return db.query(UserModel).offset(skip).limit(limit).all()

async def post_attendance(db:Session, data: Attendance_create):
    post_attendance = AttendanceModel(**data.dict())
    db.add(post_attendance)
    db.commit()
    db.refresh(post_attendance)
    return post_attendance

async def get_attendance(skip:int, limit: int, db: Session):
    return db.query(AttendanceModel).offset(skip).limit(limit).all()

async def post_monitor(db:Session, data: Monitor_create):
    post_monitor = MonitorModel(**data.dict())
    db.add(post_monitor)
    db.commit()
    db.refresh(post_monitor)
    return post_monitor

async def get_monitor(skip:int, limit: int, db: Session):
    return db.query(MonitorModel).offset(skip).limit(limit).all()