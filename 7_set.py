###############################################################
#####集合交集，并集，差集
###############################################################
list0=[1,2,3,4,5,6,7,8,9]
list1=[5,6,7,8,9,10,11,12,13,14]

print (set(list0)&set(list1))
print (set(list0)|set(list1))
print (set(list0)-set(list1))
###############################################################
#####集合可用于成员检测，去重，集合计算等，但其不支持切片，索引
###############################################################
set0=set((1,2))
print (1 in set0)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

###############################################################
#####remove相对于discard。如果没有此元素将会报错
###############################################################
thisset.discard("Runoob")
print(thisset)