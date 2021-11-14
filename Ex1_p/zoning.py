import math

from building import Building
from building import Floors
from building import Floor


class Zone:

    def __init__(self, floors: Floors, elevators):
        self.floors = floors
        self.elevators = elevators

    def floorInZone(self, f) -> bool:

        for i in range(self.floors):
            if self.floors[i].floor_Num == f:
                return True

            return False

    def __str__(self):
        return f"Zone floors: {self.floors} , Zone elevators: {self.elevators} \n"

    def __repr__(self):
        return f"Zone floors: {self.floors} , Zone elevators: {self.elevators} \n"

    def bottomFloor(self):
        return self.floors[0].floor_Num

    def middleFloor(self):
        return self.floors[len(self.floors) / 2].floor_Num

    def middleFloor(self):
        return self.floors[len(self.floors) - 1].floor_Num


class Zoning:

    def __init__(self, numofZones, building: Building):

        self.numofZones = numofZones
        self.building = building
        numofFloors = abs(building.max_Floor - building.min_Floor) + 1
        self.zones = []
        self.floorToZone = []
        self.elevtoZone = []
        self.floors = Floors(building)
        floorPerZone =  int(numofFloors / self.numofZones)
        spillPerFloor = ((numofFloors / float(self.numofZones)) - floorPerZone)

        totalSpill = 0
        handlefFloors:int = 0

        for zone in range(self.numofZones):
            zoneEle = []
            zoneFloors = []

            elePerZone = int(building.numberOfElevetors() / self.numofZones)

            totalSpill += spillPerFloor
            minFloor = int(handlefFloors)
            maxFloor = int(handlefFloors + floorPerZone - 1)

            if totalSpill >= 1.0 - 0.00001:
                totalSpill = max(0, totalSpill - 1.0)
                maxFloor += 1

            for i in range(building.numberOfElevetors()):
                ele = building.getElevator(i)
                if ele.id >= zone * elePerZone and ele.id < (zone + 1) * elePerZone:
                    zoneEle.append(ele)

            min = minFloor
            while min <= maxFloor:
                zoneFloors.append(self.floors.floors[min])
                min += 1


            handlefFloors += maxFloor - minFloor + 1
            self.zones.append(Zone(zoneFloors, zoneEle))

            a = 0
            while a < len(zoneFloors):
                zone = self.zones[len(self.zones) - 1]
                self.floorToZone.insert(a, zone)
                a += 1


            for ele in zoneEle:
                zone = self.zones[len(self.zones) - 1]
                self.elevtoZone.insert(ele.id, zone)


if __name__ == '__main__':
    building = Building.building_F("b3.txt")

    zoning = Zoning(building.numberOfElevetors(), building)
    for zone in zoning.zones:
        print(zone)
