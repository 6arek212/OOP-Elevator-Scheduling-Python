from  building import Building
import sys
from elevator import Elevator
from call import Call
import csv
from zoning import Zoning
from zoning import Zone
if __name__ == '__main__':

    building = Building.building_F("b1.txt")
    calls = Call.call_F("c1.text")
    print(building.elevators)
    n = 0


    def threePassage_alloc(call):

        pick = 0
        cost = sys.maxsize

        for i in range(building.numberOfElevetors()):
            ele = building.getElevator(i)
            calls = len(ele.up_calls)+ len(ele.down_calls)
            floorDiff = abs(call.src - ele.currFloor)


            ele_cost = (calls+1)*(ele.speed*ele.)






    def roundRobin_alloc():
        global n
        ans = n % building.numberOfElevetors()
        n = (n + 1) % building.numberOfElevetors()

        return ans


    def getBuilding(self):
        pass


    def zoning_alloc(call):
        zoning = Zoning(building.numberOfElevetors() , building)

        for zone in zoning.zones:
            for i in range(len(zone.floors.floors)):
                if zone.floors.floors[i].floor_Num == call.src:
                    return  zone.elevators[0].id




    def allocateAnElevator(call):
        if call.dest > building.max_Floor or call.dest < building.min_Floor:
            raise Exception('out of boundries')
        ans= zoning_alloc(call)
        # for el in range(1, len(building.elevators)):
        #     time_with_call = building.elevators[el].estimated_time(call)
        #     if time_with_call < buildings.elevators[picked].estimated_time(call):
        #         picked = el
        for el in bu
        building.elevators[ans].add_call(call)
        print('----------------------------------------')
        return ans


    # for call in calls:
    #     print(call.time_coming)
    #     call.allocated_to = allocate_call(call)
    #
    # for el in building.elevators:
    #     print('------------')
    #     print(f'time {el.time_to_finish_calls()}')
    #     print(el.up_calls)
    #     print(el.down_calls)
    #     print('------------')

    with open('./out.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for call in calls:
            csv_writer.writerow(call.__dict__())



