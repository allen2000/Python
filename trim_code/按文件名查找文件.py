""" import os
path='E:/1'
name='2020'
result=[]

for root,dirs,files in os.walk(path):
    for file in files:
        if name in file:
            result.append(os.path.join(root, file)) """

""" list0=os.listdir(path)
for i in range(0,len(list0)-1):
    if name in list0[i]:
        print (f"{i}"+"   "+list0[i])
        result.append(f"{i}"+"   "+list0[i])
print (result)

for i in range(0,len(result)):
    #print (i)
    print (f"{i}" + " "+result[i])

    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}×{i}={i*j}",end="\t")
        print(" ")"""

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}×{i}={i*j}",end="\t")
    print(" ")