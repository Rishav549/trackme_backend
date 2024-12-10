from pydantic import BaseModel
from datetime import datetime

class Monitor(BaseModel):
    emp_id: int
    Timestamp: datetime
    lat: str
    lan: str
    tag_scanned: str

class Monitor_create(Monitor):
    pass

class Monitor_view(Monitor):
    id: int
