import math
"""Variables"""
a=[2,1,0.4]
a1=[]
b=[0.8,2,1]
b1=[]
c=[8,0.1,0.2]
c1=[]
g1=a[0]+a[1]+a[2]
g2=b[0]+b[1]+b[2]
g3=c[0]+c[1]+c[2]
print(g1,g2,g3)
"""Function"""
print('First')
for i in range(len(a)):
         a1.append(a[i]/g1)
         print(a1,end=' ')
         print(type(a1))
print('\n')
print('Second')
for i in range(len(b)):
         b1.append(b[i]/g2)
         print(b1,end=' ')
         print(type(b1))
print('\n')
print('Third')
for i in range(len(c)):
         c1.append(c[i]/g3)
         print(c1,end=' ')
         print(type(c1))
print('\n')
print('So answer of this question is..')
answer1=abs(g1*(a1[0]*math.log2(a1[0])+a1[1]*math.log2(a1[1])))
answer2=abs(g2*(b1[1]*math.log2(b1[1])+b1[2]*math.log2(b1[2])+b1[0]*math.log2(b1[0])))
answer3=abs(g3*(1*math.log2(1)))
print(answer1,"+",answer2,"+",answer3,"=",answer1+answer2+answer3,'бит/условие')
