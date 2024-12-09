from pydantic import BaseModel

class Employee(BaseModel):
    emp_code: str
    scan_code: str
    mac_id: str
    emp_name: str
    emp_email: str
    emp_phone: str
    emp_designation: str
    emp_picture: str
    tagged_imei: str
    password: str

class Employee_create(Employee):
    pass

class Employee_view(Employee):
    id: int


class Login(BaseModel):
    emp_email: str
    password: str

class RefreshToken(BaseModel):
    refresh_token: str
    
class TokenData(BaseModel):
    id: int
    email: str
    token_type: str