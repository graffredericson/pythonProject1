# Aufgabe 1

lst = [1, 2, 3, 3, 4, 3, 7, 3, 8]

def count_integer(numbers, integer):
    Anzahl = 0
    for i in numbers:
        if i == integer:
            Anzahl += 1
        else:
            continue
    if Anzahl != 0:
        return Anzahl
    else:
        return 42


count_integer(lst, 1)

# Aufgabe 2

def list_func(numbers, integer):
    reverselist = []
    anzahl = 0
    bumbers = numbers[:]
    for i in bumbers:
        if i == integer:
            anzahl += 1
        else:
            continue
    if anzahl == 0:
        return reverselist
    stelle = -1
    for i in bumbers:
        stelle += 1
        if i == integer:
            bumbers[stelle] = 6
        else:
            continue
    for i in range(len(bumbers)):
        reverse = len(bumbers) - 1
        reverse -= i
        reverselist.append(bumbers[reverse])
    print(reverselist)
    return bumbers

print(list_func(lst, 3))


# Aufgabe 3

lst2 = [1, 4, 3, 3, 6, 7, 9, 0, 4, 0]


def compare_lists(list1, list2):
    empty_list = []
    for i in list1:
        if i == i in list2:
            empty_list.append(i)
        else:
            continue
    dupfree_lst = list(set(empty_list))
    return dupfree_lst


print(compare_lists(lst, lst2))


# Aufgabe 4

def remove_duplicates(lst):
    dupfree_lst = list(set(lst))
    return dupfree_lst


remove_duplicates(lst2)

# Aufgabe 5


my_dict = {"Type": "Notebook", "Brand": "Dell", "Price": 2000}

def dict_func(dictionary):
    if "Type" not in dictionary:
        type = "unknown type"
    else:
        type = dictionary["Type"]
    if "Brand" not in dictionary:
        brand = "unknown brand"
    else:
        brand = dictionary["Brand"]
    if "Price" not in dictionary:
        price = "unknown price"
    else:
        price = dictionary["Price"]
    print("You have a", type, "from",  brand, "that costs:", price)
    dictionary["OS"] = "Linux"
    print(dictionary)
    return dictionary

print(dict_func(my_dict))


