from datetime import datetime, timedelta
from .constants import ReservationStatus


class VehicleReservation:
    def __init__(self, reservation_number, customer, vehicle,
                 pickup_location, return_location,
                 pickup_date=None, due_date=None):
        self.__reservation_number = reservation_number
        self.__creation_date = datetime.now()
        self.__status = ReservationStatus.ACTIVE
        self.__due_date = due_date if due_date else datetime.now() + timedelta(days=7)
        self.__return_date = None
        self.__pickup_date = pickup_date if pickup_date else datetime.now()
        self.__pickup_location_name = pickup_location
        self.__return_location_name = return_location
        self.__customer = customer
        self.__vehicle = vehicle
        self.__bill = None
        self.__additional_drivers = []
        self.__notifications = []
        self.__insurances = []
        self.__equipments = []
        self.__services = []

    def get_reservation_number(self):
        return self.__reservation_number

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_due_date(self):
        return self.__due_date

    def get_return_date(self):
        return self.__return_date

    def set_return_date(self, return_date):
        self.__return_date = return_date

    def get_pickup_date(self):
        return self.__pickup_date

    def get_customer(self):
        return self.__customer

    def get_vehicle(self):
        return self.__vehicle

    def get_bill(self):
        return self.__bill

    def set_bill(self, bill):
        self.__bill = bill

    def get_additional_drivers(self):
        return self.__additional_drivers

    def add_additional_driver(self, driver):
        self.__additional_drivers.append(driver)

    def get_insurances(self):
        return self.__insurances

    def add_insurance(self, insurance):
        self.__insurances.append(insurance)

    def get_equipments(self):
        return self.__equipments

    def add_equipment(self, equipment):
        self.__equipments.append(equipment)

    def get_services(self):
        return self.__services

    def add_service(self, service):
        self.__services.append(service)

    def get_notifications(self):
        return self.__notifications

    def add_notification(self, notification):
        self.__notifications.append(notification)

    def cancel(self):
        if self.__status in [ReservationStatus.ACTIVE, ReservationStatus.PENDING, ReservationStatus.CONFIRMED]:
            self.__status = ReservationStatus.CANCELLED
            self.__vehicle.set_status(ReservationStatus.CANCELLED)
            return True
        return False

    def complete_reservation(self):
        self.__status = ReservationStatus.COMPLETED
        self.__return_date = datetime.now()

    def __str__(self):
        return (f"Reservation #{self.__reservation_number}: {self.__vehicle.get_make()} {self.__vehicle.get_model()} "
                f"- Status: {self.__status.name} - Due: {self.__due_date.strftime('%Y-%m-%d')}")
