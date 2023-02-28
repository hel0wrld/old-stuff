import numpy as np
a=np.array([[12,0,0],[1,5,0],[3,7,14]])
print(a)
b=np.linalg.inv(a)
print(b)
c=np.array([[1,28,76]]).T
d=np.cross(b,c)
print(d)