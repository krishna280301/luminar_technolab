# class=is a design (eg:buidling,land,plan,template)
# only attributes and meathods in class
# object= used to build or design or produce using class
# meathods=what all a thing can do 
# objecy=car,meathods=drive,drift,race
# attributes=what all a thing have
# object=car,attributes=doore,engine,mirror,seat

# java,c++= constructor name is same as class name
# javascript = constructor name is constructor()
# python = constructor name is __init__

# constructor initialises instance variable
# __class__ to print class name 
# SUPER is used to refer parent class and print both elements in parent and child class


#CREATING A CLASS
class employee:
    id:int
    name:str
    gender:str  #TYPE HIND ( NOT NECESSARY )
    salary:int
    department:str

    def create(self,id,name,grnder,slry,dept): #create USED TO INITIALISE INSTANCE VARIABLE
        self.id=id
        self.name=name
        self.gender=grnder  #INSTANCE VARIABLES
        self.salary=slry
        self.department=dept
    
    def get(self):
        print(self.id,self.name,self.gender,self.department,self.salary) #CLASS CREATION COMPLETE
    
#CREATING OBJECT
emp1=employee()
emp2=employee()
emp1.create(10,"kp","male",100000,"IT")
emp2.create(11,"milana","female",200000,"HR") #OBJECT CREATION COMPLETE

emp1.get()
emp2.get()



