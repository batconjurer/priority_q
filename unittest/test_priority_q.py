import unittest
import priority_queue



class TestPriorityQueue(unittest.TestCase):

    def test_init_size(self):
        pqueue = priority_queue.PyPQ()
        self.assertEqual(pqueue.size(), 0)
        self.assertEqual(pqueue.empty(), True)
        self.assertRaises(IndexError, lambda: pqueue.pop())

    def test_add(self):
        pqueue = priority_queue.PyPQ()
        pqueue.insert((1, 1))
        self.assertEqual(pqueue.size(), 1)
        self.assertEqual(pqueue.get_items(), [1])
        self.assertEqual(pqueue.empty(), False)

    def test_delete(self):
        pqueue = priority_queue.PyPQ()
        pqueue.insert((1, 1))
        self.assertEqual(pqueue.pop(), (1.0, 1))
        self.assertEqual(pqueue.size(), 0)
        self.assertEqual(pqueue.empty(), True)

    def test_insert_even(self):
        pqueue = priority_queue.PyPQ()
        first_list = list(range(10))
        for i in range(10):

            for element in first_list:
                pqueue.insert((element, element))
            self.assertEqual(sorted(pqueue.get_items()), first_list)
            self.assertEqual(pqueue.size(), 10)
            self.assertEqual(pqueue.pop(), (0, 0))
            pqueue.clear()

    def test_insert_odd(self):
        pqueue = priority_queue.PyPQ()
        first_list = list(range(11))
        for i in range(11):
            for element in first_list:
                pqueue.insert((element, element))

            self.assertEqual(sorted(pqueue.get_items()), first_list)
            self.assertEqual(pqueue.size(), 11)
            self.assertEqual(pqueue.pop(), (0, 0))
            pqueue.clear()