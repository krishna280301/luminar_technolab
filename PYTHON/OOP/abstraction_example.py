from abc import ABC
class bike(ABC):
    def start(self):
        pass
    def breaks(self):
        pass
    def accelerate(self):
        pass

class hunter(bike):
    pass
obj=hunter()
obj.start()


