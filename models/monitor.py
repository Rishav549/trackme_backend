from db.db import Base
from sqlalchemy import ForeignKey, Integer,String,Column,DateTime,Boolean
import datetime

class MonitorModel(Base):
    __tablename__="monitor_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer,ForeignKey("employee_master.id"), nullable=False)
    Timestamp = Column(DateTime, nullable=False)
    lat = Column(String, nullable=False)
    lan = Column(String, nullable=False)
    tag_scanned = Column(String, nullable=False)