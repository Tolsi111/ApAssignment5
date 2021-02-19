from classPassanger import Passanger
import logic as l

class PassangerRepository:
    '''
    This class manages a passanger repository. A list of objects of type "Passanger"
    '''
    def __init__(self):
        self.__data = []
    
    def getData(self):
        return self.__data

    #CRUD operations
    def createPassanger(self,firstName,lastName,passportNumber):
        '''
        creates and adds a new object of type "Passanger" to the repository
        '''
        self.__data.append(Passanger(firstName,lastName,passportNumber))
    
    def getPassanger(self,index):
        '''
        returns the object at index "index" from the list "self"
        '''
        return self.__data[index]

    def readPassanger(self,index):
        '''
        prints the object at index "index" from the list "self"
        '''
        print(self.getPassanger(index))

    def uppdatePassanger(self,index,newPassanger):
        '''
        uppdates the passanger...
        at the index "index" from the repository "self" with the object "newPassanger" of type "Passanger"
        '''
        self.__data[index] = newPassanger

    def deletePassanger(self,index):
        '''
        delets the object at index "index" from the list "self"
        '''
        del(self.__data[index])
    
    #ITERATION 2
    def sortByLastName(self):#i2p1
        '''
        sorts the passengers in a plane by last name using bubble sort :) decreasing
        '''
        def cond(a,b):
            return a.getLastName() < b.getLastName()
        l.mySort(self.getData(),cond)



