import sys

from .elevator import Elevator
from .call import Call


class simulator:
    def __init__(self, elevator):
        self.elevator = elevator
        self.elevator_pos = 0
        self.direction = Elevator.LEVEL
        self.calls = []
        self.time = 0

    def add(self, c: Call):
        # print(f'call got added {c.src} --> {c.dest}  direction {c.direction}')
        if self.direction == Elevator.LEVEL:
            if c.src == self.elevator_pos:
                self.direction = c.direction
            if c.src > self.elevator_pos:
                self.direction = Elevator.UP
            else:
                self.direction = Elevator.DOWN
        self.calls.append(c)

    def get_next_up_calls(self, elv_pos=None):
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
        for c in self.calls:
            if c.direction == Elevator.DOWN and c.src == self.elevator_pos:
                c.picked = True
                c.src_time = self.time

        if elv_pos is not None:
            calls_up = []
            for c in self.calls:
                if c.direction == Elevator.DOWN and c.src <= elv_pos and not c.picked:
                    calls_up.append(c.src)

                if c.direction == Elevator.DOWN and c.dest <= elv_pos and c.picked:
                    calls_up.append(c.dest)

            calls_up.sort(reverse=True)
            if not calls_up:
                return None
            return calls_up[0]
        else:
            calls_up = []
            for c in self.calls:
                if c.direction == Elevator.DOWN and not c.picked:
                    calls_up.append(c.src)

                if c.direction == Elevator.DOWN and c.picked:
                    calls_up.append(c.dest)

            calls_up.sort(reverse=True)
            if not calls_up:
                return None
            return calls_up[0]

    def get_next(self):
        if not self.calls:
            self.direction = Elevator.LEVEL
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

        if dd is not None:
            if dd >= self.elevator_pos:
                self.direction = Elevator.UP
            else:
                self.direction = Elevator.DOWN

        return dd

    def cmd(self):
        next = self.get_next()
        while next is not None and next == self.elevator_pos:
            next = self.get_next()
        # print(f'next is {next}')
        # print(f'current floor is {self.elevator_pos}   direction {self.direction}')

        if next is None:
            return

        if self.direction == Elevator.UP and self.elevator_pos < self.elevator.max_floor:
            if self.elevator_pos + self.elevator.speed >= next:
                self.elevator_pos = next
            else:
                self.elevator_pos += self.elevator.speed


        elif self.direction == Elevator.DOWN and self.elevator_pos > self.elevator.min_floor:
            if self.elevator_pos - self.elevator.speed <= next:
                self.elevator_pos = next
            else:
                self.elevator_pos -= self.elevator.speed

    def get_elevator_state_at(self, till_time, calls: [], new_call : Call):
        # print(f'simulation starting start pos {self.elevator_pos}  start direction {self.direction} elevator {self.elevator.id}')
        last_elevator_level = []

        while self.time < till_time:
            # print('-----')
            if self.direction == Elevator.LEVEL:
                last_elevator_level.append(self.time)

            if new_call.dest_time is not None and self.direction == Elevator.LEVEL:
                x = last_elevator_level[len(last_elevator_level)-2]
                print(self.time,x)
                return self.time - x

            for c in calls:
                if c.time_coming <= self.time:
                    self.add(c)
                    calls.remove(c)

            # print('[')
            # for c in self.calls:
            #     print(f'{c.src} -> {c.dest} , ')
            # print(']')

            self.cmd()
            # print('-----')
            self.time += 1

        if new_call.dest_time is None:
            return sys.maxsize

        return self.time - new_call.time_coming
