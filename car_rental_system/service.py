class Service:
    def __init__(self, service_id, name, description, cost):
        self.__id = service_id
        self.__name = name
        self.__description = description
        self.__cost = cost

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return f"{self.__name} - ${self.__cost}"
