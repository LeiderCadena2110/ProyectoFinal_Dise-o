from abc import ABC
from .constants import AccountStatus


class Account(ABC):
    def __init__(self, account_id, password, person, status=AccountStatus.ACTIVE):
        self.__id = account_id
        self.__password = password
        self.__status = status
        self.__person = person

    def get_id(self):
        return self.__id

    def get_person(self):
        return self.__person

    def get_status(self):
        return self.__status

    def reset_password(self, new_password):
        self.__password = new_password


class Member(Account):
    def __init__(self, account_id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(account_id, password, person, status)
        self.__total_vehicles_reserved = 0
        self.__reservations = []

    def get_total_vehicles_reserved(self):
        return self.__total_vehicles_reserved

    def get_reservations(self):
        return self.__reservations

    def add_reservation(self, reservation):
        self.__reservations.append(reservation)
        self.__total_vehicles_reserved += 1


class Receptionist(Account):
    def __init__(self, account_id, password, person, date_joined, status=AccountStatus.ACTIVE):
        super().__init__(account_id, password, person, status)
        self.__date_joined = date_joined

    def search_member(self, name, members):
        results = [m for m in members if name.lower() in m.get_person().get_name().lower()]
        return results


class AdditionalDriver:
    def __init__(self, driver_id, person):
        self.__driver_id = driver_id
        self.__person = person

    def get_driver_id(self):
        return self.__driver_id

    def get_person(self):
        return self.__person
