#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        i = b = 0
        if not self.__head:
            self.__head = new
            return
        if new.data < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current:
            if new.data > current.data:
                current = current.next_node
                i += 1
            else:
                break
        current = before = self.__head
        while b < i:
            current = current.next_node
            if b > 0:
                before = before.next_node
            b += 1
        new.next_node = current
        before.next_node = new

    def __str__(self):
        llist = ""
        current = self.__head
        while current:
            llist += str(current.data)
            current = current.next_node
            if current:
                llist += '\n'
        return llist
