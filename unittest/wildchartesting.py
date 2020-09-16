import re
str1="2301020200809002X"
str2="230102020****002X"
n1=len(str1)
n2=len(str2)
assert n1==n2
#print(n)
j=0
for i in range(n1):
    if str1[i]==str2[i]:
        pass
    elif str2[i]=="*":
        pass
    else:
        j=j+1
print(j)
        


#assert str1==str2