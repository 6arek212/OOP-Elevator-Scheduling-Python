import elevator
import data
import elevator_ds as ElevatorDS


def allocate_call():
    pass


def move_elevators(elev: elevator, ds: ElevatorDS):
    if elev.state == elevator.LEVEL:
        elev.go_to(ds.get_next())


print(data.get_calls())
