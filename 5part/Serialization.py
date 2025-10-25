from pydantic import BaseModel, ConfigDict 
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str 
    zip_code : str 
    
class User(BaseModel):
    id : int 
    name : str 
    email : str 
    is_active : bool = True 
    createdAt : datetime
    address : Address
    tags : List[str] = []
    
    model_config = ConfigDict(
        json_encoders = {datetime: lambda v : v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    
    
user = User(
    id = 1 , 
    name = "Ashish",
    email = "Ashish@gmail.com",
    is_active=True,
    createdAt= datetime(2024,3,15,14,30),
    address = Address( street ="aman salon" , city = "faridabad" , zip_code="121013"),
    tags = ["premium","subscriber"]
)



#Using model_dump() -> dict

python_dict = user.model_dump()
print(python_dict)


#using model_dump_json

json_str = user.model_dump_json()
print(json_str)