from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean
import datetime

class AttendanceModel(Base):
    __tablename__="attendance_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer,ForeignKey("employee_master.id"), nullable=False)
    attn_date = Column(DateTime, nullable=False)
    login_datestamp = Column(DateTime, nullable=False)
    login_lat = Column(String, nullable=False)
    login_lan = Column(String, nullable=False)
    tag_scanned_in = Column(String, nullable=False)
    logout_datestamp = Column(DateTime, nullable=False)
    logout_lat = Column(String, nullable=False)
    logout_lan = Column(String, nullable=False)
    tag_scanned_out = Column(String, nullable=False)