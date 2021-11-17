import sys

from .elevator import Elevator
from models.simulator import simulator
from models.call import Call


class ElevatorManager:
    def __init__(self, elevator: Elevator , time_for_sim):
        self.elevator = elevator
        self.calls = []
        self.time_for_sim = time_for_sim


    def add(self,c):
        self.calls.append(c)


    def estimated_time_to(self, c):
        # print('--------------')
        new_calls = self.calls.copy()
        new_calls.append(c)
        new_calls.sort()
        s = simulator(self.elevator)
        time = s.get_elevator_state_at(self.time_for_sim, new_calls.copy(), c)

        # print(f'time for simulation {time}',self.time_for_sim)
        # print('--------------')

        for c in new_calls:
            c.picked = False
            c.src_time = None
            c.dest_time = None


        return time


