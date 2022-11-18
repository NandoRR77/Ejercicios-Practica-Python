import numpy as np

e = 5
print(e)

v = np.array([-4, 8, 5]) #creación vector v
print(v)


m = np.array([[1,0,-9],[3,-6,7]]) #creación matriz m
print(m)


e_array = np.array([5])
print(e_array)

m.shape #muestra de que dimension es el objeto
v.shape
e_array.shape


v.reshape(1,3) #redimensiona el vector, así mostrará un vector 1x3
v.reshape(3,1) #redimensiona el vector, así mostrará un vector 3x1
