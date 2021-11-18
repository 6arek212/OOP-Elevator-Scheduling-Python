import json
import unittest

from models.elevator import Elevator


class Building:
    def __init__(self, elevators: Elevator, max_floor, min_floor):
        self.elevators = elevators
        self.max_floor = max_floor
        self.min_floor = min_floor

    def __str__(self):
        return f"elevators : {self.elevators} ,\n max_floor : {self.max_floor} ,\n min_floor : {self.min_floor}"

    @staticmethod
    def init_from_file(filepath):
        building = {}
        with open(filepath, 'r') as f:
            j_buildings = json.load(f)
            building['max_floor'] = j_buildings['_maxFloor']
            building['min_floor'] = j_buildings['_minFloor']
            building['elevators'] = []

            for o in j_buildings['_elevators']:
                el = {
                    'min_floor': o['_minFloor'],
                    'id': o['_id'],
                    'speed': o['_speed'],
                    'close_time': o['_closeTime'],
                    'open_time': o['_openTime'],
                    'start_time': o['_startTime'],
                    'stop_time': o['_stopTime'],
                    'max_floor': o['_maxFloor'],
                }
                building['elevators'].append(Elevator(**el))
        return Building(**building)






