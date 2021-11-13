class Elevator:
    UP = 1
    DOWN = -1

    def __init__(self, id, speed, max_floor, min_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.up_calls = []
        self.down_calls = []
        self.start_direction = None

    def __str__(self):
        return f"id : {self.id} ,\n speed : {self.speed} ,\n min_floor : {self.min_floor} ," \
               f"\n max_floor:{self.max_floor}"

    def __repr__(self):
        return f"id : {self.id} ,\n speed : {self.speed} ,\n min_floor : {self.min_floor} ," \
               f"\n max_floor:{self.max_floor}"

    def add_call(self, call):
        if self.start_direction is None:
            self.start_direction = call.direction
        if call.direction == Elevator.UP:
            if not self.up_calls.__contains__(call.src):
                self.up_calls.append(call.src)
            if not self.up_calls.__contains__(call.dest):
                self.up_calls.append(call.dest)
            self.up_calls.sort()
        else:
            if not self.down_calls.__contains__(call.src):
                self.down_calls.append(call.src)
            if not self.down_calls.__contains__(call.dest):
                self.down_calls.append(call.dest)
            self.down_calls.sort()
        print(f'{call.src} ---> {call.dest}  call got added to ', self.id)

    def time_up_calls(self, list, start_pos: int):
        time = 0.0
        current_pos = start_pos
        for floor in list:
            time += self.close_time + self.start_time
            time += abs(floor - current_pos) / self.speed
            time += self.stop_time + self.open_time
            current_pos = floor
        return (time, current_pos)

    def time_down_calls(self, list, start_pos: int):
        time = 0.0
        current_pos = start_pos
        for i in range(len(list) - 1, -1, -1):
            time += self.close_time + self.start_time
            time += abs(list[i] - current_pos) / self.speed
            time += self.stop_time + self.open_time
            current_pos = list[i]
        return (time, current_pos)

    def time_to_finish_calls(self):
        time = 0.0
        if self.start_direction == Elevator.UP:
            t = self.time_up_calls(self.up_calls, 0)
            time += t[0]
            time += self.time_down_calls(self.down_calls, t[1])[0]
        else:
            t = self.time_down_calls(self.down_calls, 0)
            time += t[0]
            time += self.time_up_calls(self.up_calls, t[1])[0]
        return time

    def estimated_time(self, call):
        """calculate the time for this elevator to get to the given call"""

        time = 0.0

        if call.direction == Elevator.UP:
            new_calls = self.up_calls.copy()
        else:
            new_calls = self.down_calls.copy()

        if not new_calls.__contains__(call.src):
            new_calls.append(call.src)
        if not new_calls.__contains__(call.dest):
            new_calls.append(call.dest)
        new_calls.sort()

        if self.start_direction is None:
            if call.src != 0:
                time += self.close_time + self.start_time
                time += abs(call.src) / self.speed
                time += self.stop_time + self.open_time
            time += self.close_time + self.start_time
            time += abs(call.dest - call.src) / self.speed
            time += self.stop_time + self.open_time


        elif call.direction == Elevator.UP and self.start_direction == Elevator.DOWN:
            t = self.time_down_calls(self.down_calls, 0)
            time += t[0]
            time += self.time_up_calls(new_calls, t[1])[0]

        elif call.direction == Elevator.UP and self.start_direction == Elevator.UP:
            t = self.time_up_calls(new_calls, 0)
            time += t[0]
            time += self.time_down_calls(self.down_calls, t[1])[0]

        elif call.direction == Elevator.DOWN and self.start_direction == Elevator.UP:
            t = self.time_up_calls(self.up_calls, 0)
            time += t[0]
            time += self.time_down_calls(new_calls, t[1])[0]

        elif call.direction == Elevator.DOWN and self.start_direction == Elevator.DOWN:
            t = self.time_down_calls(new_calls, 0)
            time += t[0]
            time += self.time_up_calls(self.up_calls, t[1])[0]

        print(time, '-----------', self.time_to_finish_calls())

        return time
