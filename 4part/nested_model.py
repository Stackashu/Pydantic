from pickletools import optimize
from typing import List , Optional
from pydantic import BaseModel 


class Address(BaseModel):
    street : str
    city: str
    postal_code : str 
    

class User(BaseModel):
    id: int 
    name : str
    address : Address
    

class Comment(BaseModel):
    id: int
    content : str 
    replies : Optional[List['Comment']] = None   #this is called forward referencing
    

Comment.model_rebuild() #alwarys do this whenever using forward Referencing


address = Address(
    street = "123 something",
    city = "Delhi",
    postal_code = "1001"
)

user = User(
    id = 1 ,
    name = "Ashish Verma",
    address = address
)

comment = Comment(
    id = 1,
    content = "hi Ashish",
    replies = [
        Comment(id = 2 , content = "hi Stack" ),
        Comment(id = 3 , content = "hi Stack" )
    ]
)