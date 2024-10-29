import numpy as np
from matplotlib import pyplot as plt
N=7
n=np.arange(N)
x1=[1,2,3,4,0,0,0]
l1=len(x1)
o=np.linspace(-np.pi,np.pi,100)
for i in range(0,l1-1):
  y1=np.array([np.sum(x1[i]*np.exp(-1j*w*n)) for w in o])
x2=np.append(np.zeros(3),x1)
l2=len(x2)
for i in range(0,l2-1):
   y2=np.array([np.sum(x2[i]*np.exp(-1j*w*n)) for w in o])
print(y1)
print(y2)
y=y1*np.exp(-1j*o*3)  
print(y)
if(y.all()==y2.all()):
  print("time shifting")
else:
  print("not")
plt.subplot(2,1,1)
plt.plot(y)
plt.subplot(2,1,2)
plt.plot(y2)
plt.show()
 
