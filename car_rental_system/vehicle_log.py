from datetime import datetime
from .constants import VehicleLogType


class VehicleLog:
    def __init__(self, log_id, log_type, description, creation_date=None):
        self.__id = log_id
        self.__type = log_type
        self.__description = description
        self.__creation_date = creation_date if creation_date else datetime.now()

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

    def get_creation_date(self):
        return self.__creation_date

    def update(self, description=None, log_type=None):
        if description:
            self.__description = description
        if log_type:
            self.__type = log_type

    def __str__(self):
        return f"[{self.__creation_date.strftime('%Y-%m-%d %H:%M')}] {self.__type.name}: {self.__description}"
