import sys

from .elevator import Elevator
from .call import Call


class simulator:
    def __init__(self, elevator, start_direction):
        self.elevator = elevator
        self.elevator_pos = 0
        self.elevator_mode = Elevator.LEVEL
        self.direction = start_direction
        self.active_calls = []
        self.up_calls = []
        self.down_calls = []



    def add(self, list, v):
        if not list.__contains__(v):
            list.append(v)


    def add_call_to_active(self, c: Call):
        if not self.active_calls:
            self.add(self.active_calls, c.src)
            # self.add(self.active_calls, c.dest)


        if c.direction == Elevator.UP and self.direction == Elevator.UP and self.elevator_pos <= c.src:
            self.add(self.active_calls , c.src)
            self.add(self.active_calls , c.dest)

        elif c.direction == Elevator.DOWN and self.direction == Elevator.DOWN and self.elevator_pos >= c.src:
            self.add(self.active_calls, c.src)
            self.add(self.active_calls, c.dest)


        elif c.direction == Elevator.UP:
            self.add(self.up_calls, c.src)
            self.add(self.up_calls, c.dest)

        elif c.direction == Elevator.DOWN:
            self.add(self.down_calls, c.src)
            self.add(self.down_calls, c.dest)

        if self.direction == Elevator.UP:
            self.active_calls.sort()
        else:
            self.active_calls.sort(reverse=True)

        print(f'a call got added {c.src} ---> {c.dest}')

        self.up_calls.sort()
        self.down_calls.sort(reverse=True)





    def feed_calls(self):
        if self.direction == Elevator.UP and not self.active_calls:
            if self.down_calls and self.down_calls[0] > self.elevator_pos:
                self.active_calls.append(self.down_calls[0])
                self.active_calls.sort(reverse=True)
            elif self.down_calls and self.down_calls[0] <= self.elevator_pos:
                self.active_calls = self.down_calls
                self.down_calls = []
                self.direction = Elevator.DOWN

        elif not self.active_calls:
            if self.up_calls and self.up_calls[0] < self.elevator_pos:
                self.active_calls.append(self.up_calls[0])
                self.active_calls.sort()
            elif self.up_calls and self.up_calls[0] >= self.elevator_pos:
                self.active_calls = self.up_calls
                self.up_calls = []
                self.direction = Elevator.UP





    def get_next(self):
        while  self.active_calls and self.active_calls[0] == self.elevator_pos:
            self.active_calls.pop(0)

        if not self.active_calls:
            self.feed_calls()

        if not self.active_calls:
            self.direction = Elevator.LEVEL
            return None


        if self.elevator_pos >= self.active_calls[0]:
            self.direction = Elevator.DOWN
        else:
            self.direction = Elevator.UP

        print(f'next is {self.active_calls[0]} direction {self.direction}')
        return self.active_calls[0]





    def cmd(self):
        next = self.get_next()
        print(f'current floor is {self.elevator_pos}   direction {self.direction}')

        if next is None:
            return

        if self.elevator_pos == next:
            self.active_calls.pop(0)



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









    def get_elevator_state_at(self, time, calls: []):
        i = 0
        print(f'simulation starting start pos {self.elevator_pos}  start direction {self.direction}')

        while i < time:
            for c in calls:
                if c.time_coming <= i:
                    self.add_call_to_active(c)
                    calls.remove(c)
            print('-----')
            print(self.active_calls)
            print(self.up_calls)
            print(self.down_calls)
            print('-----')

            self.cmd()
            i += 1
