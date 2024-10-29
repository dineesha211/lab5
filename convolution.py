import numpy as np 
from matplotlib import pyplot as plt

x1=[1,2,3,4]
x2=[5,6,7,8]
convolved_length=len(x1)+len(x2)-1
x3=np.zeros(convolved_length)
for i in range(convolved_length):
	for j in range(len(x2)):
		if i-j>=0 and i-j<len(x1):
			x3[i]+=x1[i-j]*x2[j]
print(x3)
N=4
n=np.arange(N)
x1=[1,2,3,4]
l1=len(x1)
o=np.linspace(-np.pi,np.pi,100)
for i in range(0,l1-1):
  y1=np.array([np.sum(x1[i]*np.exp(-1j*w*n)) for w in o])
x2=[5,6,7,8]
l2=len(x2)
for i in range(0,l2-1):
   y2=np.array([np.sum(x2[i]*np.exp(-1j*w*n)) for w in o])
y3=y1*y2
print(y3)
if(x3.all()==y3.all()):
   print("convolution")
plt.subplot(2,1,1)
plt.plot(x3)
plt.subplot(2,1,2)
plt.plot(y3)
plt.show()

