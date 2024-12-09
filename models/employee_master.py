from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean
import datetime

class UserModel(Base):
    __tablename__ = "employee_master"

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_code = Column(String, nullable=False)
    scan_code = Column(String, nullable=False)
    mac_id = Column(String, nullable=False)
    emp_name = Column(String, nullable=False)
    emp_email = Column(String, nullable=False)
    emp_phone = Column(String, nullable=False)
    emp_designation = Column(String, nullable=False)
    emp_picture = Column(String, nullable=False)
    tagged_imei = Column(String, nullable=False)
    password = Column(String, nullable=False)

