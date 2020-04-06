###############################################################
#####元组拆包
#####*代表剩下的元素，_相当于占位符，去除用。
###############################################################
tuple0=('allen','male','38')
name,gender,age=tuple0
print (name+":"+gender+","+age)
a,b,*rest=range(5)
print (rest)
c,_=(0,1)
print (c)
x,*_,y=(1,2,3,4,5)
print (y)
###############################################################
#####*args 是用于接收多余的未命名参数，**kwargs 用于接收实参中的命名参数.
##### 其中 args 是一个元组类型，而 kwargs 是一个字典类型的数据。
##### 形参中的 *args 把传进来的数据放在了 args 这个元组中。把 **kwargs 传进来的数据放在了 kwargs 这个字典中。
#####*args 其实就是把元组中的数据进行拆包;**kwargs 就是把字典中的数据进行拆包;
###############################################################
def print_number(*args):
    for a,b in enumerate(args):
        print ('{0}.{1}'.format(a,b))
print_number('allen','bill','crystal','dell')
print ('-----------------------------------------------------')
def table_items(**kwargs):
    for name,item in kwargs.items():
        print('{0}={1}'.format(name,item))

table_items(apple='fruit',cup='container',cat='pet')
print ('-----------------------------------------------------')
def test(re_item,*args,**kwargs):
    print(re_item)
    if args:
        print(args)
    if kwargs:
        print(kwargs) 
test('test','a','b','c',a='1',b='2',c='3')