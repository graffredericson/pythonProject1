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


def power(a, b):
    if a < 0 and b < 0:
        return -1
    elif a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b - 1)


def binary_search(numbers, num, start=0, end=0):
    if end >= start:
        mid = (end+start) // 2
        if numbers[mid] == num:
            return mid
        elif numbers[mid] > num:
            return binary_search(numbers, num, start, mid-1)
        else:
            return binary_search(numbers, num, mid+1, end)
    else:
        return -1

    # am ende jeder zeile gibt es eine line termination (\n)
    # wenn wir write benutzen überschreibt, lieber append verwenden
    # write wird hauptsächlich für neue Dateien
    # befehl rsplit ist eine Funktion, die für uns eine Zeile aufsplitet. () sortiert nach Leerzeichen; (,) nach Beistrichen; etc.



class Random(_random.Random):
    """Random number generator base class used by bound module functions.
    Used to instantiate instances of Random to get generators that don't
    share state.
    Class Random can also be subclassed if you want to use a different basic
    generator of your own devising: in that case, override the following
    methods:  random(), seed(), getstate(), and setstate().
    Optionally, implement a getrandbits() method so that randrange()
    can cover arbitrarily large ranges.
    """

    VERSION = 3  # used by getstate/setstate

    def __init__(self, x=None):
        """Initialize an instance.
        Optional argument x controls seeding, as for Random.seed().
        """

        self.seed(x)
        self.gauss_next = None


def shuffle(self, x, random=None):
    """Shuffle list x in place, and return None.
    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.
    """

    if random is None:
        randbelow = self._randbelow
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = randbelow(i + 1)
            x[i], x[j] = x[j], x[i]
    else:
        _warn('The *random* parameter to shuffle() has been deprecated\n'
              'since Python 3.9 and will be removed in a subsequent '
              'version.',
              DeprecationWarning, 2)
        floor = _floor
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = floor(random() * (i + 1))
            x[i], x[j] = x[j], x[i]
