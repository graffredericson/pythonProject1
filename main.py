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


print(count_integer(lst, 3))

# Aufgabe 2

def list_func(numbers, integer):
    reverselist = []
    if integer in numbers:
        pass
    else:
        return reverselist
    for i in numbers:
        if numbers[i] == integer:
            numbers[i] = 6
        else:
            continue
    for i in range(len(numbers)):
        reverse = len(numbers) - 1
        reverse -= i
        reverselist.append(numbers[reverse])
    print(reverselist)

    return numbers


# Aufgabe 3

lst2 = [1, 4, 3, 3, 6, 7, 9, 0, 4, 0]


def compare_lists(list1, list2):
    empty_list = []
    for i in list1:
        if i == i in list2:
            empty_list.append(i)
        else:
            continue
    return empty_list


print(compare_lists(lst, lst2))


# Aufgabe 4

def remove_duplicates(lst):
    dupfree_lst = list(set(lst))
    return dupfree_lst


print(remove_duplicates(lst2))

# Aufgabe 5


my_dict = {"Type": "Notebook", "Brand": "Dell", "Price": 2000}

def dict_func(dictionary):
    print("You have a", dictionary["Type"], "from",  dictionary["Brand"], "that costs:", dictionary["Price"])
    dictionary["OS"] = "Linux"
    print(dictionary)
    dictionary.get("Type", "unknown type")
    dictionary.get("Brand", "unknown brand")
    dictionary.get("Price", "unknown price")
    return dictionary

print(dict_func(my_dict))
