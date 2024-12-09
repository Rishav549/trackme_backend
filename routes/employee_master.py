from fastapi import APIRouter,Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from utilities.auth import authenticate_user, get_user_by_email, create_user
from utilities.crypt import create_access_token,create_refresh_token, decode_token
from schemas.employee_master import Employee_create, Employee_view, Login
from crud.crud import post_employee_details
from db.db import get_db
router =APIRouter()

@router.post("/auth/login/")
async def login(form_data: Login,db: Session= Depends(get_db)):
    user = authenticate_user(db, form_data.emp_email, form_data.password)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token=create_access_token(data={"id": user.id,"emp_email": user.emp_email,"tagged_imei": user.tagged_imei})
    refresh_token=create_refresh_token(data={"id": user.id,"emp_email": user.emp_email,"tagged_imei": user.tagged_imei})
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token, "name":user.emp_name,"email":user.emp_email}

@router.post("/auth/register/")
async def register_user(request: Employee_create,db: Session = Depends(get_db)): 
    user_data = request.dict()

    # Validate Request Body

    if "emp_email" not in user_data or "password" not in user_data or "emp_name" not in user_data:
        return JSONResponse(status_code=400, content="Please Enter A Valid Json Body")

    try:
        db_user = get_user_by_email(db, user_data["emp_email"])
        if db_user:
            return JSONResponse(status_code=400, content="User already registered")
    except Exception as e:
        return JSONResponse({"detail":e},status_code=400)
    create_user(db, user_data)
    return JSONResponse(content={"detail":"User Created"},status_code=201)