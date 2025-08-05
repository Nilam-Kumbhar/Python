n=int(input("enter a number:"))
for i in range(2,n):
    if n%i==0:
        print(n,"is not a prime no.")
        break
else:
    print(n, "is a prime no.")
