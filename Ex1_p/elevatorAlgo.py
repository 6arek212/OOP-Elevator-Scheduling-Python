import building as Building
from elevator import Elevator
from call import Call
import csv
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




