set1 = set((1, 2, 3))
set2 = set([3, 4, 5])
set3 = {1, 2, 9}
print(set1.intersection(set3))
print(set1.issubset(set3))
print(set3.issubset(set1))
print(set3.difference(set1))
print(set1.symmetric_difference(set2))
print(set1.union(set2).union(set3)) # {1, 2, 3, 4, 5, 9}

print(set1 - set2 - set1,  set1 & set3, set1 | set2 | set3, set1 ^ set2)

#set1.difference_update(set2, set3)
#print(set1)
#set2.intersection_update(set1)
set2 &= set1
print(set2)

new_elements = ['seven, eight', 'nine']
#for el in new_elements:
#    set2.add(el)
#set2.update(set(new_elements))
#set2.add('sewen')
set2 |= set(new_elements)
print(set2)

set2.discard('nine')
set2.discard('ten') #удаление в тихую если нет элемента
#set2.remove('ten') #ошибка еслм нет такого элемента
set2.pop()
print(set2)
