class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_country(self):
        return self.__country

    def __str__(self):
        return f"{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code}, {self.__country}"
