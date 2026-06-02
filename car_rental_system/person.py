class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return f"{self.__name}, {self.__email}"
