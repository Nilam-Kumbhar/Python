# Create a list
l = [5, 2, 9, 1, 5, 6]
print("Original List:",l)

l.append(4)
print("appending 4:",l)

l.insert(1, 10)
print("list after inserting 1  and 10:",l)

b = [3, 4]
l.extend(b)
print("list after combineing l and b:",l)  

l.remove(2)
print("list after removing 2:",l)

x = l.pop()
print("popped",x)       
print("list after pop:",l)

l.clear()
print("clearlist:",l)

l = [1, 2, 2, 3]
print("count of 2:",l.count(2))

l.sort()
print("sorted list:",l)

l.reverse()
print("reverse list:",l)