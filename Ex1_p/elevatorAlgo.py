import building as Building
from elevator import Elevator
from call import Call

if __name__ == '__main__':
    building = Building.building_F("b1.txt")
    calls = Call.call_F("c1.text")
    n = 0


    def round_robin():
        global n
        ans = n % building.numberOfElevetors()
        n = (n + 1) % building.numberOfElevetors()

        return ans


    def getBuilding(self):
        pass


    def allocateAnElevator(self, call):
        pass


    def alloc_cost(self, call: Call):

        _reqFloor = call.getDest()
        _dir = call.getDir()
        if self.direction == 1:
            if self.currFloor > _reqFloor or _dir == -1:
                return self._maxFloor - self.currFloor + self._maxFloor - _reqFloor
            else:
                return _reqFloor - self.currFloor

        elif self.direction == -1:
            if self.currFloor < _reqFloor or _dir == 1:
                return self.currFloor - 1 + _reqFloor - 1
            else:
                return self.currFloor - 1 + _reqFloor

        else:

            return abs(self.currFloor - _reqFloor)


    def get_distance(self, call: Call):
        _reqFloor = call.getDest()

        if self.direction == 1:
            if self.self.currFloor > _reqFloor:
                return self._maxFloor - self.currFloor + self._maxFloor - _reqFloor
            else:
                return _reqFloor - self.currFloor
        elif self.direction == -1:
            if self.currFloor > _reqFloor:
                return self.currFloor - _reqFloor
            else:
                return self.currFloor - 1 + _reqFloor - 1
        else:
            return abs(self.currFloor - _reqFloor)
