# from building import Building
from call import Call


class Elevator:
    UP, DOWN, IDLE = 1, -1, 0

    def __init__(self, id, speed, max_floor, min_floor, close_time, open_time, start_time, stop_time, **kwargs):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.direction = Elevator.UP
        self.currFloor = 0
        self.Calls = []

    def __str__(self):
        return f"id : {self.id} , speed : {self.speed} , max_floor : {self.max_floor} ," \
               f" min_floor:{self.min_floor}"

    def __repr__(self):
        return f"id : {self.id} , speed : {self.speed} , min_floor : {self.min_floor} ," \
               f" max_floor:{self.max_floor}"


if __name__ == '__main__':
    elev = Elevator("22", 3, 4, 2, 3, 4, 12, 2)
    print(elev)
