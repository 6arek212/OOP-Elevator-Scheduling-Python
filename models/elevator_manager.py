import sys

from .elevator import Elevator
from models.simulator import simulator
from models.call import Call


class ElevatorManager:
    def __init__(self, elevator: Elevator):
        self.elevator = elevator
        self.calls = []
        self.active_calls = []
        self.up_calls = []
        self.down_calls = []
        self.start_direction = None
        self.direction = Elevator.LEVEL
        self.elv_pos = 0
        self.going_to = None
        self.to_dst = None

    def add_call(self, call):
        self.calls.append(call)
        if self.start_direction is None:
            self.start_direction = call.direction



    def add(self, list, v):
        if not list.__contains__(v):
            list.append(v)

    def add_call_2(self, c: Call):
        if not self.active_calls and not self.up_calls and not self.down_calls:
            self.add(self.active_calls, c.src)
            self.add(self.active_calls, c.dest)
            print(f'a call got added {c.src} ---> {c.dest}')
            return

        if c.direction == Elevator.UP and self.direction == Elevator.UP and self.elv_pos <= c.src:
            self.add(self.active_calls, c.src)
            self.add(self.active_calls, c.dest)

        elif c.direction == Elevator.DOWN and self.direction == Elevator.DOWN and self.elv_pos >= c.src:
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

            if self.down_calls and self.down_calls[0] > self.elv_pos:
                self.add(self.active_calls, self.down_calls[0])

            elif self.down_calls and self.down_calls[0] <= self.elv_pos:
                self.active_calls = self.down_calls
                self.down_calls = []
                self.direction = Elevator.DOWN

            elif not self.down_calls:
                if self.up_calls and self.up_calls[0] < self.elv_pos:
                    self.add(self.active_calls, self.up_calls[0])
                elif self.up_calls and self.up_calls[0] >= self.elv_pos:
                    self.active_calls = self.up_calls
                    self.up_calls = []
                    self.direction = Elevator.UP



        elif not self.active_calls:
            if self.up_calls and self.up_calls[0] < self.elv_pos:
                self.add(self.active_calls, self.up_calls[0])
            elif self.up_calls and self.up_calls[0] >= self.elv_pos:
                self.active_calls = self.up_calls
                self.up_calls = []
                self.direction = Elevator.UP

            elif not self.up_calls:
                if self.down_calls and self.down_calls[0] > self.elv_pos:
                    self.add(self.active_calls, self.down_calls[0])

                elif self.down_calls and self.down_calls[0] <= self.elv_pos:
                    self.active_calls = self.down_calls
                    self.down_calls = []
                    self.direction = Elevator.DOWN

    def get_next(self):
        while  self.active_calls and self.active_calls[0] == self.elv_pos:
            self.active_calls.pop(0)

        if not self.active_calls:
            if self.to_dst is not None:
                self.add(self.active_calls, self.to_dst)
                self.to_dst =  None
            else:
                self.feed_calls()

        while  self.active_calls and self.active_calls[0] == self.elv_pos:
            self.active_calls.pop(0)

        if not self.active_calls:
            self.direction = Elevator.LEVEL
            return None

        if self.elv_pos >= self.active_calls[0]:
            self.direction = Elevator.DOWN
        else:
            self.direction = Elevator.UP

        print(f'next is {self.active_calls[0]} direction {self.direction}')
        return self.active_calls.pop(0)



    def calculate_time(self, c):
        is_moving = False
        if self.going_to is not None:
            is_moving = True
        #     self.add(self.active_calls,self.going_to)
        #     if self.direction == Elevator.UP:
        #         self.active_calls.sort()
        #     else:
        #         self.active_calls.sort(reverse=True)


        print('-----')
        print(self.active_calls)
        print(self.up_calls)
        print(self.down_calls)
        print('-----')

        time = 0
        next = self.get_next()

        while next is not None:

            if time == 0 and not is_moving:
                time += self.elevator.close_time + self.elevator.stop_time
            time += abs(self.elv_pos - next) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            self.elv_pos = next
            next = self.get_next()
            is_moving = False

        return time




    def estimated_time_to(self, c):
        if self.start_direction is None:
            time = 0
            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(self.elv_pos - c.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time

            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(c.src - c.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            return time


        self.start_simulate(c.time_coming)

        if self.going_to is None:
            time = 0
            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(self.elv_pos - c.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time

            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(c.src - c.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            return time

        self.add_call_2(c)

        return self.calculate_time(c)

    def start_simulate(self, time):
        s = simulator(self.elevator)
        (active_calls, down_calls, up_calls, elv_pos, going_to, direction) = s.get_elevator_state_at(time, self.calls)
        self.active_calls = active_calls
        self.down_calls = down_calls
        self.up_calls = up_calls
        self.elv_pos = elv_pos
        self.going_to = going_to
        self.direction = direction
        print('simulation result -> ',active_calls,down_calls,up_calls,elv_pos,going_to,direction)