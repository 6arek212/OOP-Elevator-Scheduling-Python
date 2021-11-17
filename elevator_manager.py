from models.elevator import Elevator
from simulator import Simulator


class ElevatorManager:
    def __init__(self, elevator: Elevator , time_for_sim):
        self.elevator = elevator
        self.calls = []
        self.time_for_sim = time_for_sim


    def add(self,c):
        self.calls.append(c)


    def estimated_time_with(self, c):
        '''
        :param c: call to evaluate
        :return: the estimated time that this call adds to the overall elevator time
        '''
        new_calls = self.calls.copy()
        new_calls.append(c)
        new_calls.sort()
        s = Simulator(self.elevator)
        time = s.start_simulation(self.time_for_sim, new_calls.copy(), c)

        for c in new_calls:
            c.picked = False
            c.src_time = None
            c.dest_time = None

        return time


