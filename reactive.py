import reactivex as rx
from reactivex import operators as ops

observable = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

composed = observable.pipe(
    ops.map(lambda s: len(s)),
    ops.filter(lambda i: i >= 5)
)
composed.subscribe(lambda value: print("Received {0}".format(value)))

# nodes:
# planner
# robot

# topic: location (x,y)

location_observable = rx.of((0,0),(0,1),(1,0),(1,1))

class Node:
    def send(x,y):
        location_observable.publish_value(x,y)
    def receive(f):
        location_observable.subscribe(lambda value: f(value))

class Planner(Node):
    def next_location(x,y):
        return x + 1, y

class Robot(Node):
    def send_location():
        pass
