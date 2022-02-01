from datetime import datetime
from typing import Dict, Tuple
from .Weekdays import Weekdays
from .FileDataSaver import DatabaseBaseModel

from collections import namedtuple

# VisitDays = namedtuple('VisitDays' , ['Day', 'date'])

class Doctor(DatabaseBaseModel):
    first_name: str
    last_name: str
    specialty: str
    address: str
    present_time: Tuple[Tuple[Weekdays,datetime]]

