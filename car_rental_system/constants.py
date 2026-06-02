from enum import Enum


class BillItemType(Enum):
    BASE_CHARGE = 1
    ADDITIONAL_SERVICE = 2
    FINE = 3
    OTHER = 4


class VehicleLogType(Enum):
    ACCIDENT = 1
    FUELING = 2
    CLEANING_SERVICE = 3
    OIL_CHANGE = 4
    REPAIR = 5
    OTHER = 6


class VanType(Enum):
    PASSENGER = 1
    CARGO = 2


class CarType(Enum):
    ECONOMY = 1
    COMPACT = 2
    INTERMEDIATE = 3
    STANDARD = 4
    FULL_SIZE = 5
    PREMIUM = 6
    LUXURY = 7


class VehicleStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOANED = 3
    LOST = 4
    BEING_SERVICED = 5
    OTHER = 6


class ReservationStatus(Enum):
    ACTIVE = 1
    PENDING = 2
    CONFIRMED = 3
    COMPLETED = 4
    CANCELLED = 5
    NONE = 6


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    BLOCKED = 5


class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    FILLED = 4
    DECLINED = 5
    CANCELLED = 6
    ABANDONED = 7
    SETTLING = 8
    SETTLED = 9
    REFUNDED = 10
