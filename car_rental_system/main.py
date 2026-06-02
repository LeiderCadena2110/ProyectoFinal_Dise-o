from datetime import datetime, timedelta

from .constants import (
    CarType, VanType, VehicleStatus, AccountStatus, PaymentStatus, VehicleLogType
)
from .address import Address
from .person import Person
from .account import Member, Receptionist, AdditionalDriver
from .vehicle import Car, Van, Truck, SUV, Motorcycle
from .vehicle_log import VehicleLog
from .car_rental_location import CarRentalLocation
from .car_rental_system import CarRentalSystem
from .notification import Notification
from .equipment import Equipment
from .service import Service
from .rental_insurance import RentalInsurance


def demo():
    print("=" * 70)
    print("          CAR RENTAL SYSTEM - OBJECT ORIENTED DESIGN")
    print("=" * 70)

    # ------------------------------------------------------------------
    # 1. Create Addresses
    # ------------------------------------------------------------------
    addr1 = Address("123 Main St", "New York", "NY", "10001", "USA")
    addr2 = Address("456 Airport Blvd", "Los Angeles", "CA", "90045", "USA")
    addr3 = Address("789 Oak Ave", "Miami", "FL", "33101", "USA")
    addr_member = Address("321 Home St", "Brooklyn", "NY", "11201", "USA")

    # ------------------------------------------------------------------
    # 2. Create Rental Locations
    # ------------------------------------------------------------------
    location_downtown = CarRentalLocation("Downtown NYC", addr1)
    location_airport = CarRentalLocation("LAX Airport", addr2)
    location_miami = CarRentalLocation("Miami Beach", addr3)

    # ------------------------------------------------------------------
    # 3. Create Car Rental System
    # ------------------------------------------------------------------
    system = CarRentalSystem("EasyRent Car Rental")
    system.add_new_location(location_downtown)
    system.add_new_location(location_airport)
    system.add_new_location(location_miami)
    print(f"\n[SYSTEM] '{system.get_name()}' initialized with {len(system.get_locations())} locations.")

    # ------------------------------------------------------------------
    # 4. Create People & Accounts
    # ------------------------------------------------------------------
    person_john = Person("John Doe", addr_member, "john@email.com", "555-0101")
    person_alice = Person("Alice Smith", addr_member, "alice@email.com", "555-0102")
    person_bob = Person("Bob Receptionist", addr1, "bob@rental.com", "555-0201")

    member1 = Member("M001", "pass123", person_john)
    member2 = Member("M002", "pass456", person_alice)

    receptionist = Receptionist("R001", "admin123", person_bob, datetime.now())

    system.register_member(member1)
    system.register_member(member2)
    system.add_receptionist(receptionist)

    print(f"[ACCOUNTS] Registered {len(system.get_members())} members and {len(system.get_receptionists())} receptionist.")

    # ------------------------------------------------------------------
    # 5. Create Vehicles
    # ------------------------------------------------------------------
    car1 = Car("LIC-1001", "STK-001", 5, "BARCODE-001", True,
               VehicleStatus.AVAILABLE, "Camry", "Toyota", 2022, 15000,
               CarType.STANDARD)
    car2 = Car("LIC-1002", "STK-002", 5, "BARCODE-002", True,
               VehicleStatus.AVAILABLE, "Civic", "Honda", 2023, 8000,
               CarType.COMPACT)
    car3 = Car("LIC-1003", "STK-003", 4, "BARCODE-003", False,
               VehicleStatus.AVAILABLE, "Mustang", "Ford", 2024, 5000,
               CarType.PREMIUM)
    van1 = Van("LIC-2001", "STK-004", 12, "BARCODE-004", False,
               VehicleStatus.AVAILABLE, "Sprinter", "Mercedes", 2022, 30000,
               VanType.PASSENGER)
    truck1 = Truck("LIC-3001", "STK-005", 3, "BARCODE-005", False,
                   VehicleStatus.AVAILABLE, "F-150", "Ford", 2021, 45000)
    suv1 = SUV("LIC-4001", "STK-006", 7, "BARCODE-006", True,
               VehicleStatus.AVAILABLE, "Highlander", "Toyota", 2023, 12000)
    motorcycle1 = Motorcycle("LIC-5001", "STK-007", 2, "BARCODE-007", False,
                             VehicleStatus.AVAILABLE, "Ninja 650", "Kawasaki", 2024, 2000)

    inventory = system.get_inventory()
    for v in [car1, car2, car3, van1, truck1, suv1, motorcycle1]:
        inventory.add_vehicle(v)

    print(f"[INVENTORY] Added {len(inventory.get_all_vehicles())} vehicles to inventory.")

    # ------------------------------------------------------------------
    # 6. Add Vehicle Logs
    # ------------------------------------------------------------------
    log1 = VehicleLog(1, VehicleLogType.OIL_CHANGE, "Regular oil change performed", datetime.now() - timedelta(days=30))
    log2 = VehicleLog(2, VehicleLogType.CLEANING_SERVICE, "Detailed cleaning completed", datetime.now() - timedelta(days=7))
    log3 = VehicleLog(3, VehicleLogType.REPAIR, "Brake pads replaced", datetime.now() - timedelta(days=60))

    car1.add_log_entry(log1)
    car1.add_log_entry(log2)
    truck1.add_log_entry(log3)

    print(f"[LOGS] Added vehicle maintenance logs.")

    # ------------------------------------------------------------------
    # 7. Create Equipment, Services, Insurance
    # ------------------------------------------------------------------
    gps = Equipment("EQ-001", "GPS Navigation", "Portable GPS device", 5.0)
    child_seat = Equipment("EQ-002", "Child Safety Seat", "Infant car seat", 8.0)
    ski_rack = Equipment("EQ-003", "Ski Rack", "Roof-mounted ski rack", 12.0)

    roadside = Service("SV-001", "Roadside Assistance", "24/7 emergency roadside help", 15.0)
    extra_driver = Service("SV-002", "Additional Driver", "Add a second driver to the rental", 10.0)
    wifi = Service("SV-003", "In-Car WiFi", "High-speed WiFi hotspot", 12.0)

    basic_ins = RentalInsurance("IN-001", "Basic Insurance",
                                "Covers collision damage up to $5000", 20.0,
                                "Collision: $5000 max, Liability: $10000")
    full_ins = RentalInsurance("IN-002", "Full Coverage Insurance",
                               "Full coverage with zero deductible", 35.0,
                               "Collision: Full, Liability: $50000, Theft: Covered")

    print(f"[ADD-ONS] Created equipment, services, and insurance options.")

    # ------------------------------------------------------------------
    # 8. Member searches for available vehicles
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("                  USE CASE: SEARCH VEHICLES")
    print("=" * 70)
    available = inventory.get_available_vehicles()
    print(f"\n[SEARCH] Available vehicles ({len(available)} found):")
    for v in available:
        print(f"   - {v} | Capacity: {v.get_passenger_capacity()} | Mileage: {v.get_mileage()} mi")

    # ------------------------------------------------------------------
    # 9. Member reserves a vehicle
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("               USE CASE: RESERVE A VEHICLE (PICK UP)")
    print("=" * 70)
    pickup_date = datetime.now() + timedelta(days=1)
    due_date = pickup_date + timedelta(days=5)

    reservation1 = system.reserve_vehicle(
        member1, car1,
        location_downtown.get_name(),
        location_airport.get_name(),
        pickup_date, due_date
    )

    if reservation1:
        print(f"\n[RESERVATION] Created: {reservation1}")
        print(f"   Customer: {member1.get_person().get_name()}")
        print(f"   Vehicle: {car1.get_make()} {car1.get_model()}")
        print(f"   Pick up: {location_downtown.get_name()} on {pickup_date.strftime('%Y-%m-%d')}")
        print(f"   Return:  {location_airport.get_name()} by {due_date.strftime('%Y-%m-%d')}")
    else:
        print("\n[ERROR] Vehicle could not be reserved (not available).")

    # ------------------------------------------------------------------
    # 10. Member adds equipment, services, and insurance to reservation
    # ------------------------------------------------------------------
    reservation1.add_equipment(gps)
    reservation1.add_equipment(child_seat)
    reservation1.add_service(roadside)
    reservation1.add_insurance(basic_ins)

    print(f"\n[ADD-ONS] Added to reservation #{reservation1.get_reservation_number()}:")
    for eq in reservation1.get_equipments():
        print(f"   Equipment: {eq}")
    for svc in reservation1.get_services():
        print(f"   Service: {svc}")
    for ins in reservation1.get_insurances():
        print(f"   Insurance: {ins}")

    # ------------------------------------------------------------------
    # 11. System sends a notification about upcoming pick-up
    # ------------------------------------------------------------------
    notif1 = Notification(1, f"Reminder: Your vehicle rental starts tomorrow at {location_downtown.get_name()}.",
                          member1.get_person())
    reservation1.add_notification(notif1)
    print(f"\n[NOTIFICATION] Sent: {notif1}")

    # ------------------------------------------------------------------
    # 12. Check-out vehicle (member picks it up)
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("               USE CASE: CHECK-OUT VEHICLE")
    print("=" * 70)
    if system.check_out_vehicle(reservation1):
        print(f"\n[CHECK-OUT] Vehicle successfully checked out!")
        print(f"   Vehicle status: {car1.get_status().name}")
        print(f"   Reservation status: {reservation1.get_status().name}")
    else:
        print("\n[ERROR] Check-out failed.")

    # ------------------------------------------------------------------
    # 13. Member reserves a second vehicle
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("               USE CASE: SECOND RESERVATION")
    print("=" * 70)
    reservation2 = system.reserve_vehicle(
        member2, suv1,
        location_miami.get_name(),
        location_miami.get_name(),
        datetime.now() + timedelta(days=2),
        datetime.now() + timedelta(days=9)
    )

    if reservation2:
        reservation2.add_equipment(ski_rack)
        reservation2.add_service(extra_driver)
        reservation2.add_service(wifi)
        reservation2.add_insurance(full_ins)

        print(f"\n[RESERVATION] Created: {reservation2}")
        print(f"   Customer: {member2.get_person().get_name()}")
        print(f"   Vehicle: {suv1.get_make()} {suv1.get_model()}")
        for ins in reservation2.get_insurances():
            print(f"   Insurance: {ins}")

    # ------------------------------------------------------------------
    # 14. Return a vehicle (with late fee)
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("               USE CASE: RETURN VEHICLE")
    print("=" * 70)
    # Simulate returning 2 days late
    reservation1.set_return_date(due_date + timedelta(days=2))
    bill = system.return_vehicle(reservation1)

    if bill:
        print(f"\n[RETURN] Vehicle returned successfully!")
        print(f"\n{'=' * 50}")
        print(f"             FINAL BILL")
        print(f"{'=' * 50}")
        print(f"   Reservation: {reservation1.get_reservation_number()}")
        print(f"   Customer: {member1.get_person().get_name()}")
        print(f"   Vehicle: {car1.get_make()} {car1.get_model()}")
        print(f"   Pick up: {reservation1.get_pickup_date().strftime('%Y-%m-%d')}")
        print(f"   Due date: {reservation1.get_due_date().strftime('%Y-%m-%d')}")
        print(f"   Returned: {reservation1.get_return_date().strftime('%Y-%m-%d')}")
        print(f"\n   Items:")
        for item in bill.get_items():
            print(f"      {item}")
        print(f"\n   TOTAL: ${bill.get_total_amount():.2f}")
        print(f"   Status: {bill.get_payment_status().name}")
        print(f"{'=' * 50}")

    # ------------------------------------------------------------------
    # 15. Cancel a reservation
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("               USE CASE: CANCEL RESERVATION")
    print("=" * 70)
    reservation3 = system.reserve_vehicle(
        member1, car2,
        location_downtown.get_name(),
        location_downtown.get_name(),
        datetime.now() + timedelta(days=10)
    )

    if reservation3:
        print(f"\n[RESERVATION] Created: {reservation3}")
        if reservation3.cancel():
            print(f"[CANCEL] Reservation #{reservation3.get_reservation_number()} cancelled successfully.")
            print(f"   Vehicle {car2.get_license_number()} status: {car2.get_status().name}")
        else:
            print(f"[CANCEL] Failed to cancel reservation.")

    # ------------------------------------------------------------------
    # 16. Receptionist searches for a member
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("               USE CASE: RECEPTIONIST SEARCH")
    print("=" * 70)
    search_results = receptionist.search_member("john", system.get_members())
    print(f"\n[SEARCH MEMBER] Searching for 'john':")
    for m in search_results:
        print(f"   Found: {m.get_person().get_name()} (ID: {m.get_id()})")
    print(f"   Total results: {len(search_results)}")

    # ------------------------------------------------------------------
    # 17. Summary
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("                    SYSTEM SUMMARY")
    print("=" * 70)
    print(f"   System: {system.get_name()}")
    print(f"   Locations: {len(system.get_locations())}")
    print(f"   Vehicles: {len(inventory.get_all_vehicles())}")
    print(f"   Members: {len(system.get_members())}")
    print(f"   Reservations: {len(system.get_reservations())}")
    cancelled_count = sum(1 for r in system.get_reservations() if r.get_status().name == "CANCELLED")
    completed_count = sum(1 for r in system.get_reservations() if r.get_status().name == "COMPLETED")
    active_count = sum(1 for r in system.get_reservations() if r.get_status().name not in ["CANCELLED", "COMPLETED"])
    print(f"      - Active: {active_count}")
    print(f"      - Completed: {completed_count}")
    print(f"      - Cancelled: {cancelled_count}")
    print("=" * 70)
    print("\n          CAR RENTAL SYSTEM DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    demo()
