from json import load
with open("/home/deck/Desktop/defently-not-a-name-at-all-im-sirious/bleblah.json")as f:
   meh = load(f)

print(meh)
from enum import Enum
class Gender(Enum):
    MALE = "man"
    FEMALE = "WOman"
    UNKNOWN = "unknown"
    ALIEN = "alien"

from pydantic import BaseModel
class Mwahaha(BaseModel):
    name:str
    age:int
    gender:Gender

heerheer = Mwahaha(**meh)
print (heerheer)
print(heerheer.age)
