import csv
from models.elevator import Elevator

class Call:

    def __init__(self, src: int, dest: int, type: int, time_coming: float):
        self.src = src
        self.dest = dest
        self.type = type
        self.allocated_to = -1
        self.time_coming = time_coming
        self.time_going_src = -1
        self.time_going_dest = -1
        self.time_done = -1
        self.allocated_to = -1
        if src <= dest:
            self.direction = Elevator.UP
        else:
            self.direction = Elevator.DOWN

    def __str__(self):
        return f'src {self.src} ,dest {self.dest} , type {self.type}  , allocated_to {self.allocated_to}'

    def __repr__(self):
        return f'{{ src {self.src} ,dest {self.dest} , type {self.type}  , allocated_to {self.allocated_to} }}'

    def __dict__(self):
        return [
            'Elevator call',
            self.time_coming,
            self.src,
            self.dest,
            self.type,
            self.allocated_to
        ]

    @staticmethod
    def init_from_file(filepath):
        calls = []
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                calls.append(Call(src=int(row[2]), dest=int(row[3]), time_coming=float(row[1]), type=int(row[4])))
        return calls
