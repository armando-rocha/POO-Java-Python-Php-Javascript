from car import Car

class UberBlack(Car):
    __typeCarAccepted =[]
    __seatsMaterial = []
    def __init__(self, id, driver ,license,passenger,typeCarAccepted,seatsMaterial):
        super().__init__(id,driver,license, passenger)
        self.__typeCarAccepted = typeCarAccepted
        self.__seatsMaterial = seatsMaterial
    
    def setTypeCarAccepted(self,typeCarAccepted):
        self.__typeCarAccepted=typeCarAccepted
    
    def getTypeCarAccepted(self):
        return self.__typeCarAccepted

    def setSeatsMaterial(self,seatsMaterial ):        
        self.__seatsMaterial
    
    def getSeatsMaterial(self):
        return self.__seatsMaterial

    def printDataCar(self):
        super().printDataCar()
        for item in self.typeCarAccepted:
            print(item)
        for item in self.setSeatsMaterial:
            print(item)