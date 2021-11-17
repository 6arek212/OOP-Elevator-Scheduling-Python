import sys

from .elevator import Elevator
from .call import Call


class simulator:
    def __init__(self, elevator):
        self.elevator = elevator
        self.elevator_pos = 0
        self.elevator_mode = Elevator.LEVEL
        self.direction = Elevator.LEVEL
        # self.active_calls = []
        # self.up_calls = []
        # self.down_calls = []
        self.calls = []

        self.to_dst = None


    def add(self , call:Call):
        self.calls.append(call)



    # def add(self, list, v):
    #     if not list.__contains__(v):
    #         list.append(v)
    #
    # def add_call_to_active(self, c: Call):
    #     # print(f'a call got added {c.src} ---> {c.dest}  direction {c.direction}')
    #     if not self.active_calls and not self.up_calls and not self.down_calls:
    #         if c.src == self.elevator_pos:
    #             self.direction = c.direction
    #         if c.src > self.elevator_pos:
    #             self.direction = Elevator.UP
    #         else:
    #             self.direction = Elevator.DOWN
    #
    #         if self.direction != c.direction:
    #             self.add(self.active_calls, c.src)
    #             self.to_dst = c.dest
    #
    #         else:
    #             self.add(self.active_calls, c.src)
    #             self.add(self.active_calls, c.dest)
    #
    #
    #
    #         if self.direction == Elevator.UP:
    #             self.active_calls.sort()
    #         else:
    #             self.active_calls.sort(reverse=True)
    #
    #         self.up_calls.sort()
    #         self.down_calls.sort(reverse=True)
    #         return
    #
    #
    #     if c.direction == Elevator.UP and self.direction == Elevator.UP and self.elevator_pos <= c.src:
    #         self.add(self.active_calls, c.src)
    #         self.add(self.active_calls, c.dest)
    #
    #     elif c.direction == Elevator.DOWN and self.direction == Elevator.DOWN and self.elevator_pos >= c.src:
    #         self.add(self.active_calls, c.src)
    #         self.add(self.active_calls, c.dest)
    #
    #
    #     elif c.direction == Elevator.UP:
    #         self.add(self.up_calls, c.src)
    #         self.add(self.up_calls, c.dest)
    #
    #     elif c.direction == Elevator.DOWN:
    #         self.add(self.down_calls, c.src)
    #         self.add(self.down_calls, c.dest)
    #
    #     if self.direction == Elevator.UP:
    #         self.active_calls.sort()
    #     else:
    #         self.active_calls.sort(reverse=True)
    #
    #     self.up_calls.sort()
    #     self.down_calls.sort(reverse=True)

    # def feed_calls(self):
    #     if self.direction == Elevator.UP and not self.active_calls:
    #
    #         if self.down_calls and self.down_calls[0] > self.elevator_pos:
    #             self.add(self.active_calls, self.down_calls[0])
    #
    #         elif self.down_calls and self.down_calls[0] <= self.elevator_pos:
    #             self.active_calls = self.down_calls
    #             self.down_calls = []
    #             self.direction = Elevator.DOWN
    #
    #         elif not self.down_calls:
    #             if self.up_calls and self.up_calls[0] < self.elevator_pos:
    #                 self.add(self.active_calls, self.up_calls[0])
    #             elif self.up_calls and self.up_calls[0] >= self.elevator_pos:
    #                 self.active_calls = self.up_calls
    #                 self.up_calls = []
    #                 self.direction = Elevator.UP
    #
    #
    #
    #     elif not self.active_calls:
    #         if self.up_calls and self.up_calls[0] < self.elevator_pos:
    #             self.add(self.active_calls, self.up_calls[0])
    #         elif self.up_calls and self.up_calls[0] >= self.elevator_pos:
    #             self.active_calls = self.up_calls
    #             self.up_calls = []
    #             self.direction = Elevator.UP
    #
    #         elif not self.up_calls:
    #             if self.down_calls and self.down_calls[0] > self.elevator_pos:
    #                 self.add(self.active_calls, self.down_calls[0])
    #
    #             elif self.down_calls and self.down_calls[0] <= self.elevator_pos:
    #                 self.active_calls = self.down_calls
    #                 self.down_calls = []
    #                 self.direction = Elevator.DOWN
    #
    # def get_next(self):
    #     while self.active_calls and self.active_calls[0] == self.elevator_pos:
    #         self.active_calls.pop(0)
    #
    #     if not self.active_calls:
    #         if self.to_dst is not None :
    #             self.add(self.active_calls,self.to_dst)
    #             self.to_dst = None
    #         else:
    #             self.feed_calls()
    #
    #     while self.active_calls and self.active_calls[0] == self.elevator_pos:
    #         self.active_calls.pop(0)
    #
    #     if not self.active_calls:
    #         self.direction = Elevator.LEVEL
    #         return None
    #
    #     if self.elevator_pos >= self.active_calls[0]:
    #         self.direction = Elevator.DOWN
    #     else:
    #         self.direction = Elevator.UP
    #
    #     # print(f'next is {self.active_calls[0]} direction {self.direction}')
    #     return self.active_calls[0]








    def get_min_dest_up_calls(elv_pos = None):
        picked = None
        if elv_pos is not None:
            for c in cs:
                if c.direction == 1 and c.src == elv_pos:
                    c.picked = True

                if c.direction == 1 and c.src > elv_pos and picked is None:
                    picked = c

                elif c.src > elv_pos and c.src < picked.src:
                    picked = c
        else:
            for c in cs:
                if c.direction == 1 and c.src == elv_pos:
                    c.picked = True

                if c.direction == 1 and picked is None:
                    picked = c

                elif c.src < picked.src:
                    picked = c
        return picked

    def get_min_dest_down_calls(elv_pos = None):
        picked = None
        if elv_pos is not None:
            for c in cs:
                if c.direction == -1 and c.src == elv_pos:
                    c.picked = True
                if c.direction == -1 and c.src < elv_pos and picked is None:
                    picked = c

                elif c.direction == -1 and c.src < elv_pos and c.src > picked.src:
                    picked = c

        else:
            for c in cs:
                if c.direction == -1 and c.src == elv_pos:
                    c.picked = True

                if c.direction == -1 and picked is None:
                    picked = c

                elif c.direction == -1 and c.src > picked.src:
                    picked = c
        return picked



    def get_next(self,direction, elv_pos):
        for c in cs:
            if c.picked and elv_pos == c.dest:
                cs.remove(c)
        if direction == 1:
            dd = self.get_min_dest_up_calls(elv_pos)
            if dd is None:
                dd = self.get_min_dest_down_calls()
            if dd is None:
                dd = self.get_min_dest_up_calls()
        else:
            dd = get_min_dest_down_calls(elv_pos)
            if dd is None:
                dd = get_min_dest_up_calls()
            if dd is None:
                dd = get_min_dest_down_calls()

        return dd











    def cmd(self):
        next = self.get_next()
        # print(f'current floor is {self.elevator_pos}   direction {self.direction}')

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
        # print(f'simulation starting start pos {self.elevator_pos}  start direction {self.direction}')
        new_calls = calls.copy()

        while i < time:
            # print('-----')
            for c in new_calls:
                if c.time_coming <= i:
                    self.add(c)
                    new_calls.remove(c)

            # print(self.active_calls)
            # print('up calls ', self.up_calls)
            # print('down calls', self.down_calls)

            self.cmd()
            # print('-----')
            i += 1

        return (self.calls , self.elevator_pos, self.get_next(), self.direction)
