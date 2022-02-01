from calendar import MONDAY, SATURDAY
from datetime import datetime
from typing import Dict
from pydantic import BaseModel
from Weekdays import Weekdays

class Doctor(BaseModel):
    first_name: str
    last_name: str
    specialty: str
    address: str
    present_time: Dict[Weekdays,datetime]
