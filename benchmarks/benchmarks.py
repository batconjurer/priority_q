import heapq
import priority_queue
import numpy.random as nprand


class TimePQ:
    """
    A benchmark that times the performance of pythons native heapq module and
    a custom cython wrapped version of c++'s priority queue.
    """
    def setup(self):
        nprand.seed(152535)
        self.heap = []
        self.pqueue = priority_queue.PyPQ()
        self.rand_list = list(nprand.permutation(1000))
        self.big_rand_list = list(nprand.permutation(100000))

    def time_heapq(self):
        for item in self.rand_list:
            heapq.heappush(self.heap, (item, item))
        for _ in range(1000):
            heapq.heappop(self.heap)

    def time_priority_q(self):
        for item in self.rand_list:
            self.pqueue.insert((item, item))
        for _ in range(1000):
            self.pqueue.pop()

    def peakmem_heapq(self):
        for item in self.big_rand_list:
            heapq.heappush(self.heap, (item, item))
        for _ in range(100000):
            heapq.heappop(self.heap)

    def peakmem_priority_q(self):
        for item in self.big_rand_list:
            self.pqueue.insert((item, item))
        for _ in range(100000):
            self.pqueue.pop()

