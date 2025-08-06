t = (10,20,20,30,40,50,60)
print("length:",len(t))

print("count of 20:",t.count(20))

print("index of 10:",t.index(10))

print("value:",t[0])  
print("value at index -1:",t[-1])

print("slicing:",t[1:4])


for i in t:
    print("tuple:",i)

t2 = (3, 4)
print("total tuples:",t + t2)

print("3 times of tuple:",t * 3)