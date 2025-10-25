from fastapi import FastAPI , Depends
from pydantic import BaseModel , EmailStr

app = FastAPI()

class User(BaseModel):
    id : int 
    name : str 
    email : EmailStr
    password : str
    

class Settings(BaseModel):
    app_name: str = "Stackashu"
    admin_email = str = "Admin@google.com"
    
    
def get_settings():
    return Settings



@app.post('/signup')
def signup(user: User):
    return {'message' , f'user { user.name} signed up'}
    
@app.get('/settings')
def get_settings_endpoint(settings : Settings = Depends(get_settings)):
    return settings