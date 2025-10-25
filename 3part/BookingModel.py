from pydantic import BaseModel , field_validator , model_validator , computed_field


class Booking(BaseModel):
    user_id : int 
    room_id : int 
    night : int 
    rate_per_night: float
    
    
    @model_validator(mode="after")
    def rooms_booked(cls,values):
        if values.night < 1:
            raise ValueError("Atleast  book one room .");
        return f"rooms booked{values.night}"
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.night * self.rate_per_night