from pydantic import BaseModel
from datetime import datetime

class Attendance(BaseModel):
    emp_id: str
    attn_date: datetime
    login_datestamp: datetime
    login_lat: str
    login_lan: str
    tag_scanned_in: str
    logout_datestamp: datetime
    logout_lat: str
    logout_lan: str
    tag_scanned_out: str

class Attendance_create(Attendance):
    pass

class Attendance_view(Attendance):
    id: int