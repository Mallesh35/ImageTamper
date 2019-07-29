import i2
import image_tamper
import numpy as np
i=np.int8
l1=[]
l2=[]
l3=[]
l11=[]
l22=[]
for i in i2.diff_list:
	l1.append(i)
for i in image_tamper.diff_list1:
	l2.append(i)

print(l1)
print('\n')
print(l2)
print('\n')
l1=[float(i) for i in l1]
l2=[float(j) for j in l2]
l=len(l1)
for i in range(0,l):
	l3.append(l1[i]-l2[i])
print(l3)
	