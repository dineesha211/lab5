import numpy as np
from matplotlib import pyplot as plt
N=4
n=np.arange(N)
x1=[1,2,3,4]
l1=len(x1)
o=np.linspace(-np.pi,np.pi,100)
for i in range(0,l1-1):
  y1=np.array([np.sum(x1[i]*np.exp(-1j*w*n)) for w in o])
x2=[4,3,2,1]
l2=len(x2)
for i in range(0,l2-1):
   y2=np.array([np.sum(x2[i]*np.exp(-1j*w*n)) for w in o])
x3=[5,5,5,5]
l3=len(x3)
for i in range(0,l3-1):
   y3=np.array([np.sum(x3[i]*np.exp(-1j*w*n)) for w in o])
y=y1+y2
print(y1)
print(y2)
print(y3)
if(y.all()==y3.all()):
  print("linearity")
else:
   print("non linear")
   
plt.subplot(2,1,1)
plt.plot(y)
plt.subplot(2,1,2)
plt.plot(y3)
plt.show()

