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
