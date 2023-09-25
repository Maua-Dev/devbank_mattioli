from typing import List
from src.app.entities.transaction import Transactions
from ..enums.transaction_enum import transaction_enum
from ..repo.transaction_repository_interface import ITransactionRepository
import time

class TransactionRepositoryMock(ITransactionRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = [
            Transactions(transaction_enum.DEPOSIT, 250.00, 1250.00, time.time()*1234),
            Transactions(transaction_enum.WITHDRAW, 200.00, 1050.00, time.time()*1234),
        ]
    def create_transaction(self, transaction: Transactions) -> Transactions:
        self.transactions.append(transaction)
        return transaction    
    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
    
