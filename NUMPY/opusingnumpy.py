import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([[1,2],[3,4]])
c=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,12,13]]])
print("1D array:\n",a)
print(f"no. of element (row column):{a.shape} dimension: {a.ndim}")
print("2D array:\n",b)
print(f"no. of element (row column):{b.shape} dimension: {b.ndim}")
print("3D array:\n",c)
print(f"no. of element (row column):{c.shape} dimension: {c.ndim}")

print("reshape 1D in (2,3):\n",a.reshape(2,3))

#oprations
print("oprations on 1D array:")
d=np.array([10,20,30,40])
e=np.arange(4)
print(d)
print(e)
c=d+e
print(c)
print(e**2)

print("oprations on 2D array:")
f=np.array([[1,2],[4,5]])
g=np.array([[7,8],[3,4]])
print("matrix 1:\n",f)
print("matrix 2:\n",g)
print("addition of mAtrix 1 and 2:\n",f+g)
print("multiplication of mstrix 1 and 2:\n",f@g)

