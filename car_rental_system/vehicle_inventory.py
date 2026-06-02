from abc import ABC


class Search(ABC):
    def search_by_type(self, vehicle_type):
        pass

    def search_by_model(self, model):
        pass

    def search_by_make(self, make):
        pass


class VehicleInventory(Search):
    def __init__(self):
        self.__vehicle_types = {}
        self.__vehicle_models = {}
        self.__vehicle_makes = {}
        self.__all_vehicles = []

    def add_vehicle(self, vehicle):
        self.__all_vehicles.append(vehicle)
        vtype = type(vehicle).__name__
        if vtype not in self.__vehicle_types:
            self.__vehicle_types[vtype] = []
        self.__vehicle_types[vtype].append(vehicle)

        model = vehicle.get_model()
        if model not in self.__vehicle_models:
            self.__vehicle_models[model] = []
        self.__vehicle_models[model].append(vehicle)

        make = vehicle.get_make()
        if make not in self.__vehicle_makes:
            self.__vehicle_makes[make] = []
        self.__vehicle_makes[make].append(vehicle)

    def remove_vehicle(self, vehicle):
        self.__all_vehicles.remove(vehicle)
        vtype = type(vehicle).__name__
        if vtype in self.__vehicle_types:
            self.__vehicle_types[vtype].remove(vehicle)
        model = vehicle.get_model()
        if model in self.__vehicle_models:
            self.__vehicle_models[model].remove(vehicle)
        make = vehicle.get_make()
        if make in self.__vehicle_makes:
            self.__vehicle_makes[make].remove(vehicle)

    def search_by_type(self, vehicle_type):
        return self.__vehicle_types.get(vehicle_type, [])

    def search_by_model(self, model):
        return self.__vehicle_models.get(model, [])

    def search_by_make(self, make):
        return self.__vehicle_makes.get(make, [])

    def get_all_vehicles(self):
        return self.__all_vehicles

    def get_available_vehicles(self):
        from .constants import VehicleStatus
        return [v for v in self.__all_vehicles if v.get_status() == VehicleStatus.AVAILABLE]
