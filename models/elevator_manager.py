import sys

from .elevator import Elevator


class ElevatorManager:
    def __init__(self, elevator: Elevator):
        self.elevator = elevator
        self.start_direction = None
        self.calls = []

    def add_call(self, call):
        if self.start_direction is None:
            self.start_direction = call.direction
        self.calls.append(call)
        print(f'{call.src} ---> {call.dest}  call got added to ', self.elevator.id)

    def has_up_calls(self, calls, time):
        for c in calls:
            if c.direction == Elevator.UP and c.time_coming <= time:
                return True
        return False

    def has_down_calls(self, calls, time):
        for c in calls:
            if c.direction == Elevator.DOWN and c.time_coming <= time:
                return True
        return False

    def get_next_call(self, calls, elevator_pos, direction, time):
        if len(calls) == 0:
            return sys.maxsize

        if direction == Elevator.UP:
            for c in calls:
                if elevator_pos > c.dest and time > c.time_coming:
                    calls.remove(c)


            min = []
            for c in calls:
                if c.direction == Elevator.UP and time > c.time_coming:
                    min.append(c.src)
                    min.append(c.dest)
            min.sort()

            if len(min) == 0:
                return sys.maxsize

            while min[0] < elevator_pos:
                min.remove(0)


            return min[0]

        else:
            for c in calls:
                if elevator_pos < c.dest and time > c.time_coming:
                    calls.remove(c)

            min = []
            for c in calls:
                if c.direction == Elevator.DOWN and time > c.time_coming:
                    min.append(c.src)
                    min.append(c.dest)
            min.sort()
            if len(min) == 0:
                return sys.maxsize

            while min[0] < elevator_pos:
                min.remove(0)

            return min[0]

    def elevator_status_at(self, time):
        ':returns (currnet_up_calls , currnet_down_calls , elevator_po'
        current_calls = []

        for call in self.calls:
            if call.time_coming < time:
                current_calls.append(call)

        current_pos = 0
        t = 0

        go_to = self.get_next_call(current_calls, 0, self.start_direction, t)
        while t < time and self.has_up_calls(current_calls, t) or self.has_down_calls(
                current_calls, t):
            t += self.elevator.close_time + self.elevator.stop_time
            t += abs(current_pos - go_to) / self.elevator.speed
            t += self.elevator.close_time + self.elevator.start_time
            current_pos = go_to

            if self.has_up_calls(current_calls, t):
                go_to = self.get_next_call(current_calls, current_pos, Elevator.UP, t)

            elif self.has_down_calls(current_calls, t):
                go_to = self.get_next_call(current_calls, current_pos, Elevator.DOWN, t)
            else:
                t += 1

        return (current_calls,current_pos, go_to)

    def time_up_calls(self, current_pos, up_calls):
        time = 0
        for c in up_calls:
            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(current_pos - c) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            current_pos = c
        return time

    def time_down_calls(self, current_pos, up_calls):
        time = 0
        for c in up_calls:
            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(current_pos - c) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            current_pos = c
        return time

    def calculate_time(self, calls, going_to, direction, elevator_pos):
        call_up = []
        call_down = []

        for c in calls:
            if c.direction == Elevator.UP:
                call_up.append(c.src)
                call_up.append(c.dest)
            else:
                call_down.append(c.src)
                call_down.append(c.dest)

        if direction == Elevator.UP:
            call_up.append(going_to)
            call_up.sort()
            return self.time_up_calls(elevator_pos, call_up) + self.time_down_calls(elevator_pos, call_down)
        else:
            call_down.append(going_to)
            call_down.sort(reverse=True)
            return self.time_down_calls(elevator_pos, call_down) + self.time_up_calls(elevator_pos, call_up)

    def estimated_time_to(self, call):
        (calls, elv_pos, going_to) = self.elevator_status_at(call.time_coming)

        print('current elevator calls',calls)

        if going_to is None:
            time = 0
            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(elv_pos - call.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time

            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(call.src - call.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            return time

        direction = Elevator.UP if elv_pos <= going_to else Elevator.DOWN
        time = self.calculate_time(calls, going_to, direction, elv_pos)
        print(time)
        return time
