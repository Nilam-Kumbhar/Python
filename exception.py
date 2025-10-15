class a:
    n=6
    try:
        res=n/0
    except ZeroDivisionError:
        print("cant divide by zero.")
    else:
        print("division:",res)
    finally:
        print("program completed")    


n1=int(input("enter a no.1: "))
n2=int(input("enter a no.2:"))
try:
    res=n1/n2
except ZeroDivisionError :
    print("cannot divide by zero!")   
else:
    print("division of no.s:",res)
finally:
    print("sucessfully completed.")            
