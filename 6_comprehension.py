###############################################################
#####列表中每个元素的平方生产一个新的列表 [x_expr for x in iterable if condition ]
#####把一个序列或是其他可迭代对象中的元素过滤或是加工，然后再创建一个新的列表
###############################################################
list0=[1,2,3,4,5,6,7,8,9]
list1=[]
list2=[]
list3=[]

for i in range(len(list0)):
  list1.append(list0[i]**2)
print (list1)

list2=list(map(lambda x: x**2, list0))
print (list2)

list3=[x**2 for x in list0]
print (list3)

###############################################################
#####嵌套
###############################################################
a='abc'
b=[1,2,3]
print ([(x,y) for x in a for y in b ])
###############################################################
#####字典推导式
###############################################################
print ({k:v for k,v in enumerate(('a','b','c'))})
print ({k:v for k,v in zip((1,2,3),('a','b','c'))})
###############################################################
#####集合推导是花括号，列表推导是方括号，生成器表达式是圆括号。
##### 生成器表达式相对于列表推导式的优势在于，它得到的是一个生成器，只有在需要的时候，才会计算新的值，从而节省内存。
###############################################################