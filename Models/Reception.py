from pydantic import BaseModel
from Doctor import Doctor
class Reception(BaseModel):
    first_name: str
    last_name: str
    doctor: Doctor