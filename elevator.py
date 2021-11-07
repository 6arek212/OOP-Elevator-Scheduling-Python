class Elevator:
    UP = 1
    DOWN = -1
    LEVEL = 0

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.allocated_to = None
        self.state = Elevator.UP

    def go_to(self, target):
        pass

    def allocated_to(self, elev):
        self.allocated_to = elev
