import pytest
from src.app.entities.transaction import Transactions
from src.app.enums.transaction_enum import transaction_enum
from src.app.errors.entity_errors import ParamNotValidated

class Test_Transactions:
    def test_transactions(self):
        type_transaction =  transaction_enum.WITHDRAW
        value = 500.00
        balance = 1000.00
        time = 1012983522.00

        transaction = Transactions(type_transaction, value, balance, time)
        assert transaction.type_transaction ==  transaction_enum.WITHDRAW
        
    def test_validate_balance(self):
        balance = "1000.00"

        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.DEPOSIT.value, 500.00, balance, 1012983522.00)

        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.WITHDRAW.value,
            1000.00, balance, 1012983522.00)
    
    def test_validate_time(self):
        time = "1012983522.00"

        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.DEPOSIT.value, 500.00, 1000.00, time)

        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.WITHDRAW.value, 500.00, 1000.00, time)
            
    def test_validate_value(self):
        value = "500.00"

        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.DEPOSIT.value, value, 1000.00, 1012983522.00)


    def test_validate_negative_value(self):
        value = -500.00

        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.DEPOSIT.value, value, 1000.00, 1012983522.00)
        
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_enum.WITHDRAW.value,
            value, 1000.00, 1012983522.00)
