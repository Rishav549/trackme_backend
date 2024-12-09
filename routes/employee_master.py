from fastapi import APIRouter,Depends, Request, status, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from utilities.auth import authenticate_user, get_user_by_email, create_user
from utilities.crypt import create_access_token,create_refresh_token, decode_token
from schemas.employee_master import Employee_create, Employee_view, Login
from crud.crud import post_employee_details
from db.db import get_db
import uuid
import os
router =APIRouter()

UPLOAD_DIRECTORY = "./uploaded_images/employees"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

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
async def register_user(
    emp_code: str = Form(...),
    scan_code: str = Form(...),
    mac_id: str = Form(...),
    emp_name: str = Form(...),
    emp_email: str = Form(...),
    emp_phone: str = Form(...),
    emp_designation: str = Form(...),
    tagged_imei: str = Form(...),
    password: str = Form(...),
    emp_picture: UploadFile = File(...),
    db: Session = Depends(get_db)): 

    unique_filename = f"{uuid.uuid4()}.png"
    image_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)
    with open(image_path, "wb") as buffer:
        buffer.write(await emp_picture.read())
    
    user_data = {
        "emp_code": emp_code,
        "scan_code": scan_code,
        "mac_id": mac_id,
        "emp_name": emp_name,
        "emp_email": emp_email,
        "emp_phone": emp_phone,
        "emp_designation": emp_designation,
        "tagged_imei": tagged_imei,
        "password": password,
        "emp_picture": image_path  # Storing the uploaded image path
    }

    # Validate Request Body

    if not user_data["emp_email"] or not user_data["password"] or not user_data["emp_name"]:
        raise HTTPException(status_code=400, detail="Please Enter A Valid Json Body")

    try:
        db_user = get_user_by_email(db, user_data["emp_email"])
        if db_user:
            return JSONResponse(status_code=400, content="User already registered")
    except Exception as e:
        return JSONResponse({"detail":e},status_code=400)
    create_user(db, user_data)
    return JSONResponse({"detail":"User Created"},status_code=201)