import sys

from elevator_manager import ElevatorManager
from models.call import Call
from models.building import Building
import csv

if __name__ == '__main__':
    print()

    has_input = True

    if len(sys.argv) == 4:
        building_file_name = sys.argv[1]
        calls_file_name = sys.argv[2]
        out_file_name = sys.argv[3]
    else:
        print('you need to provide the file names of <Building.json> <Calls.csv> <output.csv>')
        has_input = False


    if has_input:
        buildings = Building.init_from_file(f'./data/Ex1_input/Ex1_Buildings/{building_file_name}')
        calls = Call.init_from_file(f'./data/Ex1_input/Ex1_Calls/{calls_file_name}')
        elevator_manager = []
        calls.sort()
        time_for_sim = calls[len(calls) - 1].time_coming + 120

        for el in buildings.elevators:
            elevator_manager.append(ElevatorManager(el, time_for_sim))

        print('simulating...')


        def allocate_call(call):
            if call.dest > buildings.max_floor or call.dest < buildings.min_floor:
                raise Exception('out of floor range')
            picked = 0
            picked_sim = elevator_manager[picked].estimated_time_with(call)
            for el in range(1, len(buildings.elevators)):
                time_with_call = elevator_manager[el].estimated_time_with(call)
                if time_with_call < picked_sim:
                    picked = el
                    picked_sim = time_with_call
            elevator_manager[picked].add(call)
            return picked


        for call in calls:
            x = allocate_call(call)
            if x is not None:
                call.allocated_to = x

        print('Done')

        with open(f'./{out_file_name}', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            for call in calls:
                csv_writer.writerow(call.__dict__())
