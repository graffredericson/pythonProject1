import numpy as np

bill = 10**7

lst = [1] * bill
arr = np.ones((bill), dtype=int)
print(lst.__sizeof__())
print(arr.__sizeof__())

lst = [1, 2, 3, 4]
remove_lst = []
for i in lst:
    if i >= 3:
        remove_lst.append(i)
for i in remove_lst:
    print(lst)

for i in lst:  # Aufgabe 4
    if i not in lst_2:
        lst_2.append(i)
    else:
        continue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

# das was jetzt steht ist von mir

    def clear(self):
        self.head = None # wir arbeiten uns immer vom direkten pointer weg, wenn wir den wegnehmen sind alle anderen pointer pointless
        self.size = 0



matrix = [[] for x in range(6)]
print(matrix)

def default_param(text = "hello"):
    print(text)

default_param()