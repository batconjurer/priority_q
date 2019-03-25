from priority_queue import PyPQ


class FancyClass(object):

    def __init__(self):
        self.string = "I'm Fancy"

    def __str__(self):
        return self.string


pq = PyPQ()
x = FancyClass()
y = FancyClass()
z = FancyClass()
pq.insert((2, x))