class CarRentalLocation:
    def __init__(self, name, location_address):
        self.__name = name
        self.__location = location_address

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def __str__(self):
        return f"{self.__name} - {self.__location}"
