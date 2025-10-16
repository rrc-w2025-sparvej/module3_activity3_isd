"""This module defines the Payment class."""

__author__ = "Sania Parvej"
__version__ = "1.0.0"

from patterns.strategy.payment_strategy  import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class Payment:
    def __init__(self, strategy: PaymentStrategy):
        #If the value is of PaymentStrategy
        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        #If the value is is not of PaymentStrategy, raise a ValueError
        else:
            raise ValueError("Invalid Strategy")
        
    def pay_bill(self, account: BillingAccount, payee: Payee, amount: float) -> str:
       
        return self.__strategy.process_payment(account, payee, amount)