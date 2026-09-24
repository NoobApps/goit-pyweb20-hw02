from datetime import datetime
from abc import abstractmethod, ABC

class Field(ABC):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    @abstractmethod
    def value(self, value):
        self.value=self.value

class Name(Field):
    def __init__(self,value):
        if len(value) !=0:
            super().__init__(value)
        else:
            raise ValueError ("Name cannot be empty")

    def value(self, value):
        return self.value
		
class Phone(Field):
    def __init__(self, value:str) -> None :
        if len(value)==10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone number must be 10 digits like:0671234567")

    def value(self, value):
        return super().value(value)

class Birthday(Field):
    def __init__(self, value: str):
        try:
            if self.__is_valid(value):
                self.value = value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __is_valid(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def value(self, value):
        return super().value(value)
    

# bd=Birthday("16.09.2012")
# print (type(bd))
