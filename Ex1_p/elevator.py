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

    def alloc_cost(self, call: Call):

        req_Floor = call.dest
        dir = call.direction
        if self.direction == 1:
            if self.currFloor > req_Floor or dir == -1:
                return self.max_floor - self.currFloor + self.max_floor - req_Floor
            else:
                return req_Floor - self.currFloor

        elif self.direction == -1:
            if self.currFloor < req_Floor or dir == 1:
                return self.currFloor - 1 + req_Floor - 1
            else:
                return self.currFloor - 1 + req_Floor

        else:

            return abs(self.currFloor - req_Floor)

    def get_distance(self, call: Call):
        req_Floor = call.dest

        if self.direction == 1:
            if self.self.currFloor > req_Floor:
                return self.max_floor - self.currFloor + self.max_floor - req_Floor
            else:
                return req_Floor - self.currFloor
        elif self.direction == -1:
            if self.currFloor > req_Floor:
                return self.currFloor - req_Floor
            else:
                return self.currFloor - 1 + req_Floor - 1
        else:
            return abs(self.currFloor - req_Floor)


if __name__ == '__main__':
    elev = Elevator("22", 3, 4, 2, 3, 4, 12, 2)
    print(elev)
