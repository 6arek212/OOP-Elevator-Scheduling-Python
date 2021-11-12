import csv


# from elevator import Elevator

class Call:
    UP, DOWN, LEVEL = 1, -1, 0

    def __init__(self, time_coming, src, dest, type):
        self.src = src
        self.dest = dest
        self.type = type
        self.time_coming = time_coming

        if src >= dest:
            self._direction = Call.DOWN
        else:
            self._direction = Call.UP

    def __str__(self):
        return f"Elevator call, src: {self.src} ,  dest: {self.dest} , type: {self.type} , time_coming: {self.time_coming}\n"

    def __repr__(self):
        return f"Elevator call, src: {self.src} ,  dest: {self.dest} , type: {self.type} , time_coming: {self.time_coming}\n"

    def call_F(file_name):
        calls = []

        with open(file_name, 'r') as csv_f:
          csv_reader = csv.reader(csv_f)

          for row in csv_reader:
            # print(row[1])
            c = Call(float(row[1]), int(row[2]), int(row[3]), int(row[4]))
            # print("c: >>" , c)

            calls.append(c)

        return calls


if __name__ == '__main__':
    calls = Call.call_F("c1.text")
    print(calls)
