class bank:
    bank_name=str
    account_number=int
    person_name=str
    ifsc_code=str
    branch=str
    ac_type=str
    balance=int

    def create(self,name,number,pname,ifsc,branch,atype,bal):
        self.bank_name=name
        self.account_number=number
        self.person_name=pname
        self.ifsc_code=ifsc
        self.branch=branch
        self.ac_type=atype
        self.balance=bal
    def deposit(self,amount):
        self.balance+=amount
        print(f"YOUR {self.bank_name} ACCOUNT HAS BEEN CREDITED WITH {amount}, YOUR AVAILABLE BALANCE IS {self.balance}")
    def withdraw(self,amount):
        if(amount>self.balance):
            print(f"YOUR {self.bank_name} ACCOUNT HAS INSUFFICIENT BALANCE, TRANSACTION REJECTED")
        else:
            self.balance-=amount
            print(f"YOUR {self.bank_name} ACCOUNT HAS BEEN DEBITED WITH {amount}, YOUR AVAILABLE BALANCE IS {self.balance}")
    def get(self):
        print(self.bank_name,self.account_number,self.person_name,self.ifsc_code,self.branch,self.ac_type,self.balance)
id1=bank()
id2=bank()
id1.create("STATE BANK OF INDIA",200021077031,"KRISHNA PRASAD","SBIN0012","EDAPPALLY","SAVINGS",20000)
id2.create("FEDERAL BANK",200021077031,"MILANA ROY","FDIN2314","VAZHAKKALA","CURRENT",1000)
id1.get()
id2.get()
id1.deposit(10000)
id2.withdraw(25000)

