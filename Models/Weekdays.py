from enum import Enum
class Weekdays(Enum):
    SAT = "Saturday"
    SUN = "Sunday"
    MON = "Monday"
    TEU = "Teusday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"

    def __hash__(self) :
        return hash(self.value)
