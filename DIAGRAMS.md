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

## Component Diagram

```mermaid
graph TB
    subgraph Presentation_Layer["Presentation Layer"]
        Web[Web Interface]
        CLI[CLI Interface]
        API[REST API]
    end

    subgraph Business_Layer["Business Logic Layer"]
        CRS[CarRentalSystem]
        RM[Reservation Manager]
        VM[Vehicle Manager]
        MM[Member Manager]
        BM[Billing Manager]
        NM[Notification Manager]
        IM[Inventory Manager]
    end

    subgraph Data_Layer["Data Access Layer"]
        VR[Vehicle Repository]
        MR[Member Repository]
        RR[Reservation Repository]
        BR[Bill Repository]
        LR[Log Repository]
    end

    subgraph External["External Systems"]
        PG[Payment Gateway]
        ES[Email Service]
        SMS[SMS Service]
        BS[Barcode Scanner]
    end

    Web --> CRS
    CLI --> CRS
    API --> CRS

    CRS --> RM
    CRS --> VM
    CRS --> MM
    CRS --> BM
    CRS --> NM
    CRS --> IM

    RM --> RR
    VM --> VR
    MM --> MR
    BM --> BR
    VM --> LR

    BM --> PG
    NM --> ES
    NM --> SMS
    VM --> BS
```

## Context Diagram

```mermaid
graph TB
    subgraph System[Car Rental System]
        Core[CarRentalSystem]
    end

    Member((Member))
    Receptionist((Receptionist))
    Worker((Worker))
    Admin((System Admin))

    PG[Payment Gateway]
    ES[Email Service]
    SMS[SMS Service]
    BS[Barcode Scanner]
    DB[(Database)]

    Member -->|Search, Reserve, Pick-up, Return| System
    Receptionist -->|Manage vehicles, Register members| System
    Worker -->|Inspect returns, Update logs| System
    Admin -->|Configure system, Manage accounts| System

    System -->|Process payments| PG
    System -->|Send email notifications| ES
    System -->|Send SMS alerts| SMS
    System -->|Read vehicle barcodes| BS
    System -->|Persist all data| DB
    DB -->|Retrieve data| System
```

## Package / Development Diagram

```mermaid
graph TB
    subgraph car_rental_system["car_rental_system"]
        subgraph models["models"]
            Address
            Person
            Account
            Member
            Receptionist
            AdditionalDriver
            Vehicle
            Car
            Van
            Truck
            SUV
            Motorcycle
        end

        subgraph enums["enums"]
            BillItemType
            VehicleLogType
            VehicleStatus
            ReservationStatus
            AccountStatus
            PaymentStatus
            CarType
            VanType
        end

        subgraph services["services"]
            CarRentalSystem
            VehicleInventory
            VehicleReservation
        end

        subgraph business["business"]
            Bill
            BillItem
            Equipment
            Service
            RentalInsurance
            Notification
            VehicleLog
        end

        subgraph ui["ui"]
            main
        end
    end

    enums -.->|import| models
    services -.->|import| models
    services -.->|import| enums
    business -.->|import| models
    business -.->|import| enums
    ui -.->|import| services
    ui -.->|import| business
    ui -.->|import| models
```

## Deployment Diagram

```mermaid
graph TB
    subgraph Client_Tier["Client Tier"]
        Browser[Web Browser]
        Mobile[Mobile Device]
        CLI[CLI Terminal]
    end

    LB[Load Balancer]

    subgraph App_Server["Application Server"]
        subgraph App["car_rental_system.war"]
            UI[Presentation]
            Logic[Business Logic]
            DA[Data Access]
        end
    end

    subgraph DB_Server["Database Server"]
        DBInstance[Database Instance]
        Database[(Car Rental DB)]
    end

    subgraph External_Services["External Services"]
        PG[Payment Gateway Server]
        Mail[Mail Server]
        SMS[SMS Gateway]
    end

    Browser -->|HTTPS| LB
    Mobile -->|HTTPS| LB
    CLI -->|SSH| LB
    LB -->|HTTP/REST| App_Server
    App_Server -->|JDBC/SQL| DB_Server
    DBInstance --> Database
    App_Server -->|Payment API| PG
    App_Server -->|SMTP| Mail
    App_Server -->|SMS API| SMS
```

## Archivos PlantUML

Los diagramas en formato PlantUML estan disponibles en la carpeta `diagrams/`:

| Diagrama | Archivo |
|----------|---------|
| Use Case | `diagrams/use_case_diagram.puml` |
| Class | `diagrams/class_diagram.puml` |
| Activity - Pick Up | `diagrams/activity_pickup.puml` |
| Activity - Return | `diagrams/activity_return.puml` |
| **Component** | `diagrams/component_diagram.puml` |
| **Context** | `diagrams/context_diagram.puml` |
| **Development/Package** | `diagrams/development_diagram.puml` |
| **Deployment** | `diagrams/deployment_diagram.puml` |

Puedes renderizarlos con [PlantUML](https://plantuml.com/) o con extensiones de VS Code como `PlantUML Preview`.

---

> **Nota:** No puedo procesar archivos de imagen directamente. Los diagramas han sido creados en formato **PlantUML** (`.puml`) y **Mermaid.js** (en este archivo), los cuales se renderizan automáticamente en GitHub y en editores con soporte para estos formatos.
