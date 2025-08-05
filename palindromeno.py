<<<<<<< HEAD
n=int(input("enter a number:"))
reverse=0
temp=n
while n>0:
    a=n%10
    reverse=reverse*10+a
    n=n//10
if temp==reverse:
    print(temp,"numbher is a palindrome.")
else:
=======
n=int(input("enter a number:"))
reverse=0
temp=n
while n>0:
    a=n%10
    reverse=reverse*10+a
    n=n//10
if temp==reverse:
    print(temp,"numbher is a palindrome.")
else:
>>>>>>> 35b91a352e40226b495cea534a9c78020b6b6caf
    print(temp,"number is not a palindrome.")    