from .vehicle_inventory import VehicleInventory
from .constants import VehicleStatus, ReservationStatus, PaymentStatus
from .bill import Bill, BillItem
from .bill import BillItemType


class CarRentalSystem:
    def __init__(self, name):
        self.__name = name
        self.__locations = []
        self.__members = []
        self.__receptionists = []
        self.__inventory = VehicleInventory()
        self.__reservations = []

    def get_name(self):
        return self.__name

    def get_locations(self):
        return self.__locations

    def add_new_location(self, location):
        self.__locations.append(location)

    def get_members(self):
        return self.__members

    def register_member(self, member):
        self.__members.append(member)

    def get_receptionists(self):
        return self.__receptionists

    def add_receptionist(self, receptionist):
        self.__receptionists.append(receptionist)

    def get_inventory(self):
        return self.__inventory

    def get_reservations(self):
        return self.__reservations

    def reserve_vehicle(self, member, vehicle, pickup_location, return_location,
                        pickup_date=None, due_date=None):
        if vehicle.get_status() != VehicleStatus.AVAILABLE:
            return None

        from .vehicle_reservation import VehicleReservation
        reservation_number = f"RES-{len(self.__reservations) + 1:04d}"
        reservation = VehicleReservation(
            reservation_number, member, vehicle,
            pickup_location, return_location,
            pickup_date, due_date
        )
        vehicle.reserve_vehicle()
        member.add_reservation(reservation)
        self.__reservations.append(reservation)
        return reservation

    def check_out_vehicle(self, reservation):
        if reservation.get_status() == ReservationStatus.CONFIRMED:
            return False
        reservation.set_status(ReservationStatus.CONFIRMED)
        reservation.get_vehicle().set_status(VehicleStatus.LOANED)
        return True

    def return_vehicle(self, reservation):
        vehicle = reservation.get_vehicle()
        vehicle.return_vehicle()

        due_date = reservation.get_due_date()
        return_date = reservation.get_return_date()
        from datetime import datetime
        if return_date is None:
            return_date = datetime.now()
            reservation.set_return_date(return_date)

        bill = Bill(f"BILL-{reservation.get_reservation_number()}")
        days_rented = (return_date - reservation.get_pickup_date()).days
        if days_rented <= 0:
            days_rented = 1

        base_rate = 50.0
        base_item = BillItem(f"BI-001", f"Base charge ({days_rented} days @ ${base_rate}/day)",
                             base_rate * days_rented)
        bill.add_item(base_item)

        if return_date > due_date:
            late_days = (return_date - due_date).days
            late_fee_rate = 25.0
            fine_item = BillItem(f"BI-002", f"Late fee ({late_days} days @ ${late_fee_rate}/day)",
                                 late_fee_rate * late_days, BillItemType.FINE)
            bill.add_item(fine_item)

        for equipment in reservation.get_equipments():
            equip_item = BillItem(f"BI-EQ-{equipment.get_id()}",
                                  f"Equipment: {equipment.get_name()}",
                                  equipment.get_daily_cost() * days_rented,
                                  BillItemType.ADDITIONAL_SERVICE)
            bill.add_item(equip_item)

        for service in reservation.get_services():
            svc_item = BillItem(f"BI-SV-{service.get_id()}",
                                f"Service: {service.get_name()}",
                                service.get_cost(),
                                BillItemType.ADDITIONAL_SERVICE)
            bill.add_item(svc_item)

        for insurance in reservation.get_insurances():
            ins_item = BillItem(f"BI-IN-{insurance.get_id()}",
                                f"Insurance: {insurance.get_name()}",
                                insurance.get_daily_cost() * days_rented,
                                BillItemType.ADDITIONAL_SERVICE)
            bill.add_item(ins_item)

        bill.set_payment_status(PaymentStatus.COMPLETED)
        reservation.set_bill(bill)
        reservation.complete_reservation()
        return bill
