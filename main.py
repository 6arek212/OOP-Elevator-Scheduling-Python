import sys
from pprint import pprint

from models.call import Call
from models.building import Building
import csv

if __name__ == '__main__':
    buildings = Building.init_from_file('./data/Ex1_input/Ex1_Buildings/B5.json')
    calls = Call.init_from_file('./data/Ex1_input/Ex1_Calls/Calls_d.csv')


    def allocate_call(call):
        if call.dest > buildings.max_floor or call.dest < buildings.min_floor:
            return sys.maxsize
        picked = 0
        for el in range(1, len(buildings.elevators)):
            time_with_call = buildings.elevators[el].estimated_time(call)
            if time_with_call < buildings.elevators[picked].estimated_time(call):
                picked = el
        buildings.elevators[picked].add_call(call)
        print('----------------------------------------')
        return picked


    calls.sort()
    for call in calls:
        call.allocated_to = allocate_call(call)

    total_waiting = 0
    for el in buildings.elevators:
        print('------------')
        print(f'time {el.time_to_finish_calls()} , start direction {"UP" if el.start_direction == 1 else "DOWN"}  , elevator {el.id}')
        print(el.up_calls)
        print(el.down_calls)
        total_waiting += el.time_to_finish_calls()
        print('------------')

    print('calls number ', len(calls), total_waiting)
    with open('./out.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for call in calls:
            if call.allocated_to != sys.maxsize:
                csv_writer.writerow(call.__dict__())
