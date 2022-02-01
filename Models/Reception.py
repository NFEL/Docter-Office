from uuid import uuid4
from pydantic import Field

from .Doctor import Doctor
from .FileDataSaver import DatabaseBaseModel

class Reception(DatabaseBaseModel):
    id : str 
    first_name: str
    last_name: str
    doctor: Doctor