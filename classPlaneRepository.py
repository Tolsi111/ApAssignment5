from classPlane import Plane as Pl
import logic as l

class PlaneRepository:
    '''
    this class manages a planes repository. A list of objects of type "Plane", just like an airport :)
    '''
    def __init__(self):
        self.__data = []

    def getData(self):
        return self.__data

    #CRUD operations
    def createPlane(self,ID,company,seats,destination,passangersRepo):
        '''
        creates and adds a new object of type "Plane" to the repository
        '''
        self.__data.append(Pl(ID,company,seats,destination,passangersRepo))
    
    def getPlane(self,index):
        '''
        returns the object at index "index" from the list "self"
        '''
        return self.__data[index]

    def readPlane(self,index):
        '''
        prints the object at index "index" from the list "self"
        '''
        print(self.__data[index])

    def uppdatePlane(self,index,newPlane):
        '''
        uppdates the plane...
        at the index "index" from the repository "self" with the object "newPlane" of type "Plane"
        '''
        self.__data[index] = newPlane

    def deletePlane(self,index):
        '''
        delets the object at index "index" from the list "self"
        '''
        del(self.__data[index])
    
    #ITERATION 2
    def sortByPassangersNb(self):#i2p2
        '''
        Sorts the planes according to the number of passengers decreasing
        '''
        def cond(a,b):
            return len(a.getPassangers().getData()) > len(b.getPassangers().getData())
        l.mySort(self.getData(),cond)
    def sortByPassangerStartString(self,s):#i2p3
        '''
        Sorts the planes according to the number of passengers with the first name starting with a given substring "s"
        '''
        l.mySort(self.getData(),lambda x,y: x.getNbPassangersStartString(s) > y.getNbPassangersStartString(s))
    def sortByConcatenation(self):#i2p4
        '''
        Sorts yhe planes according to 
        the string obtained by concatenation of the number of passengers in the plane and the destination
        '''
        def cond(a,b):
            return a.getConcatenationNbDestination() > b.getConcatenationNbDestination()
        l.mySort(self.getData(),cond)
    def planesPassengersPassport3Numbers(self,a):#i2p5
        '''
        Identifies planes that have passengers with passport numbers starting with the same 3 letters "a"
        a = a 3-digit int
        returns the result list
        '''
        def cond(self,a):
            for elem in self.getPassangers().getData():
                if str(l.first3Digits(elem.getPassportNumber())) == str(a):
                    return True
            return False
        return l.mySearch(self.getData(),cond,a)
    
    def planePassangersStringInName(self,i,s):#i2p6
        '''
        Identify passengers from a given plane for which the first name or last name contain a string given as parameter
        Returns the result list
        '''
        return self.getPlane(i).passangersStringInName(s)

    def planePassangerName(self,name):#i2p7
        '''
        Identifies plane/planes where there is a passenger with given name
        returns a list
        '''
        def cond(self,name):
            for elem in self.getPassangers().getData():
                if elem.getFirstName() == name or elem.getLastName() == name:
                    return True
            return False
        return l.mySearch(self.getData(),cond,name)
    
    #ITERATION 3
    def groupsOfPlanes(self,k):
        '''
        Forms groups of k planes with the same destination but belonging to different airline
        companies (k is a value given by the user)
        '''
        n = len(self.__data)
        e = False
        if k <= n:
            def cond(a,b):
                return ( a.getDestination() == b.getDestination() ) and ( a.getCompany() != b.getCompany() )
            for p in l.myBracktrackingRec(n,k,[],self.__data,cond):
                l.printSolution(p,self.__data)#print every solution
                e = True
        if not e:
            print("No group could be formed")
