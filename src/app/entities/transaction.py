from..enums.transaction_enum import transaction_enum
from ..errors.entity_errors import ParamNotValidated
import time

class Transactions:
    type_transaction: transaction_enum
    value: float
    balance: float
    time: float

    def __init__(self, type_transaction:  transaction_enum, value: float, balance: float, time: float):
        if not self.validate_enum(type_transaction):
            raise ParamNotValidated("type_transaction", "Type transaction must be a transaction_enum")
        self.type_transaction = type_transaction
        if not self.validate_value(value):
            raise ParamNotValidated("value", "value can't be negative")
        self.value = value
        if not self.validate_balance(balance):
            raise ParamNotValidated("balance", "value can't be negative")
        self.balance = balance
        if not self.validate_time(time):
            raise ParamNotValidated("time", "time must be a float")
        self.time = time

    @staticmethod
    def validate_enum(type_transaction:  transaction_enum) -> bool:
        return (type(type_transaction) ==  transaction_enum)
    @staticmethod
    def validate_value (value: float) -> bool:
        if value < 0:
           return False
        return True
    @staticmethod
    def validate_balance (balance: float) -> bool:
        if balance < 0:
           return False
        return True
    @staticmethod
    def validate_time (time: float) -> bool:
        if type(time) != float:
           return False
        return True

