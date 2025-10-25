from typing import List , Optional
from pydantic import BaseModel



class Lesson(BaseModel):
    lesson_id : int 
    topic : str 
    
    
class Module(BaseModel):
    id : int 
    name : str
    price : float 
    lessons : List[Lesson]
    
class Course(BaseModel):
    id:int 
    name : str
    price : float 
    modules : List[Module]
    
    