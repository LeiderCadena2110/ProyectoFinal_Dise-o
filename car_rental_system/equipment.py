class Equipment:
    def __init__(self, equipment_id, name, description, daily_cost):
        self.__id = equipment_id
        self.__name = name
        self.__description = description
        self.__daily_cost = daily_cost

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_daily_cost(self):
        return self.__daily_cost

    def __str__(self):
        return f"{self.__name} - ${self.__daily_cost}/day"
