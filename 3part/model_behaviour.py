from pydantic import BaseModel , field_validator , model_validator , computed_field


class User(BaseModel):
    userName: str 
    
    @field_validator('userName') #runs before pydantic start or we can say its validate in the starting 
    def userName_length(cls , v):   #v hai userName bcz validating for it
        if len(v) < 4:
            raise ValueError("User must be atleast four characters")
        return v
    
    
class SignupData(BaseModel):
    # email: str
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def passwordMatch(cls , values):
        if values.password != values.confirm_password:
            raise ValueError("Password don not match")
        return values
    
class Product(BaseModel):
    price: float 
    quantity : int 
    
    @computed_field  #for computing something like after creating this things
    @property    
    def total_price(self) -> float:
        return self.price & self.quantity