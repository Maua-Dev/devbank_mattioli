# from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
# from ..enums.item_type_enum import ItemTypeEnum

from ..enums.agencia_enum import agencyEnum


class Client:
    agency_id: agencyEnum
    name: str
    client_id: int
    money: float
    
    def __init__(self, name: str = None, agency_id: agencyEnum = None, client_id: int = None, money: float = None):
     if not self.validate_name(name):
        raise ParamNotValidated ("name", "name must be a string")
     self.name = name
     self.agency_id = agency_id
     if not self.validate_client_id(client_id):
        raise ParamNotValidated ("client_id", "client_id must be greater than 0")
     self.client_id = client_id
     if not self.validate_money(money):
        raise ParamNotValidated ("money", "value can't be negative")
     self.money = money
    
    @staticmethod
    def validate_client_id (client_id: int) -> bool:
       if not client_id > 0 :
          return False
       return True
    
    @staticmethod
    def validate_name (name: str) -> bool:
       if type(name) != str:
         return False
       return True
    
    @staticmethod
    def validate_money (money: float) -> bool:
        if money < 0:
           return False
        return True
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "agency": self.agency_id,
            "account": self.client_id,
            "current_balance": self.money
        }
#     def __init__(self, name: str=None, price: float=None, item_type: ItemTypeEnum=None, admin_permission: bool=None):
#         validation_name = self.validate_name(name)
#         if validation_name[0] is False:
#             raise ParamNotValidated("name", validation_name[1])
#         self.name = name
        
#         validation_price = self.validate_price(price)
#         if validation_price[0] is False:
#             raise ParamNotValidated("price", validation_price[1])
#         self.price = price

#         validation_item_type = self.validate_item_type(item_type)
#         if validation_item_type[0] is False:
#             raise ParamNotValidated("item_type", validation_item_type[1])
#         self.item_type = item_type
        
#         validation_admin_permission = self.validate_admin_permission(admin_permission)
#         if validation_admin_permission[0] is False:
#             raise ParamNotValidated("admin_permission", validation_admin_permission[1])
#         self.admin_permission = admin_permission
        
#     @staticmethod
#     def validate_name(name: str) -> Tuple[bool, str]:
#         if name is None:
#             return (False, "Name is required")
#         if type(name) != str:
#             return (False, "Name must be a string")
#         if len(name) < 3:
#             return (False, "Name must be at least 3 characters long")
#         return (True, "")
        
#     @staticmethod
#     def validate_price(price: float) -> Tuple[bool, str]:
#         if price is None:
#             return (False, "Price is required")
#         if type(price) != float:
#             return (False, "Price must be a float")
#         if price < 0:
#             return (False, "Price must be a positive number")
#         return (True, "")
    
#     @staticmethod
#     def validate_item_type(item_type: ItemTypeEnum) -> Tuple[bool, str]:
#         if item_type is None:
#             return (False, "Item type is required")
#         if type(item_type) != ItemTypeEnum:
#             return (False, "Item type must be a ItemTypeEnum")
#         return (True, "")
    
#     @staticmethod
#     def validate_admin_permission(admin_permission: bool) -> Tuple[bool, str]:
#         if admin_permission is None:
#             return (False, "Admin permission is required")
#         if type(admin_permission) != bool:
#             return (False, "Admin permission must be a boolean")
#         return (True, "")
        
#     @staticmethod
#     def validate_item_id(item_id: int) -> Tuple[bool, str]:
#         if item_id is None:
#             return (False, "Missing 'item_id' parameter")

#         if type(item_id) != int:
#             return (False, "Parameter 'item_id' must be an integer")
        
#         if item_id < 0:
#             return (False, "Parameter 'item_id' must be a positive integer")

#         return (True, "")
    
        
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "price": self.price,
#             "item_type": self.item_type.value,
#             "admin_permission": self.admin_permission
#         }
    
#     def __eq__(self,other):
#         return self.name == other.name and self.price == other.price and self.item_type == other.item_type and self.admin_permission == other.admin_permission
    
#     def __repr__(self):
#         return f"Item(name={self.name}, price={self.price}, item_type={self.item_type}, admin_permission={self.admin_permission})"