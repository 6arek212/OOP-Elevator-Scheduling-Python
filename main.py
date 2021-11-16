import sys
from models.simulator import simulator

from models.elevator_manager import ElevatorManager
from models.call import Call
from models.building import Building
import csv

if __name__ == '__main__':
    buildings = Building.init_from_file('./data/Ex1_input/Ex1_Buildings/B5.json')
    calls = Call.init_from_file('./data/Ex1_input/Ex1_Calls/Calls_d.csv')
    elevator_manager = []
    for el in buildings.elevators:
        elevator_manager.append(ElevatorManager(el))

    x = 0


    # def allocate_call(call):
    #     if call.dest > buildings.max_floor or call.dest < buildings.min_floor:
    #         return sys.maxsize
    #     picked = 0
    #     for el in range(1, len(buildings.elevators)):
    #         time_with_call = elevator_manager[el].estimated_time_to(call)
    #         if time_with_call < elevator_manager[picked].estimated_time_to(call):
    #             picked = el
    #     elevator_manager[picked].add_call(call)
    #     print('----------------------------------------')
    #     return picked

    def allocate_call(call):
        global x
        v = x % len(buildings.elevators)
        x += 1
        return v


    calls.sort()
    for call in calls:
        call.allocated_to = allocate_call(call)





    s = simulator(buildings.elevators[0], -1)
    calls_cc =[]

    for c in calls :
        if c.time_coming <=30:
            calls_cc.append(c)

    print(calls_cc)
    s.get_elevator_state_at(50,calls_cc)



    # for manager in elevator_manager:
    #     print(manager.elevator.id)
    #     print(manager.calls)
    #     print('----------')

    # with open('./out.csv', 'w', newline='') as f:
    #     csv_writer = csv.writer(f)
    #     for call in calls:
    #         if call.allocated_to != sys.maxsize:
    #             csv_writer.writerow(call.__dict__())
