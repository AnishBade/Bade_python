L1=[3,4,5]
L2=[1,2,3]
'''L3=[]
L4=list(zip(L1,L2))//this makes list of tuples
for (x1,x2) in L4:
    L3.append(x1+x2)
'''
L3=[x1+x2 for (x1,x2) in zip(L1,L2)]
print(L3)