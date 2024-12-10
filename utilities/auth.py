from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from models.employee_master import UserModel
from db.db import get_db
from utilities.crypt import decode_token, get_password_hash,verify_password
from sqlalchemy.future import select

def get_user_by_email (db: Session, email: str):
    return db.execute(select(UserModel).filter(UserModel.emp_email == email)).scalar()

def authenticate_user(db: Session, email:str, password: str):
    user= get_user_by_email(db,email)
    if not user or not verify_password(password, user.password):
        return False
    return user

def create_user(db: Session,user:dict):
    # Create Password Hash
    hashed_password = get_password_hash(user["password"])

    # Add the password hash to the user object
    user["password"]=hashed_password

    # Create a user Model
    db_user = UserModel(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_current_user_refresh(token: str,db: Session = Depends(get_db))-> UserModel:
    token_data = decode_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Authorization"},
        )
    if token_data.token_type == "access":
        raise HTTPException(
            status_code=401,
            detail="Invalid Token Type",
            headers={"WWW-Authenticate": "Authorization"},
        )
    user = db.get(UserModel,token_data.id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Authorization"},
        )
    return user