from classPassangerRepo import PassangerRepository
from classPassanger import Passanger
import logic as l

class Plane:

    def __init__(self,ID,company,seats,destination,passangersRepo):
        self.__id = ID
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passangers = passangersRepo
    
    def getID(self):
        return self.__id
    def setID(self,newID):
        self.__id = newID

    def getCompany(self):
        return self.__company
    def setCompany(self,newCompany):
        self.__company = newCompany

    def getSeats(self):
        return self.__seats
    def setSeats(self,newSeats):
        self.__id = newSeats

    def getDestination(self):
        return self.__destination
    def setDestination(self,newDestination):
        self.__id = newDestination

    def getPassangers(self):
        return self.__passangers
    def setPassangers(self,newPassangers):
        self.__id = list(newPassangers)

    def __str__(self):
        msg = "Plane " + str(self.__id) + " from " + self.__company + " with destination " + self.__destination + " and " + str(self.__seats) + " seats"
        msg += "\n"
        msg += "Passangers: \n"
        for elem in self.__passangers.getData():
            msg += str(elem) + "\n"
        return msg

    #ITERATION 2
    def getNbPassangersStartString(self,s):
        '''
        returns the number of passangers whose names start with a given string "s"
        '''
        result = 0
        for passanger in self.getPassangers().getData():
            if passanger.getFirstName()[:len(s)] == s:
                result += 1
        return result

    def getConcatenationNbDestination(self):
        '''
        returns the string obtained by concatenation of the number of passengers in the plane and the destination
        '''
        return str(len(self.__passangers.getData())) + self.__destination

    def checkPassengersPassport3Numbers(self,a):
        '''
        checks if there is at least one passenger with passport number starting with the same 3 letters "a"
        a = a 3-digit int
        returns True or False
        '''
        for elem in self.getPassangers().getData():
            if str(l.first3Digits(elem.getPassportNumber())) == str(a):
                return True
        return False

    def passangersStringInName(self,s):#given by index in the PlaneRepo
        '''
        Identifies passengers from a given plane for which the first name or last name contain a string given as parameter
        '''
        def cond(self,s):
            if s in self.getFirstName() or s in self.getLastName() :
                return True
            return False
        return l.mySearch(self.getPassangers().getData(),cond,s)

    #ITERATION 3
    def groupsOfPassangers(self,k):
        '''
        Forms groups of k passengers from the same plane but with different last names (k is a value given by the user)
        and prints it

        The domain would be 'self.getPassangers().getData()' meaning the passanger repository of this plane
        '''
        n = len(self.getPassangers().getData())
        e = False
        if k <= n:
            def cond(a,b):#the required contition for the groups
                return a.getLastName() != b.getLastName()
            for p in l.myBracktrackingRec(n,k,[],self.getPassangers().getData(),cond):#generate every solution
                l.printSolution(p,self.getPassangers().getData())#print every solution
                e = True
        if not e:
            print("No group could be formed")
            
        