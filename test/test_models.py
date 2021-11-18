import unittest

from models.building import Building
from models.call import Call


class Elevator_test(unittest.TestCase):

    def test_init_from_file(self):
        building = Building.init_from_file(f'../data/Ex1_input/Ex1_Buildings/B5.json')
        self.assertNotEqual(building,None)





class Call_test(unittest.TestCase):

    def test_init_from_file(self):
        calls = Call.init_from_file(f'../data/Ex1_input/Ex1_Calls/Calls_a.csv')
        self.assertNotEqual(calls,None)
