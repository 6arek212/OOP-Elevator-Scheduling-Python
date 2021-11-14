from .elevator import Elevator


class ElevatorManager:
    def __init__(self, elevator: Elevator):
        self.elevator = elevator
        self.start_direction = None
        self.up_calls = []
        self.down_calls = []

    def add_call(self, call):
        if self.start_direction is None:
            self.start_direction = call.direction
        if call.direction == Elevator.UP:
            self.up_calls.append(call)
        else:
            self.down_calls.append(call)
        print(f'{call.src} ---> {call.dest}  call got added to ', self.elevator.id)

    def get_next_call(self):
        pass

    def elevator_status_at(self, time):
        ':returns (currnet_up_calls , currnet_down_calls , elevator_pos)      '

    def estimated_time_to(self, call):
        (up_calls, down_calls, elv_pos, going_to) = self.elevator_status_at(call.time_coming)
        time = 0
        if going_to is None:
            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(elv_pos - call.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time

            time += self.elevator.close_time + self.elevator.stop_time
            time += abs(call.src - call.src) / self.elevator.speed
            time += self.elevator.close_time + self.elevator.start_time
            return time

        direction = Elevator.UP if elv_pos <= going_to else Elevator.DOWN

        if direction == Elevator.UP and call.direction == Elevator.UP:
            pass

        if direction == Elevator.DOWN and call.direction == Elevator.UP:
            pass

        if direction == Elevator.DOWN and call.direction == Elevator.DOWN:
            pass

        if direction == Elevator.UP and call.direction == Elevator.DOWN:
            pass


        return time
