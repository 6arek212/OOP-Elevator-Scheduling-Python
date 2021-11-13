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
