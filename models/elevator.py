class Elevator:
    UP = 1
    DOWN = -1
    LEVEL = 0

    def __init__(self, id, speed, max_floor, min_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.start_direction = None
        self.position = 0
        self.state = Elevator.LEVEL

    def __str__(self):
        return f"id : {self.id} ,\n speed : {self.speed} ,\n min_floor : {self.min_floor} ," \
               f"\n max_floor:{self.max_floor}"

    def __repr__(self):
        return f"id : {self.id} ,\n speed : {self.speed} ,\n min_floor : {self.min_floor} ," \
               f"\n max_floor:{self.max_floor}"

    def go_to(self, dest):
        pass