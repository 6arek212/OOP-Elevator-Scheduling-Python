import json
import csv


def get_building():
    files = []

    with open('./data/Ex1_input/Ex1_Buildings/B1.json', 'r') as f:
        files.append(json.load(f))

    with open('./data/Ex1_input/Ex1_Buildings/B2.json', 'r') as f:
        files.append(json.load(f))

    with open('./data/Ex1_input/Ex1_Buildings/B3.json', 'r') as f:
        files.append(json.load(f))

    with open('./data/Ex1_input/Ex1_Buildings/B4.json', 'r') as f:
        files.append(json.load(f))

    with open('./data/Ex1_input/Ex1_Buildings/B5.json', 'r') as f:
        files.append(json.load(f))

    return files


def get_calls():
    with open('./data/Ex1_input/Ex1_Calls/Calls_a.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def allocate_calls():
    pass


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


class ElevatorDS:
    def __init__(self):
        pass

    def get_next(self):
        pass

    def add(self):
        pass


def move_elevators(elev: Elevator, ds: ElevatorDS):
    if elev.state == Elevator.LEVEL:
        elev.go_to(ds.get_next())





print(get_building()[0])
