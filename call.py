class Call:
    init = 0
    going_to_src = 1
    going_to_dest = 2
    done = 3

    up = 1
    down = -1

    def __init__(self, src: int, dest: int, type: int, time_coming: int):
        self.state = Call.init
        self.src = src
        self.dest = dest
        self.type = type
        self.allocated_to = -1
        self.time_coming = time_coming
        self.time_going_src = -1
        self.time_going_dest = -1
        self.time_done = -1
        self.allocated_to = None


    def get_time(self, state):
        if state == Call.init:
            return self.time_coming

        if state == Call.going_to_src:
            return self.going_to_src

        if state == Call.going_to_dest:
            return self.going_to_dest

        return self.done

    def allocated_to(self, elev):
        self.allocated_to = elev
