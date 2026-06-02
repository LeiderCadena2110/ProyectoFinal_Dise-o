from abc import ABC
from datetime import datetime
from .constants import VehicleStatus, CarType, VanType


class Vehicle(ABC):
    def __init__(self, license_number, stock_number, passenger_capacity, barcode,
                 has_sunroof, status, model, make, manufacturing_year, mileage):
        self.__license_number = license_number
        self.__stock_number = stock_number
        self.__passenger_capacity = passenger_capacity
        self.__barcode = barcode
        self.__has_sunroof = has_sunroof
        self.__status = status
        self.__model = model
        self.__make = make
        self.__manufacturing_year = manufacturing_year
        self.__mileage = mileage
        self.__log = []

    def get_license_number(self):
        return self.__license_number

    def get_barcode(self):
        return self.__barcode

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def get_mileage(self):
        return self.__mileage

    def get_manufacturing_year(self):
        return self.__manufacturing_year

    def get_log(self):
        return self.__log

    def add_log_entry(self, log_entry):
        self.__log.append(log_entry)

    def reserve_vehicle(self):
        if self.__status == VehicleStatus.AVAILABLE:
            self.__status = VehicleStatus.RESERVED
            return True
        return False

    def return_vehicle(self):
        self.__status = VehicleStatus.AVAILABLE

    def __str__(self):
        return f"[{self.__license_number}] {self.__make} {self.__model} ({self.__manufacturing_year})"


class Car(Vehicle):
    def __init__(self, license_number, stock_number, passenger_capacity, barcode,
                 has_sunroof, status, model, make, manufacturing_year, mileage, car_type):
        super().__init__(license_number, stock_number, passenger_capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = car_type

    def get_type(self):
        return self.__type


class Van(Vehicle):
    def __init__(self, license_number, stock_number, passenger_capacity, barcode,
                 has_sunroof, status, model, make, manufacturing_year, mileage, van_type):
        super().__init__(license_number, stock_number, passenger_capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = van_type

    def get_type(self):
        return self.__type


class Truck(Vehicle):
    def __init__(self, license_number, stock_number, passenger_capacity, barcode,
                 has_sunroof, status, model, make, manufacturing_year, mileage):
        super().__init__(license_number, stock_number, passenger_capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = "Truck"


class SUV(Vehicle):
    def __init__(self, license_number, stock_number, passenger_capacity, barcode,
                 has_sunroof, status, model, make, manufacturing_year, mileage):
        super().__init__(license_number, stock_number, passenger_capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = "SUV"


class Motorcycle(Vehicle):
    def __init__(self, license_number, stock_number, passenger_capacity, barcode,
                 has_sunroof, status, model, make, manufacturing_year, mileage):
        super().__init__(license_number, stock_number, passenger_capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = "Motorcycle"
