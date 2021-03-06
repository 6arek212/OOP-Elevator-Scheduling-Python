import unittest

from models.call import Call
from models.elevator import Elevator
from simulator import Simulator


class SimulatorTest(unittest.TestCase):

    def test_start_simulation(self):
        simulator = Simulator(
            elevator=Elevator(id=1, speed=2, max_floor=10, min_floor=0, close_time=2, open_time=2, start_time=2,
                              stop_time=2))
        calls = [Call(0, 5, 1, 0)]

        new_call = Call(5, 6, 1, 0)
        time = simulator.start_simulation(till_time=21, calls=calls + [new_call], new_call=new_call)
        self.assertEqual((5 / 2 + 2 * 4 + 1) + (1 / 2) + 2 * 4 + 1, time)

    def test_get_next(self):
        simulator = Simulator(
            elevator=Elevator(id=1, speed=2, max_floor=10, min_floor=0, close_time=2, open_time=2, start_time=2,
                              stop_time=2))

        simulator.add(Call(0, 5, 1, 0))
        next = simulator.get_next()
        self.assertEqual(next, 5)

    def test_add(self):
        simulator = Simulator(
            elevator=Elevator(id=1, speed=2, max_floor=10, min_floor=0, close_time=2, open_time=2, start_time=2,
                              stop_time=2))

        simulator.add(Call(0, 5, 1, 0))
        self.assertEqual(len(simulator.calls), 1)
