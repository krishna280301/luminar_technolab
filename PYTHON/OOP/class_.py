class bank:
    bank_name:str
    branch:str
    account_number:int
    ifsc_code:str
    person_name:str
    account_type:str
    balance:str

    def create(self,bank,branch,ac_no,ifsc,person,type,bal):
        self.bank_name:bank
        self.branch:branch
        self.account_number:ac_no
        self.ifsc_code:ifsc
        self.person_name:person
        self.account_type:type
        self.balance:bal
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} account is credited by RS {amount}")
    
    def withdraw(self,amount):
        if(amount<self.balance):
            self.balance-=amount
            print(f"your {self.bank_name} accont is debited by RS {amount}")
        else:
            print(f"your {self.bank_name} account has insufficient balance")
    
    def get(self):
        print(self.bank_name,self.branch,self.account_number,self.ifsc_code,self.person_name,self.account_type,self.balance)
    
id1=bank()
id1.create("STATE BANK OF INDIA","EDAPPALLY",200021077031,"SBIN0012","KRISHNAPRASAD CS","SAVINGS",30000)
id1.get()