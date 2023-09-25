from src.app.enums.transaction_enum import transaction_enum
from src.app.repo.client_repository_mock import ClientRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock


class Test_Client_Repository_mock :
    def test_get_all_clients(self):
        repo = ClientRepositoryMock()
        clients = repo.get_all_clients()
        excepted_client = repo.clients
        assert excepted_client == clients

    def test_deposit_money(self):
            for transaction

 def test_deposit_current_balance(self):
                for transaction in self.transaction:
                        if transaction.type_transaction == TRANSACTIONS_TYPE_ENUM.DEPOSIT:
                                expected_current_balance = self.user.current_balance + transaction.value
                                assert self.user.current_balance + transaction.value == expected_current_balance
        
        def test_withdraw_current_balance(self):
                for transaction in self.transaction:
                        if transaction.type_transaction == TRANSACTIONS_TYPE_ENUM.WITHDRAW:
                                expected_current_balance = self.user.current_balance - transaction.value
                                assert self.user.current_balance - transaction.value == expected_current_balance
        

# class Test_ItemRepositoryMock:
#     def test_get_all_items(self):
#         repo = ItemRepositoryMock()
#         assert all([item_expect == item for item_expect, item in zip(repo.items.values(), repo.get_all_items())]) 
        
#     def test_get_item(self):
#         repo = ItemRepositoryMock()
#         item = repo.get_item(item_id=1)
#         assert item == repo.items.get(1)
    
#     def test_get_item_not_found(self):
#         repo = ItemRepositoryMock()
#         item = repo.get_item(item_id=10)
#         assert item is None
        
#     def test_create_item(self):
#         repo = ItemRepositoryMock()
#         len_before = len(repo.items)
#         item = Item(name="test", price=1.0, item_type=ItemTypeEnum.TOY, admin_permission=False)
#         repo.create_item(item=item, item_id=0)
#         len_after = len(repo.items)
#         assert len_after == len_before + 1
#         assert repo.items.get(0) == item
        
#     def test_delete_item(self):
#         repo = ItemRepositoryMock()
#         item_expected_to_be_deleted = repo.items.get(1)
#         len_before = len(repo.items)
        
#         item = repo.delete_item(item_id=1)
#         len_after = len(repo.items)
#         assert len_after == len_before - 1
#         assert item == item_expected_to_be_deleted
        
#     def test_delete_item_not_found(self):
#         repo = ItemRepositoryMock()
#         item = repo.delete_item(item_id=10)
#         assert item is None
        
#     def test_update_item(self):
#         repo = ItemRepositoryMock()
#         item = Item(name="test", price=1.0, item_type=ItemTypeEnum.TOY, admin_permission=False)
#         item_updated = repo.update_item(item_id=1, name=item.name, price=item.price, item_type=item.item_type, admin_permission=item.admin_permission)
        
#         assert item_updated == item
#         assert repo.items.get(1) == item
        
#     def test_update_item_partial_1(self):
#         repo = ItemRepositoryMock()
#         name = "test"
#         item_updated = repo.update_item(item_id=1, name=name)
        
#         assert item_updated.name == name
#         assert repo.items.get(1).name == name
        
#     def test_update_item_partial_2(self):
#         repo = ItemRepositoryMock()
#         price = 1.0
#         item_updated = repo.update_item(item_id=1, price=price)
        
#         assert item_updated.price == price
#         assert repo.items.get(1).price == price