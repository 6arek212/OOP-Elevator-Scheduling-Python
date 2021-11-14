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

    def sim(self, call):
        time = 0

        while time < call.time_coming:
            'must be on a spread thread'
            self.elevator.go_to(self.get_next_call())

        'can pick it up'
        if call.direction == Elevator.UP and self.elevator.state == Elevator.UP and self.elevator.position <= call.src:
            pass

        if call.direction == Elevator.DOWN and self.elevator.state == Elevator.DOWN and self.elevator.position >= call.src:
            pass

        if self.elevator.going_to is None:
            time = self.elevator.close_time + self.elevator.start_time
            time += abs(self.elevator.position - call.src) / self.elevator.speed
            time += self.elevator.stop_time + self.elevator.open_time

            time = self.elevator.close_time + self.elevator.start_time
            time += abs(self.elevator.position - call.dest) / self.elevator.speed
            time += self.elevator.stop_time + self.elevator.open_time

        return time
