from Models.Doctor import Doctor 
from Models.Reception import Reception
from Models.Weekdays import Weekdays
from datetime import datetime

Doctor(id = "navid" , first_name = "navid" ,last_name= "filsaraee" ,specialty= "asd" ,address= "asd" ,present_time= ((Weekdays.FRI , datetime.today()),) ).save()

doc = Doctor.get("navid")

Reception(id = "asd " , first_name="asd" , last_name="asd",doctor=doc).save()

print(Reception.search_all('id' , 'asd '))
print(Doctor.search_all('last_name' , 'filsaraee'))