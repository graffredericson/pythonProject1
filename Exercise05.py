import math

#1
def power(a, b):
    if a > 0 and b > 0:
        return (a * a) * (b - 1)
    else:
        return -1

#print(2**2)
print(power(8, 2))

#2
def binary_search(numbers, num):
    #num = int
    #numbers = []
    start = 0  # die Variable "start" bezieht sich auf den Wet an Stelle Null
    end = len(numbers)-1  # die Variable "end" bezieht sich auf die letzte Stelle, also die wie lang die Liste ist
    while start <= end:
        middle = (end + start)//2
        if numbers[middle] > num:
            end = middle - 1
        elif numbers[middle] < num:
            start = middle + 1
        else:
            return middle
    return -1

mylist = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print(binary_search(mylist, 3))

#3
class HashTable():
    def __init__(self, size=60):
        self.size = size
        self.anzahl = 0
        self.elements = []
        while size > 0:
            self.elements.append([])
            size -= 1


    #4
    def __my_hash(self, element):
        count = 0
        if isinstance(element, int):
            while element > 0:
                element = element // 10
                count = count + 1
            return count
        else:
            return len(element)

    #5
    def insert(self, element):
        self.elements[self.__my_hash(element)].append(element)
        self.anzahl += 1
        return self.elements

    #6
    def get_element(self, element):
        #prüft, ob element vorhanden
        #löscht element
        #returned element
        for i in self.elements[self.__my_hash(element)]:
            if i == element:
                self.elements[self.__my_hash(element)].remove(i)
                return element
        return False

    #7
    def get_size(self):
        count = 0
        for i in self.elements:
            count += 1
        return count



myhashtable = HashTable()
(myhashtable.insert("reinhard"))
(myhashtable.insert("pappel"))
(myhashtable.insert("kein"))
(myhashtable.insert(45))
(myhashtable.insert(306))
(myhashtable.insert(676))
(myhashtable.insert(666))
(myhashtable.insert(2222))
#print(myhashtable.insert(000))

#print(myhashtable.get_element(2222))
#print(myhashtable.insert(1))

#print(myhashtable.get_size())


