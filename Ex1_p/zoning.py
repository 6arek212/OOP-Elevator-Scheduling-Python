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
        floorPerZone = numofFloors / self.numofZones
        spillPerFloor = (numofFloors / self.numofZones) - floorPerZone
        totalSpill = 0
        handlefFloors = 0

        for zone in range(self.numofZones):
            zoneEle = []
            zoneFloors = []

            elePerZone = building.numberOfElevetors() / self.numofZones

            totalSpill += spillPerFloor
            minFloor = handlefFloors
            maxFloor = handlefFloors + floorPerZone - 1

            if totalSpill >= 1.0 - 0.00001:
                totalSpill = max(0, totalSpill - 1.0)
                maxFloor += 1

            for i in range(building.numberOfElevetors()):
                ele = building.getElevator(i)
                if ele['id'] >= zone * elePerZone and ele['id'] < (zone + 1) * elePerZone:
                    zoneEle.append(ele)

            f = minFloor
            m = maxFloor
            while f <= m:
                zoneFloors.append(self.floors[f])
                f += 1

            handlefFloors += maxFloor - minFloor + 1
            self.zones.append(Zone(zoneFloors, zoneEle))

            a = 0

            for a in range(len(zoneFloors)):
                self.floorToZone[i] = self.zones[len(self.zones) - 1]
                i += 1

            for ele in zoneEle:
                self.elevtoZone[ele['id']] = self.zones[len(self.zones) - 1]


if __name__ == '__main__':
    building = Building.building_F("b1.txt")
    zoning = Zoning(building.numberOfElevetors() , building)
    print(zoning)

