from pydantic import EmailStr, BaseModel


class Users(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class registration_form(Users):
    pass


class registration_response(BaseModel):
    user_id: str

#get 
class get_user_info_response(Users):
    pass #I do not need to add anything to Users
    
#This was wrong. Because this was for the register 
#user enpoint which is sending information with the Users 
#inherited?
#class get_user_info(Users):
#    pass
    