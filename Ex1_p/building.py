from elevator import Elevator
import json
import math
import sys
class Building:
    global _totalElev

    def __init__(self, elevators, max_Floor, min_Floor):
        self.elevators = elevators
        self.max_Floor = max_Floor
        self.min_Floor = min_Floor

    def __str__(self):
        return f"elevators : {self.elevators} , max_floor : {self.max_Floor} , min_floor : {self.min_Floor}"

    def __repr__(self):
        return f"elevators : {self.elevators} , max_floor : {self.max_Floor} , min_floor : {self.min_Floor}"

    def getElevator(self, i) -> Elevator:
        return self.elevators[i]

    def numberOfElevetors(self):
        return len(self.elevators)

    @staticmethod
    def building_F(filepath):
        with open(filepath, 'r') as f:
            buildings = json.load(f)
            max_floor = buildings['_maxFloor']
            min_floor = buildings['_minFloor']
            elevators = []

            print(type(buildings))
            for e in buildings['_elevators']:
                # def __init__(self, id, speed, max_floor, min_floor, close_time, open_time, start_time, stop_time,
                #              **kwargs):
                ele = Elevator(e['_id'], e['_speed'], e['_maxFloor'], e['_minFloor'], e['_closeTime'], e['_openTime'],
                               e['_stopTime'], e['_stopTime'])

                elevators.append(ele)

            building = Building(elevators, max_floor, min_floor)
            return building


class Floor:

    def __init__(self, floor_Num):
        self.floor_Num = floor_Num

    def __str__(self):
        return f"Num_Floor: {self.floor_Num}"

    def __repr__(self):
        return f"Num_Floor: {self.floor_Num}"


class Floors:

    def __init__(self, building: Building):
        self.building = building
        self.floors = []

        j = self.building.min_Floor
        while (j <= self.building.max_Floor):
            self.floors.append(Floor(j))
            j += 1

    def __str__(self):
        return f"Floors: {self.floors}"

    def __repr__(self):
        return f"Floors: {self.floors}"


if __name__ == '__main__':
    building = Building.building_F("b2.txt")
    # ele = building.elevators[0]
    # building.
    # print(ele["min_floor"])
    # print(building)
    # print(ele)

    print(math.ceil(4.3))
    print(building.getElevator(0))
    print(sys.maxsize)
    for i in range(10):
        print(i)
    # print(building.elevators[1])
    # floors = Floors(building)
    #
    #
    # print(floors.floors[0])
