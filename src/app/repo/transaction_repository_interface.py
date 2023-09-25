from abc import ABC, abstractmethod
from typing import List
from src.app.entities.transaction import Transactions

class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        #returs all Transactions
        pass

    def create_transaction(self, transaction: Transactions) -> Transactions:
        #create a Transaction
        pass