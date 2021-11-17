import sys
from models.simulator import simulator

from models.elevator_manager import ElevatorManager
from models.call import Call
from models.building import Building
import csv

if __name__ == '__main__':
    buildings = Building.init_from_file('./data/Ex1_input/Ex1_Buildings/B5.json')
    calls = Call.init_from_file('./data/Ex1_input/Ex1_Calls/Calls_c.csv')
    elevator_manager = []
    calls.sort()
    time_for_sim = calls[len(calls) - 1].time_coming + 120

    for el in buildings.elevators:
        elevator_manager.append(ElevatorManager(el,time_for_sim))



    def allocate_call(call):
        if call.dest > buildings.max_floor or call.dest < buildings.min_floor:
            raise Exception('out of floor range')
        picked = 0
        picked_sim = elevator_manager[picked].estimated_time_to(call)
        for el in range(1, len(buildings.elevators)):
            print(el)
            time_with_call = elevator_manager[el].estimated_time_to(call)
            print(time_with_call, picked_sim)
            if time_with_call < picked_sim:
                picked = el
                picked_sim = time_with_call
        elevator_manager[picked].add(call)
        print(f'{call.src} ---> {call.dest}  call got added to ', picked)
        print('----------------------------------------')
        return picked

    # x = 0
    # def allocate_call(call):
    #     global x
    #     v = x % len(buildings.elevators)
    #     x += 1
    #     return v




    for call in calls:
        x = allocate_call(call)
        if x is not None:
            call.allocated_to = x
    #
    # s = simulator(buildings.elevators[0])
    # calls_cc =[]

    # for c in calls :
    #     if c.time_coming <=100:
    #         calls_cc.append(c)
    #
    # print(calls_cc)
    # print(s.get_elevator_state_at(30,calls_cc))

    for manager in elevator_manager:
        print(manager.elevator.id)
        print(manager.calls)
        print('----------')


    with open('./out.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for call in calls:
            if call.allocated_to != sys.maxsize:
                csv_writer.writerow(call.__dict__())
