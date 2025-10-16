"""This module defines the PenaltyStrategy class."""

__author__ = "Sania Parvej"
__version__ = "1.0.0"

from .payment_strategy import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PenaltyStrategy(PaymentStrategy):
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        # Deduct the payment amount from the payee account
        account.deduct_balance(payee, amount)
        
        # Get the updated balance
        updated_balance = account.get_balance(payee)
        
       # confirminng payment
        if updated_balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        
       #Adding penalty if not paid fully with a return messagw
        else:
            account.add_balance(payee, 10.00)
            new_total = account.get_balance(payee)
            return f"Insufficient payment!. A $10.00 penalty has been added. New balance: ${new_total:.2f}."