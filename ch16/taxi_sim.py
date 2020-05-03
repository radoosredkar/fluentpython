import collections
import queue

Event = collections.namedtuple("Event", "time proc allocation")


class Simulator:
    def __init__(self, proc_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(proc_map)

    def run(self, end_time):
        """Schedule and display events untill time is up"""
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print("***end of events***")
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print("taxi:", proc_id, proc_id * "   ", current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = "*** end of simulation time {} events pending ***"
            print(msg.format(self.events.qsize()))


def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change"""
    time = yield Event(start_time, ident, "leave garage")
    for i in range(trips):
        time = yield Event(time, ident, "pick up passanger")
        time = yield Event(time, ident, "drop off passanger")

    yield Event(time, Event, "going home")


def get_time(event: Event):
    print(event)
    return event[0]


taxis = {
    0: taxi_process(ident=0, trips=2, start_time=0),
    1: taxi_process(ident=1, trips=4, start_time=5),
    2: taxi_process(ident=2, trips=6, start_time=10),
}

sim = Simulator(taxis)
sim.run(150)

taxi = taxi_process(ident=13, trips=2, start_time=0)
time = get_time(next(taxi))
print(taxi.send(time + 7))
print(taxi.send(time + 23))
print(taxi.send(time + 5))
print(taxi.send(time + 48))
print(taxi.send(time + 1))
