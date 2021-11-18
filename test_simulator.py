import unittest

from models.building import Building
from models.call import Call
from models.elevator import Elevator
from simulator import Simulator

building = {
    'max_floor': 10,
    'min_floor': 0,
    'elevators': [
        Elevator(id=1, speed=2, max_floor=10, min_floor=0, close_time=2, open_time=2, start_time=2, stop_time=2)]
}

simulator = Simulator(
    elevator=Elevator(id=1, speed=2, max_floor=10, min_floor=0, close_time=2, open_time=2, start_time=2, stop_time=2))
calls = [Call(0, 5, 1, 0)]


class SimulatorTest(unittest.TestCase):

    def test_time(self):
        new_call = Call(5, 6, 1, 0)
        time = simulator.start_simulation(till_time=10, calls=calls + [new_call], new_call=new_call)
        self.assertEqual((5 / 2 + 2 * 4) + (1 / 2) + 2 * 4, time)
