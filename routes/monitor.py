from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from fastapi.responses import JSONResponse
from datetime import datetime
from schemas.monitor import Monitor_create, Monitor_view
from crud.crud import post_monitor, get_monitor

router = APIRouter()

@router.post("/monitor/")
async def post_mon(data: Monitor_create, db: Session = Depends(get_db)):
    try:
        result = await post_monitor(db=db, data=data)
        return result
    except HTTPException as e:
        print(e)
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)

@router.get("/monitor/get")
async def get_data(skip: int= 1, limit: int =10, db: Session =Depends(get_db)):
    get_data = await get_monitor(db=db, skip=skip, limit=limit)
    return get_data