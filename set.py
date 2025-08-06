s={10,20,30,40}
print("set:",s)

s.pop()
print("popped",s.pop())
print("set after pop:",s)

s.add(3)
print("set after adding 3:",s)

s.update([50,60])
print("updating 50 and 60:",s)

s.clear()
print("clear set:",s)


a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b)) 
print(b.difference(a)) 