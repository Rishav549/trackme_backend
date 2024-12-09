from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from fastapi.responses import JSONResponse
from datetime import datetime
from schemas.attendance import Attendance_create, Attendance_view
from crud.crud import post_attendance

router = APIRouter()

@router.post("/attendance/")
async def post_att(data: Attendance_create, db: Session = Depends(get_db)):
    try:
        result = await post_attendance(db=db, data=data)
        return result
    except HTTPException as e:
        print(e)
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)