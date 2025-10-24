from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool 
    

class Product(BaseModel):
    id:int 
    name:str 
    price: float 
    in_stock : bool = True 


input_data = {'id':101, 'name':"stackashu","is_active":True}

user = User(**input_data)
print(user)