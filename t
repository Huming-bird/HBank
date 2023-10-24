import uuid
from datetime import datetime
import random

time = "%Y-%m-%dT%H:%M:%S.%f"

class Account:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)


    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
    def create_account(self, acct_type):
        random_number = random.randint(0, 999999999)
        if acct_type == 'savings':
            ten_digit_number = '1' + str(random_number).zfill(9)
        elif acct_type == 'current':
            ten_digit_number = '0' + str(random_number).zfill(9)

        return ten_digit_number

class Customer(Account):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    acct_num = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if kwargs:
            if 'acct_type' in kwargs.keys():
                super().__init__(*args, **kwargs)
                self.acct_num = self.create_account(kwargs['acct_type'])
