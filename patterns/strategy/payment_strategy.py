"""This module defines the PaymentStrategy class."""

__author__ = "Sania Parvej"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        pass
