class Passanger:

    def __init__(self,firstName,lastName,passportNumber):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__passportNumber = passportNumber

    def getFirstName(self):
        return self.__firstName
    def setFirstName(self,newFirstName):
        self.__firstName = newFirstName

    def getLastName(self):
        return self.__lastName
    def setLastName(self,newLastName):
        self.__lastName = newLastName

    def getPassportNumber(self):
        return self.__passportNumber
    def setPassportNumber(self,newPassportNumber):
        self.__passportNumber = newPassportNumber

    def __str__(self):
        return "Passanger " + self.__firstName + " " + self.__lastName + " with passport number " + str(self.__passportNumber)
    