#THE CONTROLLER LAYER SHOULDN'T TAKE ANY INPUT
'''
This module controlls everything in the app
'''
import ui
import logic as l

class Controller():
    def __init__(self,planeRepo):
        self.__airport = planeRepo
    def printRepo(self):
        for elem in self.__airport.getData():
            print(elem)

    def start(self):
        ui.displayNotes()
        print("Start...")
        while True:
            ui.displayMenu()
            option = input("Your option: ")
            if option == "1":#Sort
                while True:
                    ui.option1()
                    op = input("Your operation: ")
                    if op == "a":#Sort the passengers in a plane by last name   i2p1
                        i = l.validIndex(self.__airport.getData(),input("Index: "))
                        self.__airport.getPlane(i).getPassangers().sortByLastName()
                        break
                    elif op == "b":#Sort planes according to the number of passengers   i2p2
                        self.__airport.sortByPassangersNb()
                        break
                    elif op == "c":#Sort planes according to the number of passengers with the first name starting with a given substring   i2p3
                        self.__airport.sortByPassangerStartString(input("String: "))
                        break
                    elif op == "d":#Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination   i2p4
                        self.__airport.sortByConcatenation()
                        break
                    elif op == "0":#Back to menu
                        print("back")
                        break
                    else:
                        print("Please insert a valid operation :( \n")
            elif option == "2":#Search
                while True:
                    ui.option2()
                    op = input("Your operation: ")
                    if op == "a":#Identify planes that have passengers with passport numbers starting with the same 3 letters   i2p5 
                        ok = False
                        while not ok:#Forces the user to input a 3-digit positive number
                            a = input("3-digit positive number: ") 
                            a = l.validNumber(a)
                            ok = l.isThreeDigits(a)
                        for elem in self.__airport.planesPassengersPassport3Numbers(a):#printing the result
                            print(elem)
                        break
                    elif op == "b":#Identify passengers from a given plane for which the first name or last name contain a string given as parameter   i2p6
                        i = l.validIndex(self.__airport.getData(),input("Index: "))
                        for elem in self.__airport.planePassangersStringInName(i,input("String: ")):
                            print(elem)#printing the result
                        break
                    elif op == "c":#Identify plane/planes where there is a passenger with given name   i2p7 
                        for elem in self.__airport.planePassangerName(input("Name: ")):
                            print(elem)#printing the result
                        break
                    elif op == "0":#Back to menu
                        print("back")
                        break
                    else:
                        print("Please insert a valid operation :( \n")
            elif option == "3":#Form groups
                while True:
                    ui.option3()
                    op = input("Your operation: ")
                    if op == "a":#Form groups of k passengers from the same plane but with different last names (k is a value given by the user)   i3p1
                        k = l.validNumber(input("k= : "))
                        self.__airport.getPlane(l.validIndex(self.__airport.getData(),input("Index: "))).groupsOfPassangers(k)
                        break
                    elif op == "b":#Form groups of k planes with the same destination but belonging to different airline companies   i3p2
                        k = l.validNumber(input("k= : "))
                        self.__airport.groupsOfPlanes(k)
                        break
                    elif op == "0":#Back to menu
                        print("back")
                        break
                    else:
                        print("Please insert a valid operation :( \n")
            elif option == "4":#Print the repository
                self.printRepo()
            elif option == "0":
                print("Exit...")
                break
            else:
                print("Invalid option, please insert a valid option :( \n")
        print("End...")
