import re
from mongoengine.errors import ValidationError

class Validation:
    """
        Class Validation provide support for data validation
    """
    def __init__(self):
        """
            Descritpion
            ***********
                Most important data for validating data are described during the object creation
        """
        self.email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        self.option = ["bowler", "bating"]
        self.phone_num_pattern = r"^[6-9]\d{9}$"

    def email_valid(self, mail):
        """
        Description:
        ************
            Check for the valid email ID by using regex pattern
            returns True or False as result

            params:
            *******
                mail - it get the string data
        """
        
        return re.match( self.email_pattern, mail)
   
    def type_valid(self, type):
        """
        Description:
        ************
            Check for the valid type that is available on the option
            returns True or False as result
            params:
            ******
                type - it get the string data
        """
        type = type.lower()
        if type in self.option:
            return True 
        else:
            return False
    
    def phone_number_valid(self, number):
        """
        Description:
        ************
            check for the valid phone number by using regex pattern (india phone)
            returns True or False as result

            params:
            *******
                number - it get the string numeric data
        """
        return re.match(self.phone_num_pattern, number)

    def age_valid(self, age):
        """
        Description:
        ************
            check for the valid age

            params:
            *******
                age - it get the numeric data
        """

        return age > 0
   

class Player_Validation(Validation):

    def __init__(self):
        super().__init__()    
    
    def phone_number_valid(self, number):
        if not super().phone_number_valid(str(number)):
            raise ValidationError(message="invalid phone number")
    
    def email_valid(self, mail):
        if not super().email_valid(mail):
            raise ValidationError(message="invalid email id")

    def type_valid(self, type):
        if not super().type_valid(type):
            raise ValidationError(message="invalid type")

    def age_valid(self, age):
        if not super().age_valid(age):
            raise ValidationError(message="invalid age")
