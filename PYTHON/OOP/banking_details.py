class bank:
    bank_name:str
    branch:str
    account_number:int
    ifsc_code:str
    person_name:str
    account_type:str
    balance:int

    def create(self,name,branch,ac_num,ifsc,person,ac_type,bal):
        self.bank_name=name
        self.branch=branch
        self.account_number=ac_num
        self.ifsc_code=ifsc
        self.person_name=person
        self.account_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"YOUR {self.bank_name} ACCOUNT HAS BEEN CREDIT WITH RS: {amount}, YOUR NEW BALANCE IS {self.balance}")
    
    def withdraw(self,amount):
        if(amount>self.balance):
            print(f"YOUR {self.bank_name} ACCOUNT HAS INSUFFICIENT BALANCE, TRANSACTION REJECTED, AVAILABLE BALANCE IS {self.balance}")
        else:
            self.balance-=amount
            print(f"YOUR {self.bank_name} IS DEBITED BY {amount}, AVAILABLE BALANCE IS {self.balance}")
    
    def get(self):
        print(self.bank_name,self.branch,self.account_number,self.ifsc_code,self.person_name,self.account_type,self.balance)


id1=bank()
id1.create("STATE BANK of INDIA","EDAPPALLY",200021077031,"SBIN0012","KRISHNA PRASAD","SAVINGS",180000)
id1.get()
# id1.deposit(2)
# id1.withdraw(200000)