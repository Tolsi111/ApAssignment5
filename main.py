#I MADE THIS CHANGE
'''
Start the app from here
'''
from controller import Controller
from classPlaneRepository import PlaneRepository
from classPassangerRepo import PassangerRepository


airport = PlaneRepository()

#creating passanger repositories for the planes
a = PassangerRepository()
a.createPassanger("Andrei","Pop",2003)

b = PassangerRepository()
b.createPassanger("Andrei","Pop",2003)
b.createPassanger("Romulus","Bacila",2201)
b.createPassanger("Darius","Bacila",2000)
b.createPassanger("Razvan","Dac",2202)

c = PassangerRepository()
c.createPassanger("Darius","Bacila",2000)
c.createPassanger("Razvan","Dac",2002)

d = PassangerRepository()
d.createPassanger("Darius","Bacila",2000)
d.createPassanger("Razvan","Dac",2012)
d.createPassanger("Razvan","Dac",2002)

e = PassangerRepository()
e.createPassanger("Andrei","Pop",2003)
e.createPassanger("Romulus","Bacila",2001)
e.createPassanger("Darius","Bacila",4000)
e.createPassanger("Razvan","Dac",4002)

f = PassangerRepository()
f.createPassanger("Andrei","Pop",4003)
f.createPassanger("Romulus","Bacila",2011)
f.createPassanger("Darius","Bacila",2000)
f.createPassanger("Razvan","Alex",2012)
f.createPassanger("Razvan","Dac",2002)

#creating the planes given as example and for testing purposes
airport.createPlane(1,"WizzAir",300,"Malta",a)
airport.createPlane(2,"Tarom",100,"Cluj-Napoca",b)
airport.createPlane(3,"TurkishAirlines",100,"Malta",c)
airport.createPlane(4,"WizzAir",200,"Cluj-Napoca",d)
airport.createPlane(5,"Tarom",50,"Cluj-Napoca",e)
airport.createPlane(6,"TurkishAirlines",500,"Malta",f)


app = Controller(airport)

app.start()