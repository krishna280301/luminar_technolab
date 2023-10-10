from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def fund_transfer(self):
        pass
    @abstractmethod
    def balance_enquiry(self):
        pass
    @abstractmethod
    def transaction_history(self):
        pass
class googlepay(bank):
    def fund_transfer(self):
        print("G-PAY fund transfer")
    def balance_enquiry(self):
        print("G-PAY balance enquiry")
    def transaction_history(self):
        print("G-PAY transaction history")
class paytm(bank):
    def fund_transfer(self):
        print("PAY-TM fund transfer")
    def balance_enquiry(self):
        print("PAY-TM balance enquiry")
    def transaction_history(self):
        print("PAY-TM transaction history")

b1=googlepay()
b2=paytm()
b1.fund_transfer()
b2.transaction_history()
b1.balance_enquiry()
b2.fund_transfer()
