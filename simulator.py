import sys

from models.elevator import Elevator
from models.call import Call


class simulator:
    '''
        this a simulator to mimc the tester behavior
        using the Elevator Algorithm
    '''

    def __init__(self, elevator):
        self.elevator = elevator
        self.elevator_pos = 0
        self.direction = Elevator.LEVEL
        self.calls = []
        self.time = 0

    def add(self, c: Call):
        if self.direction == Elevator.LEVEL:
            if c.src == self.elevator_pos:
                self.direction = c.direction
            if c.src > self.elevator_pos:
                self.direction = Elevator.UP
            else:
                self.direction = Elevator.DOWN
        self.calls.append(c)

    def get_next_up_calls(self, elv_pos=None):
        '''
            get the next up destination for the elevator
        :param elv_pos: the current elevator posetion
        :return: next up destination
        '''
        for c in self.calls:
            if c.direction == Elevator.UP and c.src == self.elevator_pos:
                c.picked = True
                c.src_time = self.time

        if elv_pos is not None:
            calls_up = []
            for c in self.calls:
                if c.direction == Elevator.UP and c.src >= elv_pos and not c.picked:
                    calls_up.append(c.src)

                if c.direction == Elevator.UP and c.dest >= elv_pos and c.picked:
                    calls_up.append(c.dest)

            calls_up.sort()
            if not calls_up:
                return None
            return calls_up[0]
        else:
            calls_up = []
            for c in self.calls:
                if c.direction == Elevator.UP and not c.picked:
                    calls_up.append(c.src)

                if c.direction == Elevator.UP and c.picked:
                    calls_up.append(c.dest)

            calls_up.sort()
            if not calls_up:
                return None
            return calls_up[0]

    def get_next_down_calls(self, elv_pos=None):

        '''
           get the next down destination for the elevator
           :param elv_pos: the current elevator posetion
           :return: next down destination
        '''

        for c in self.calls:
            if c.direction == Elevator.DOWN and c.src == self.elevator_pos:
                c.picked = True
                c.src_time = self.time

        if elv_pos is not None:
            calls_down = []
            for c in self.calls:
                if c.direction == Elevator.DOWN and c.src <= elv_pos and not c.picked:
                    calls_down.append(c.src)

                if c.direction == Elevator.DOWN and c.dest <= elv_pos and c.picked:
                    calls_down.append(c.dest)

            calls_down.sort(reverse=True)
            if not calls_down:
                return None
            return calls_down[0]
        else:
            calls_down = []
            for c in self.calls:
                if c.direction == Elevator.DOWN and not c.picked:
                    calls_down.append(c.src)

                if c.direction == Elevator.DOWN and c.picked:
                    calls_down.append(c.dest)

            calls_down.sort(reverse=True)
            if not calls_down:
                return None
            return calls_down[0]

    def get_next(self):
        '''
        :return: next destination
        '''
        if not self.calls:
            return None

        for c in self.calls:
            if c.picked and self.elevator_pos == c.dest:
                self.calls.remove(c)
                c.dest_time = self.time

        if self.direction == Elevator.UP:
            dd = self.get_next_up_calls(self.elevator_pos)
            if dd is None:
                dd = self.get_next_down_calls()
            if dd is None:
                dd = self.get_next_up_calls()
            if dd is None:
                return None
        else:
            dd = self.get_next_down_calls(self.elevator_pos)
            if dd is None:
                dd = self.get_next_up_calls()
            if dd is None:
                dd = self.get_next_down_calls()
            if dd is None:
                return None
        return dd

    def cmd(self):
        '''
            move the elevator depending on its speed and next destination
        :return:
        '''

        next = self.get_next()
        while next is not None and next == self.elevator_pos:
            next = self.get_next()

        start_time = False

        if next is None:
            self.direction = Elevator.LEVEL
            return
        else:
            if next == Elevator.LEVEL:
                start_time = True

            if next > self.elevator_pos:
                self.direction = Elevator.UP
            else:
                self.direction = Elevator.DOWN

        if self.direction == Elevator.UP and self.elevator_pos < self.elevator.max_floor:
            if self.elevator_pos + self.elevator.speed >= next:
                self.time += self.elevator.stop_time + self.elevator.open_time
                self.elevator_pos = next
            else:
                if start_time:
                    self.time += self.elevator.close_time + self.elevator.start_time
                self.elevator_pos += self.elevator.speed


        elif self.direction == Elevator.DOWN and self.elevator_pos > self.elevator.min_floor:
            if self.elevator_pos - self.elevator.speed <= next:
                self.time += self.elevator.stop_time + self.elevator.open_time
                self.elevator_pos = next
            else:
                if start_time:
                    self.time += self.elevator.close_time + self.elevator.start_time
                self.elevator_pos -= self.elevator.speed

    def start_simulation(self, till_time, calls: [], new_call: Call):
        '''
            spining up the simulation
        :param till_time: the time till the simulation end
        :param calls: the calls for simulation
        :param new_call: the new call to evaluate
        :return: the time from the latest Elevator stop to the next Elevator stop and the new call is Done
        '''
        last_elevator_level = []

        while self.time < till_time:
            if self.direction == Elevator.LEVEL:
                last_elevator_level.append(self.time)

            if new_call.dest_time is not None and self.direction == Elevator.LEVEL:
                x = last_elevator_level[len(last_elevator_level) - 2]
                return self.time - x

            for c in calls:
                if c.time_coming <= self.time:
                    self.add(c)
                    calls.remove(c)
            self.cmd()
            self.time += 1

        if new_call.dest_time is None:
            return sys.maxsize

        x = last_elevator_level[len(last_elevator_level) - 2]
        return self.time - x
