from classPassangerRepo import PassangerRepository as Prepo
from classPassanger import Passanger as P
from classPlane import Plane as Pl
from classPlaneRepository import PlaneRepository as Plrepo

import unittest

class Test_PassangerRepository(unittest.TestCase):
    '''
    testing for the PassangerRepository class methods
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    #CRUD testing
    def test_createPassanger(self):
        p = Prepo()
        p.createPassanger("Andrei","Bacila",2001)
        self.assertEqual(str(p.getPassanger(0)),str(P("Andrei","Bacila",2001)))
    
    def test_uppdatePassanger(self):
        p = Prepo()
        p.createPassanger("Andrei","Bacila",2001)
        p.createPassanger("Romulus","Bacila",2000)
        self.assertEqual(str(p.getPassanger(1)),str(P("Romulus","Bacila",2000)))
        p.uppdatePassanger(1,P("Romulus Andrei","Bacila",2001))
        self.assertEqual(str(p.getPassanger(1)),str(P("Romulus Andrei","Bacila",2001)))
    
    def test_deletePassanger(self):
        p = Prepo()
        p.createPassanger("Andrei","Bacila",2001)
        p.createPassanger("Romulus","Bacila",2000)
        self.assertEqual(len(p.getData()),2)
        p.deletePassanger(1)
        self.assertEqual(len(p.getData()),1)


    #ITERATION 2 testing
    def test_sortByLastName(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Romulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)
        self.assertEqual(str(p.getPassanger(0)),str(P("Andrei","Pop",2003)))
        self.assertEqual(str(p.getPassanger(1)),str(P("Romulus","Bacila",2001)))
        self.assertEqual(str(p.getPassanger(2)),str(P("Darius","Andrei",2000)))
        self.assertEqual(str(p.getPassanger(3)),str(P("Razvan","Dac",2002)))
        p.sortByLastName()
        self.assertEqual(str(p.getPassanger(0)),str(P("Darius","Andrei",2000)))
        self.assertEqual(str(p.getPassanger(1)),str(P("Romulus","Bacila",2001)))
        self.assertEqual(str(p.getPassanger(2)),str(P("Razvan","Dac",2002)))
        self.assertEqual(str(p.getPassanger(3)),str(P("Andrei","Pop",2003)))




class Test_Plane(unittest.TestCase):
    '''
    testing for the Plane class methods
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)


    #ITERATION 2 testing
    def test_getNbPassangersStartString(self):
        p = Prepo()
        plane = Pl(1,"Tarom",100,"Cluj-Napoca",p)
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Anmulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)
        self.assertEqual(plane.getNbPassangersStartString("An"),2)
        self.assertEqual(plane.getNbPassangersStartString("D"),1)
        self.assertEqual(plane.getNbPassangersStartString("K"),0)

    def test_getConcatenationNbDestination(self):
        p = Prepo()
        plane = Pl(1,"Tarom",100,"Cluj-Napoca",p)
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Anmulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)

        self.assertEqual(plane.getConcatenationNbDestination(),"4Cluj-Napoca")
        plane.getPassangers().deletePassanger(0)
        self.assertEqual(plane.getConcatenationNbDestination(),"3Cluj-Napoca")
    
    def test_checkPassengersPassport3Numbers(self):
        p = Prepo()
        plane = Pl(1,"Tarom",100,"Cluj-Napoca",p)
        p.createPassanger("Andrei","Pop",2013)
        p.createPassanger("Anmulus","Bacila",1001)
        self.assertEqual(plane.checkPassengersPassport3Numbers(201),True)
        self.assertEqual(plane.checkPassengersPassport3Numbers(200),False)
        self.assertEqual(plane.checkPassengersPassport3Numbers(202),False)
        self.assertEqual(plane.checkPassengersPassport3Numbers(100),True)

    def test_passangersStringInName(self):
        p = Prepo()
        plane = Pl(1,"Tarom",100,"Cluj-Napoca",p)
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Anmulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Daci",2002)
        self.assertEqual(len(plane.passangersStringInName("Da")),2)
        self.assertEqual(len(plane.passangersStringInName("An")),3)
        self.assertEqual(len(plane.passangersStringInName("r")),2)
        self.assertEqual(len(plane.passangersStringInName("a")),3)
        self.assertEqual(len(plane.passangersStringInName("i")),4)
        self.assertEqual(len(plane.passangersStringInName("Some Random String")),0)

    #ITERATION 3 TESTING
    def test_groupsOfPassangers(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Romulus","Bacila",2001)
        p.createPassanger("Darius","Bacila",2000)
        p.createPassanger("Razvan","Dac",2002)
        Plane = Pl(1,"Tarom",100,"Cluj-Napoca",p)
        #Plane.groupsOfPassangers(4)




class Test_PlaneRepository(unittest.TestCase):
    '''
    testing for the PlaneRepository class methods
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    #CRUD testing
    def test_createPlane(self):
        p = Prepo()
        p.createPassanger("Andrei","Bacila",2001)
        p.createPassanger("Romulus","Bacila",2000)
        PlaneRepo = Plrepo()
        self.assertEqual(len(PlaneRepo.getData()),0)
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",p)
        self.assertEqual(len(PlaneRepo.getData()),1)
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(1,"Tarom",100,"Cluj-Napoca",p)))
    
    def test_uppdatePlane(self):
        p = Prepo()
        p.createPassanger("Andrei","Bacila",2001)
        p.createPassanger("Romulus","Bacila",2000)
        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",p)
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(1,"Tarom",100,"Cluj-Napoca",p)))
        newPlane = Pl(2,"WizzAir",200,"Malta",p)
        PlaneRepo.uppdatePlane(0,newPlane)
        self.assertNotEqual(str(PlaneRepo.getPlane(0)),str(Pl(1,"Tarom",100,"Cluj-Napoca",p)))
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(2,"WizzAir",200,"Malta",p)))
    
    def test_deletePlane(self):
        p = Prepo()
        p.createPassanger("Andrei","Bacila",2001)
        p.createPassanger("Romulus","Bacila",2000)
        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",p)
        PlaneRepo.createPlane(2,"WizzAir",200,"Malta",p)
        self.assertEqual(len(PlaneRepo.getData()),2)
        PlaneRepo.deletePlane(0)
        self.assertEqual(len(PlaneRepo.getData()),1)
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(2,"WizzAir",200,"Malta",p)))
    

    #ITERATION 2 testing
    def test_sortByPassangersNb(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Romulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)

        q = Prepo()
        q.createPassanger("Romulus","Bacila",2001)
        q.createPassanger("Darius","Andrei",2000)
        q.createPassanger("Razvan","Dac",2002)

        r = Prepo()
        r.createPassanger("Romulus","Bacila",2001)

        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(2,"WizzAir",200,"Malta",q)#3
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",r)#1
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Madird",p)#4
        self.assertEqual(len(PlaneRepo.getData()),3)
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(2,"WizzAir",200,"Malta",q)))
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(1,"Tarom",100,"Cluj-Napoca",r)))
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(3,"TurkishAirlines",300,"Madird",p)))

        PlaneRepo.sortByPassangersNb()

        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(3,"TurkishAirlines",300,"Madird",p)))
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(2,"WizzAir",200,"Malta",q)))
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(1,"Tarom",100,"Cluj-Napoca",r)))
    
    def test_sortByPassangerStartString(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Anmulus","Bacila",2001)
        p.createPassanger("Anrius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)

        q = Prepo()
        q.createPassanger("Romulus","Bacila",2001)
        q.createPassanger("Rrius","Andrei",2000)
        q.createPassanger("Razvan","Dac",2002)

        r = Prepo()
        r.createPassanger("Anomulus","Bacila",2001)

        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(1,"WizzAir",200,"Malta",p)
        PlaneRepo.createPlane(2,"Tarom",100,"Cluj-Napoca",q)
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Madird",r)

        PlaneRepo.sortByPassangerStartString("An")
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(1,"WizzAir",200,"Malta",p)))
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(3,"TurkishAirlines",300,"Madird",r)))
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(2,"Tarom",100,"Cluj-Napoca",q)))

        PlaneRepo.sortByPassangerStartString("R")
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(2,"Tarom",100,"Cluj-Napoca",q)))
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(1,"WizzAir",200,"Malta",p)))
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(3,"TurkishAirlines",300,"Madird",r)))

    def test_sortByConcatenation(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Romulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)

        q = Prepo()
        q.createPassanger("Romulus","Bacila",2001)
        q.createPassanger("Darius","Andrei",2000)
        q.createPassanger("Razvan","Dac",2002)

        r = Prepo()
        r.createPassanger("Romulus","Bacila",2001)

        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(2,"WizzAir",200,"Malta",q)
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",r)
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Madird",p)
        self.assertEqual(len(PlaneRepo.getData()),3)
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(2,"WizzAir",200,"Malta",q)))#3
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(1,"Tarom",100,"Cluj-Napoca",r)))#1
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(3,"TurkishAirlines",300,"Madird",p)))#4

        PlaneRepo.sortByConcatenation()
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(3,"TurkishAirlines",300,"Madird",p)))
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(2,"WizzAir",200,"Malta",q)))
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(1,"Tarom",100,"Cluj-Napoca",r)))

    def test_planesPassengersPassport3Numbers(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Romulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",1005)
        p.createPassanger("Razvan","Dac",4002)

        q = Prepo()
        q.createPassanger("Romulus","Bacila",1001)
        q.createPassanger("Darius","Andrei",1000)
        q.createPassanger("Razvan","Dac",2002)

        r = Prepo()
        r.createPassanger("Romulus","Bacila",2001)

        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(2,"WizzAir",200,"Malta",q)
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",r)
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Madird",p)
        self.assertEqual(len(PlaneRepo.getData()),3)
        self.assertEqual(str(PlaneRepo.getPlane(0)),str(Pl(2,"WizzAir",200,"Malta",q)))#3
        self.assertEqual(str(PlaneRepo.getPlane(1)),str(Pl(1,"Tarom",100,"Cluj-Napoca",r)))#1
        self.assertEqual(str(PlaneRepo.getPlane(2)),str(Pl(3,"TurkishAirlines",300,"Madird",p)))#4

        self.assertEqual(len(PlaneRepo.planesPassengersPassport3Numbers(200)),3)
        self.assertEqual(len(PlaneRepo.planesPassengersPassport3Numbers(100)),2)
        self.assertEqual(len(PlaneRepo.planesPassengersPassport3Numbers(400)),1)
        self.assertEqual(len(PlaneRepo.planesPassengersPassport3Numbers(500)),0)

    def test_planepassangersStringInName(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Anmulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Daci",2002)
        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Madird",p)
        self.assertEqual(len(PlaneRepo.getPlane(0).passangersStringInName("Da")),2)
        self.assertEqual(len(PlaneRepo.getPlane(0).passangersStringInName("An")),3)
        self.assertEqual(len(PlaneRepo.getPlane(0).passangersStringInName("r")),2)
        self.assertEqual(len(PlaneRepo.getPlane(0).passangersStringInName("a")),3)
        self.assertEqual(len(PlaneRepo.getPlane(0).passangersStringInName("i")),4)
        self.assertEqual(len(PlaneRepo.getPlane(0).passangersStringInName("Some Random String")),0)

    def test_planePassangerName(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        p.createPassanger("Romulus","Bacila",2001)
        p.createPassanger("Darius","Andrei",2000)
        p.createPassanger("Razvan","Dac",2002)

        q = Prepo()
        q.createPassanger("Romulus","Bacila",2001)
        q.createPassanger("Darius","Andrei",2000)
        q.createPassanger("Razvan","Dac",2002)

        r = Prepo()
        r.createPassanger("Romulus","Bacila",2001)
        r.createPassanger("Bogdan","Bacila",2001)

        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(2,"WizzAir",200,"Malta",q)
        PlaneRepo.createPlane(1,"Tarom",100,"Cluj-Napoca",r)
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Madird",p)
        self.assertEqual(len(PlaneRepo.getData()),3)
        self.assertEqual(len(PlaneRepo.planePassangerName("Andrei")),2)
        self.assertEqual(len(PlaneRepo.planePassangerName("Bogdan")),1)
        self.assertEqual(len(PlaneRepo.planePassangerName("Bacila")),3)
        self.assertEqual(len(PlaneRepo.planePassangerName("Random name")),0)
    
    #ITERATION 3 TESTING
    def test_groupsOfPlanes(self):
        p = Prepo()
        p.createPassanger("Andrei","Pop",2003)
        PlaneRepo = Plrepo()
        PlaneRepo.createPlane(1,"WizzAir",200,"Malta",p)
        PlaneRepo.createPlane(2,"Tarom",100,"Cluj-Napoca",p)
        PlaneRepo.createPlane(3,"TurkishAirlines",300,"Malta",p)
        PlaneRepo.createPlane(4,"WizzAir",200,"Cluj-Napoca",p)
        PlaneRepo.createPlane(5,"Tarom",100,"Cluj-Napoca",p)
        PlaneRepo.createPlane(6,"TurkishAirlines",300,"Malta",p)
        #PlaneRepo.groupsOfPlanes(2)



if __name__ == "__main__":
    unittest.main()
