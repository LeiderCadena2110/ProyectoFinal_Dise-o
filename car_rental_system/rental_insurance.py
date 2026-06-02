class RentalInsurance:
    def __init__(self, insurance_id, name, description, daily_cost, coverage_details):
        self.__id = insurance_id
        self.__name = name
        self.__description = description
        self.__daily_cost = daily_cost
        self.__coverage_details = coverage_details

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_daily_cost(self):
        return self.__daily_cost

    def get_coverage_details(self):
        return self.__coverage_details

    def __str__(self):
        return f"{self.__name} - ${self.__daily_cost}/day"
