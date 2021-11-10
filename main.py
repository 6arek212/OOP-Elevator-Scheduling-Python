import sys
from pprint import pprint

from models.call import Call
from models.building import Building
import csv

if __name__ == '__main__':
    buildings = Building.init_from_file('./data/Ex1_input/Ex1_Buildings/B5.json')
    calls = Call.init_from_file('./data/Ex1_input/Ex1_Calls/Calls_d.csv')
    x = 0


    def round_robin_allocate():
        global x
        y = x % len(buildings.elevators)
        x = (x + 1) % len(buildings.elevators)
        return y


    def allocate_call(call):
        if call.dest > buildings.max_floor or call.dest < buildings.min_floor:
            raise Exception('out of boundries')
        picked = 0
        for el in range(1, len(buildings.elevators)):
            time_with_call = buildings.elevators[el].estimated_time(call)
            if time_with_call < buildings.elevators[picked].estimated_time(call):
                picked = el
        buildings.elevators[picked].add_call(call)
        print('----------------------------------------')
        return picked


    for call in calls:
        print(call.time_coming)
        call.allocated_to = allocate_call(call)

    for el in buildings.elevators:
        print('------------')
        print(f'time {el.time_to_finish_calls()}')
        print(el.up_calls)
        print(el.down_calls)
        print('------------')

    with open('./out.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for call in calls:
            csv_writer.writerow(call.__dict__())
