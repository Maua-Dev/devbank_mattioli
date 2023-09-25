from typing import List
from src.app.entities.client import Client
from ..enums.agencia_enum import agencyEnum
from ..entities.client import Client
from ..repo.client_repository_interface import IClientRepository

class ClientRepositoryMock(IClientRepository):
    client: List[Client]

    def __init__(self):
        self.clients = [
            Client(agency_id= agencyEnum.Santander, name="Alfredo", client_id = 1, money= 0.5),
            Client(agency_id= agencyEnum.Nubank, name="Giovanna", client_id = 2, money= 55420.0),
            Client(agency_id= agencyEnum.BancodoBrasil, name="Gabriel", client_id = 3, money= 20253.7),
            Client(agency_id= agencyEnum.Gringots, name="Harry", client_id = 4, money= 999999.99)
        ]
    def get_all_clients(self) -> List[Client]:
        return self.clients
    def deposit_money(self, money: float) -> float:
        self.client.money += money
        return self.user.money  
    def withdraw_money(self, money: float) -> float:
        self.client.money -= money
        return self.user.money  
    
#     items: Dict[int, Item]
    
#     def __init__(self):
#         self.items = {
#             1: Item(name="Barbie", price=48.90, item_type=ItemTypeEnum.TOY, admin_permission=False),
#             2: Item(name="Hamburguer", price=38.00, item_type=ItemTypeEnum.FOOD, admin_permission=False),
#             3: Item(name="T-shirt", price=22.95, item_type=ItemTypeEnum.CLOTHES, admin_permission=False),
#             4: Item(name="Super Mario Bros", price=55.00, item_type=ItemTypeEnum.GAMES, admin_permission=True)
#         }
        
#     def get_all_items(self) -> List[Item]:
#         return self.items.values()
    
#     def get_item(self, item_id: int) -> Optional[Item]:
#         return self.items.get(item_id, None)
    
#     def create_item(self, item: Item, item_id: int) -> Item:
        
#         self.items[item_id] = item
#         return item
    
#     def delete_item(self, item_id: int) -> Item:
#         item = self.items.pop(item_id, None)
#         return item
        
        
#     def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#         item = self.items.get(item_id, None)
#         if item is None:
#             return None
        
#         if name is not None:
#             item.name = name
#         if price is not None:
#             item.price = price
#         if item_type is not None:
#             item.item_type = item_type
#         if admin_permission is not None:
#             item.admin_permission = admin_permission
#         self.items[item_id] = item
        
#         return item
        
    
    