from datetime import datetime
from pydantic import BaseModel

class Doctor(BaseModel):
    first_name: str
    last_name: str
    specialty: str
    address: str
    present_time: datetime
