import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S"
class BaseModel:

    def __init__(self, **kwargs):
        """This method instantiates an object"""
        self.id = uuid.uuid4()
        self.create_at = datetime.utcnow()
        self.updated_at = self.create_at

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time)

                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, remove_password=True):
        """Returns a dictionary containing all keys/values of the instance."""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)
        if remove_password is True:
            new_dict.pop("password", None)
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""

    models.storage.delete(self)