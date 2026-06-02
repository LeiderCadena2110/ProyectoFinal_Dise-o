# Car Rental System - Diagramas

## Use Case Diagram

```mermaid
graph TD
    ActorMember[Member]
    ActorReceptionist[Receptionist]
    ActorWorker[Worker]
    ActorSystem[System]

    UC1[Search Catalog]
    UC2[Register New Account]
    UC3[Cancel Membership]
    UC4[Reserve Vehicle]
    UC5[Check-out Vehicle]
    UC6[Return Vehicle]
    UC7[Add/Remove/Edit Vehicle]
    UC8[Add Equipment]
    UC9[Add Service]
    UC10[Add Insurance]
    UC11[Update Vehicle Log]
    UC12[Send Notification]
    UC13[Generate Bill]
    UC14[Cancel Reservation]

    ActorMember --> UC1
    ActorMember --> UC2
    ActorMember --> UC3
    ActorMember --> UC4
    ActorMember --> UC5
    ActorMember --> UC6
    ActorMember --> UC8
    ActorMember --> UC9
    ActorMember --> UC10
    ActorMember --> UC14

    ActorReceptionist --> UC2
    ActorReceptionist --> UC7
    ActorReceptionist --> UC4

    ActorWorker --> UC6
    ActorWorker --> UC11

    ActorSystem --> UC12
    ActorSystem --> UC13

    UC4 -.->|include| UC12
    UC5 -.->|include| UC13
    UC6 -.->|include| UC13
    UC6 -.->|include| UC11
```

## Class Diagram

```mermaid
classDiagram

    class Account {
        <<abstract>>
        - id: str
        - password: str
        - status: AccountStatus
        - person: Person
        + reset_password()
    }

    class Member {
        - total_vehicles_reserved: int
        - reservations: list
        + get_reservations()
    }

    class Receptionist {
        - date_joined: datetime
        + search_member(name)
    }

    class AdditionalDriver {
        - driver_id: str
        - person: Person
    }

    class Person {
        - name: str
        - address: Address
        - email: str
        - phone: str
    }

    class Address {
        - street_address: str
        - city: str
        - state: str
        - zip_code: str
        - country: str
    }

    class Vehicle {
        <<abstract>>
        - license_number: str
        - stock_number: str
        - passenger_capacity: int
        - barcode: str
        - has_sunroof: bool
        - status: VehicleStatus
        - model: str
        - make: str
        - manufacturing_year: int
        - mileage: int
        - log: list
        + reserve_vehicle()
        + return_vehicle()
    }

    class Car {
        - type: CarType
    }

    class Van {
        - type: VanType
    }

    class Truck

    class SUV

    class Motorcycle

    class VehicleLog {
        - id: int
        - type: VehicleLogType
        - description: str
        - creation_date: datetime
        + update()
    }

    class VehicleInventory {
        - vehicle_types: dict
        - vehicle_models: dict
        - all_vehicles: list
        + add_vehicle()
        + remove_vehicle()
        + search_by_type()
        + search_by_model()
        + search_by_make()
        + get_available_vehicles()
    }

    class Search {
        <<interface>>
        + search_by_type()
        + search_by_model()
        + search_by_make()
    }

    class VehicleReservation {
        - reservation_number: str
        - creation_date: datetime
        - status: ReservationStatus
        - due_date: datetime
        - return_date: datetime
        - pickup_date: datetime
        - customer: Member
        - vehicle: Vehicle
        - bill: Bill
        + cancel()
        + complete_reservation()
    }

    class CarRentalLocation {
        - name: str
        - location: Address
    }

    class CarRentalSystem {
        - name: str
        - locations: list
        - members: list
        - inventory: VehicleInventory
        - reservations: list
        + register_member()
        + reserve_vehicle()
        + check_out_vehicle()
        + return_vehicle()
    }

    class Notification {
        - id: int
        - content: str
        - recipient: Person
        - sent_date: datetime
        + mark_as_read()
    }

    class Bill {
        - id: str
        - items: list
        - total_amount: float
        - payment_status: PaymentStatus
        + add_item()
    }

    class BillItem {
        - id: str
        - description: str
        - amount: float
        - type: BillItemType
    }

    class Equipment {
        - id: str
        - name: str
        - description: str
        - daily_cost: float
    }

    class Service {
        - id: str
        - name: str
        - description: str
        - cost: float
    }

    class RentalInsurance {
        - id: str
        - name: str
        - description: str
        - daily_cost: float
        - coverage_details: str
    }

    Account <|-- Member
    Account <|-- Receptionist
    Account --> Person
    Person --> Address

    Vehicle <|-- Car
    Vehicle <|-- Van
    Vehicle <|-- Truck
    Vehicle <|-- SUV
    Vehicle <|-- Motorcycle
    Vehicle --> VehicleLog
    VehicleInventory ..|> Search

    VehicleReservation --> Member
    VehicleReservation --> Vehicle
    VehicleReservation --> Bill
    VehicleReservation --> AdditionalDriver
    VehicleReservation --> Notification
    VehicleReservation --> Equipment
    VehicleReservation --> Service
    VehicleReservation --> RentalInsurance

    CarRentalSystem --> CarRentalLocation
    CarRentalSystem --> Member
    CarRentalSystem --> VehicleInventory
    CarRentalSystem --> VehicleReservation

    Bill --> BillItem
```

## Activity Diagram: Pick Up a Vehicle

```mermaid
flowchart TD
    Start([Start]) --> Search[Member searches for available vehicles]
    Search --> Select[Member selects a vehicle]
    Select --> CreateRes[Member creates reservation]
    CreateRes --> AddOns[Member adds equipment / services / insurance]

    AddOns --> CheckAvail{System verifies vehicle availability}

    CheckAvail -->|Available| Confirm[System confirms reservation]
    Confirm --> SetReserved[Vehicle status set to RESERVED]
    SetReserved --> SendNotif[System sends confirmation notification]
    SendNotif --> Arrive[Member arrives at rental location]
    Arrive --> Present[Member presents reservation details]
    Present --> Verify[Receptionist verifies reservation]
    Verify --> GenCheckout[System generates check-out form]
    GenCheckout --> Sign[Member signs rental agreement]
    Sign --> ReceiveKeys[Member receives vehicle keys]
    ReceiveKeys --> SetLoaned[Vehicle status set to LOANED]
    SetLoaned --> SetConfirmed[Reservation status set to CONFIRMED]
    SetConfirmed --> NotifPickup[System sends pick-up notification]
    NotifPickup --> Stop([Stop])

    CheckAvail -->|Not Available| Reject[System rejects reservation]
    Reject --> Suggest[System suggests alternative vehicles]
    Suggest --> ChooseAlt{Member chooses alternative?}

    ChooseAlt -->|Yes| Select
    ChooseAlt -->|No| Cancel[Reservation cancelled]
    Cancel --> Stop
```

## Activity Diagram: Return a Vehicle

```mermaid
flowchart TD
    Start([Start]) --> Return[Member returns vehicle to rental location]
    Return --> Inspect[Worker inspects vehicle condition]
    Inspect --> UpdateLog[Worker updates vehicle log]
    UpdateLog --> RecordMileage[Worker records mileage and fuel level]
    RecordMileage --> CalcPeriod[System calculates rental period]

    CalcPeriod --> CheckLate{Return date > Due date?}

    CheckLate -->|Late| CalcLateFee[System calculates late fee]
    CalcLateFee --> AddLateFee[System adds late fee charge to bill]

    CheckLate -->|On time| CalcBase[System calculates base charges]
    AddLateFee --> CalcBase

    CalcBase --> AddExtras[System adds equipment / service / insurance charges]
    AddExtras --> GenBill[System generates final bill]
    GenBill --> Review[Member reviews bill]

    Review --> Accept{Member accepts bill?}

    Accept -->|Yes| Pay[Member makes payment]
    Pay --> SetPaid[Payment status set to COMPLETED]
    SetPaid --> SetAvailable[Vehicle status set to AVAILABLE]
    SetAvailable --> SetCompleted[Reservation status set to COMPLETED]
    SetCompleted --> SendConfirm[System sends return confirmation]
    SendConfirm --> Stop([Stop])

    Accept -->|No| SetPending[Payment status set to PENDING]
    SetPending --> Escalate[System escalates to receptionist]
    Escalate --> Handle[Receptionist handles dispute]
    Handle --> Stop
```

## Archivos PlantUML

Los diagramas en formato PlantUML estan disponibles en la carpeta `diagrams/`:

- `diagrams/use_case_diagram.puml`
- `diagrams/class_diagram.puml`
- `diagrams/activity_pickup.puml`
- `diagrams/activity_return.puml`

Puedes renderizarlos con [PlantUML](https://plantuml.com/) o con extensiones de VS Code como `PlantUML Preview`.
