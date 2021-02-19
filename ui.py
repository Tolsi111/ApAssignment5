'''
This is the UI layer
'''
def displayNotes():
    msg = "Hi and welcome to my third app. \n"
    msg +="Considering an airport, there are several planes \n(identified by name/number, airline company, number of seats, destination, list of passengers) \nand each plane has certain passengers (identified by first name, last name and passport number). \n"
    msg +="To facilitate the usage and testing of the app, i divided it into 3 operations: \n"
    msg +="Sorting operations, searching operations and forming groups operations \n"
    print(msg)
def displayMenu():
    msg = "Menu: \n"
    msg +="\t 1 - Sort... \n"
    msg +="\t 2 - Search... \n"
    msg +="\t 3 - Form groups... \n"
    msg +="\t 4 - Print the repository... \n"
    msg +="\t 0 - Exit \n"
    print(msg)
def option1():#Sort
    msg = "You have chosen option 1, now choose an operation: \n"
    msg +="\t a) - Sort the passengers in a plane by last name \n"#i2p1
    msg +="\t b) - Sort planes according to the number of passengers \n"#i2p2
    msg +="\t c) - Sort planes according to the number of passengers with the first name starting with a given substring \n"#i2p3
    msg +="\t d) - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination \n"#i2p4
    msg +="\t 0 - Back to menu \n"
    print(msg)    
def option2():#Search
    msg = "You have chosen option 2, now choose an operation: \n"
    msg +="\t a) - Identify planes that have passengers with passport numbers starting with the same 3 letters \n"#i2p5
    msg +="\t b) - Identify passengers from a given plane for which the first name or last name contain a string given as parameter \n"#i2p6
    msg +="\t c) - Identify plane/planes where there is a passenger with given name \n"#i2p7
    msg +="\t 0 - Back to menu \n"
    print(msg) 
def option3():#Groups
    msg = "You have chosen option 3, now choose an operation: \n"
    msg +="\t a) - Form groups of k passengers from the same plane but with different last names (k is a value given by the user) \n"#i3p1
    msg +="\t b) - Form groups of k planes with the same destination but belonging to different airline companies \n"#i3p1
    msg +="\t 0 - Back to menu \n"
    print(msg)