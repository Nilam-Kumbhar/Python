import array as arr
a=arr.array('i',[1,2,3])
print("array",end=" ")
for i in range(0,3):
    print(a[i],end=" ")

a.append(4)
print("\narray after append;",a.tolist())

a.insert(2, 99)
print("After insert(2, 99):",a.tolist())

a.extend([70, 80])
print("After extend([70, 80]):", a.tolist())

a.pop() 
print("After pop():", a.tolist())

a.pop(2)  
print("After pop(2):", a.tolist())

a.remove(4)  
print("After remove(4):", a.tolist())

print("Index of 70:", a.index(70))

a.reverse()
print("After reverse():", a.tolist())

print("Count of 10:", a.count(10))