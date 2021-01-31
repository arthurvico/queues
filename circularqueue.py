"""
Project 4 - Circular Queues
Name:
"""
from collections import defaultdict


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False

        if self.head != other.head or self.tail != other.tail:
            return False

        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False

        return True

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"

        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        """
        Returns whether or not the queue is empty (bool).
        :return: True if queue is empty, False if not.
        """
        if self.size == 0:
            return True
        return False

    def __len__(self):
        """
        Overrides the len() method.
        :return: the size of the queue.
        """
        return self.size

    def head_element(self):
        """
        This function returns the front element of the queue.
        :return: The front element of the queue.
        """
        return self.data[self.head]

    def tail_element(self):
        """
        This function returns the last element of the queue.
        :return: The back last of the queue.
        """
        return self.data[self.tail-1]

    def grow(self):
        """
        Doubles the capacity of the queue immediately when capacity is reached
        to make room for new elements. Moves the head to the front of the new allocated list.
        :return: None.
        """
        if self.size == self.capacity:
            old = self.data
            self.data = [None] * (self.capacity*2)
            current = self.head
            for i in range(self.size):
                self.data[i] = old[current]
                current = (1 + current) % self.capacity
            self.head = 0
            self.capacity = self.capacity*2
            self.tail = i+1

    def shrink(self):
        """
        Halves the capacity of the queue immediately if the size is 1/4 or less of the capacity
        Capacity will never go below 4. Moves the head to the front of the new allocated list.
        :return: None.
        """
        if self.size <= (self.capacity/4) and self.capacity >= 8:
            old = self.data
            self.data = [None] * (self.capacity // 2)
            current = self.head
            for i in range(self.size):
                self.data[i] = old[current]
                current = (1 + current) % self.capacity
            self.head = 0
            self.capacity = self.capacity // 2
            self.tail = i+1
        if self.capacity < 4:
            self.grow()

    def enqueue(self, val):
        """
        Add an element val to the back of the queue.
        :return: None.
        """
        self.data[self.tail] = val
        self.size += 1
        self.tail = (self.head + self.size) % self.capacity
        self.grow()

    def dequeue(self):
        """
        Remove an element from the front of a queue.
        :return: Value removed.
        """
        if self.is_empty():
            return None
        to_return = self.data[self.head]
        self.data[self.head] = None
        self.head = (1 + self.head) % self.capacity
        self.size -= 1
        self.shrink()
        return to_return


class QStack:
    """
    Stack class, implemented with underlying Circular Queue
    """
    # DO NOT MODIFY THESE METHODS
    def __init__(self):
        self.cq = CircularQueue()
        self.size = 0

    def __eq__(self, other):
        """
        Defines equality for two QStacks
        :return: true if two stacks are equal, false otherwise
        """
        if self.size != other.size:
            return False

        if self.cq != other.cq:
            return False

        return True

    def __str__(self):
        """
        String representation of the QStack
        :return: the stack as a string
        """
        if self.size == 0:
            return "Empty stack"

        str_list = [str(self.cq.data[(self.cq.head + i) % self.cq.capacity]) for i in range(self.size)]
        return "Stack: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------
    def push(self, val):
        """
        Adds an element, val, to the top of the stack.
        :return: None.
        """
        if self.cq.is_empty():
            self.cq.enqueue(val)
            self.size += 1
        else:
            self.cq.enqueue(val)
            for i in range(self.size):
                to_add = self.cq.dequeue()
                self.cq.enqueue(to_add)
            self.size += 1

    def pop(self):
        """
        Removes an element from the top of the stack.
        :return: Element popped, if empty, None.
        """
        if self.cq.is_empty():
            return None
        else:
            to_return = self.cq.dequeue()
            self.size -= 1
        return to_return


    def top(self):
        """
        Returns the top element of the stack but does not remove it.
        :return: Top element of the stack, if empty, None.
        """
        if self.size == 0:
            return None
        return self.cq.head_element()


def digit_swap(nums, replacements):
    """
    This function will replace numbers in nums however many times replacement is, to create
    the longest possible sequence of the same number.
    :nums: A list of numbers.
    :replacement: An integer to represent how many replacements are allowed
    :return: The amount of numbers in the longest sequence of numbers after the replacements
    """
    queue = CircularQueue()
    items = {}
    for number in nums:
        how_many_times = 0
        queue.enqueue(number)
        items = {number:how_many_times}



