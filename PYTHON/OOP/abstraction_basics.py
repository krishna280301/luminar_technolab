#ABSTRACTION
# abstraction is used to hide the implimentation details
# java and c++ uses 'interface' for this, python does not have 'interface'
# abstract classs will only have the meathod declaration


from abc import ABC,abstractmethod
class bike(ABC):
    @abstractmethod # @ is decorator
    def start(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class hunder(bike):
    def start(self):
        print("HUNDER STARTS")
    def accelarate(self):
        print("HUNDER ACCELERATES")
    def stop(self):
        print("HUNDER STOPS")
first=hunder()
first.start()
first.accelarate()
first.stop()