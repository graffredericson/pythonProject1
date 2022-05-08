'''Class Template for a singly linked list Head -> Tail convention
Exercise Part starts at line 40'''

# class for holding the data, defaults to empty node if no data is given


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node


# Class for managing the list and nodes


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

    '''
        Exercise Part 1,2 and 3:
        Implement the given methods below according to the requirements in the exercise sheet.
        return the correct data types and values
        
    '''

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        print("Nothing to find here :(")

    def get_data(self, data):
        iter_list = iter(self)
        i = 0
        while i < self.get_size():
            i += 1
            if next(iter_list) == data:
                return data
        return False

    def delete(self, data):
        global previous
        current = self.head
        if self.size < 2:
            if current.data == data:
                self.head = None
        else:
            i = 0
            while current.data != data:
                if self.size < i:
                    return
                else:
                    i += 1
                    previous = current
                    current = current.next
            previous.next = current.next
            self.size -= 1
        return

itemlist = SinglyLinkedList()
itemlist.append(12)
itemlist.append(34)
itemlist.append(45)
itemlist.append(56)


objectlist = SinglyLinkedList()
objectlist.append(55)
objectlist.append(66)

#print(itemlist.get_data(45))
#itemlist.delete(45)
#print(itemlist.get_data(45))

'''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
    to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
    in the code to reflect the new class name (NodeDLL instead of Node).
    '''


class NodeDLL:
    def __init__(self, data=None):
        self.previous = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data, front):
        node = NodeDLL(data)
        if  self.tail is None:
            self.tail = node
            self.head = node
            self.size = 1
            return

        if front:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.size += 1

        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
            self.size += 1
        return


    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        print("Nothing to find here :(")

    def get_data(self, data):
        iter_listDLL = iter(self)
        i = 0
        while i < self.get_size():
            i += 1
            if next(iter_listDLL) == data:
                return data
        return False

    def delete(self, data):
        current = self.head
        first = self.tail
        if first.data == data:
            self.tail = first.previous
            first.previous.next = None
        if current.data == data:
            self.head = current.next
            current.next.previous = None
        else:
            if self.size < 2:
                if current.data == data:
                    self.head = None
            else:
                i = 0
                while current.data != data:
                    if self.size < i:
                        return
                    else:
                        i += 1
                        previous = current
                        current = current.next
                previous.next = current.next
                self.size -= 1
            return

thingslist = DoublyLinkedList()
thingslist.append(60, True)
thingslist.append(24, True)
thingslist.append(99, True)
thingslist.append(36, True)
thingslist.append(77, True)
thingslist.append(12, True)

print(thingslist.get_size())
print(thingslist.get_data(12))
#thingslist.delete(12)
#print(thingslist.get_data(12))

'''Exercise Part 5 and 6:
    Complete the classes below to implement a stack and queue data structure. You are free to use built-in
    methods but you have to complete all methods below. Always return the correct data type according
    to the exercise sheet'''

class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        return self.stack

    def pop(self):
        return self.stack.pop()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return "nothing here"

    def size(self):
        return len(self.stack)


mystack = MyStack()

mystack.push(2)
mystack.push(1)
mystack.push(4)
mystack.push(3)
mystack.push(7)
print(mystack.push(5))
print(mystack.top())
print(mystack.pop())
print(mystack.top())
print(mystack.size())


class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)
        return self.queue

    def pop(self):
        return self.queue.pop()

    def show_left(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return "nothing here"

    def show_right(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return "nothing here"

    def size(self):
        return len(self.queue)


myqueue = MyQueue()

myqueue.push(2)
myqueue.push(1)
myqueue.push(4)
myqueue.push(3)
myqueue.push(7)
print(myqueue.push(5))
print(myqueue.show_left())
print(myqueue.pop())
print(myqueue.show_left())
print(myqueue.size())