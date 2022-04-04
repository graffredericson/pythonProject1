#1

def count_vowels(text):
    count = text.lower().count("e") + text.lower().count("a") + text.lower().count("i") + text.lower().count("u") + text.lower().count("o")
    if count == 0:
        return 42
    else:
        return count


#print(count_vowels("45"))


#2

def hamming(text1, text2):
    distance = 0
    if len(text1) == len(text2):
        for i, j in zip(text1, text2):
            if i != j:
                distance += 1
        return distance
    else:
        return 0


print(hamming("Ahrg", "OwOgiojl"))


#3

class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        print("Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors))


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        print("Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers))


car01 = Car("orange", "diesel", 4)
#Car.all_doors(car01)


#4


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0}, {1}".format(self.name, self.author)


book1 = Book("Dune", "Frank Herbert")
book2 = Book("Das flüssige Land", "Raphaela Edelbauer")
book3 = 42
book4 = Book("Engelbert", "Frank Herbert")

list = [book1, book2, book3, book4]

#print(book1)

#5


class BookShelf:
    bookshelf = []

    def add_book_list(self, books):

        for i in books:
            if i.__class__ is Book:
                self.bookshelf.append(i)

    def books_by_author(self, author):
        names = []
        for i in self.bookshelf:
            if i.author is author:
                names.append(i.name)
        return names

    def get_books(self):
        names = []
        for i in self.bookshelf:
            names.append(i.name)
        return names

    def clear_shelf(self):
        self.bookshelf.clear()


bookshelf1 = BookShelf()

bookshelf1.add_book_list(list)
print(bookshelf1.get_books())
print(bookshelf1.books_by_author("Frank Herbert"))
bookshelf1.clear_shelf()
print(bookshelf1.get_books())
print(bookshelf1.books_by_author("Frank Herbert"))



