from datetime import datetime
from .constants import BillItemType, PaymentStatus


class BillItem:
    def __init__(self, item_id, description, amount, item_type=BillItemType.BASE_CHARGE):
        self.__id = item_id
        self.__description = description
        self.__amount = amount
        self.__type = item_type

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__type

    def __str__(self):
        return f"  {self.__description}: ${self.__amount:.2f}"


class Bill:
    def __init__(self, bill_id):
        self.__id = bill_id
        self.__items = []
        self.__total_amount = 0.0
        self.__payment_status = PaymentStatus.UNPAID
        self.__creation_date = datetime.now()

    def get_id(self):
        return self.__id

    def get_items(self):
        return self.__items

    def get_total_amount(self):
        return self.__total_amount

    def get_payment_status(self):
        return self.__payment_status

    def add_item(self, item):
        self.__items.append(item)
        self.__total_amount += item.get_amount()

    def set_payment_status(self, status):
        self.__payment_status = status

    def __str__(self):
        result = f"Bill #{self.__id} - Total: ${self.__total_amount:.2f} - Status: {self.__payment_status.name}\n"
        for item in self.__items:
            result += f"{item}\n"
        return result
