class Call:

    def __init__(self, src: int, dest: int, type: int, time_coming: int):
        self.src = src
        self.dest = dest
        self.type = type
        self.allocated_to = -1
        self.time_coming = time_coming
        self.time_going_src = -1
        self.time_going_dest = -1
        self.time_done = -1
        self.allocated_to = None

    def allocated_to(self, elev):
        self.allocated_to = elev
