"""This module defines the PartialPaymentStrategy class."""

__author__ = "Sania Parvej"
__version__ = "1.0.0"

from .payment_strategy import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PartialPaymentStrategy(PaymentStrategy):
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        
        #Deduct the payment from the payee account
        account.deduct_balance(payee, amount)
        
        #Get the updated balance
        balance = account.get_balance(payee)

        #Check if the balance is paid fully or partially
        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."