
def find_divisor(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return find_divisor(b,a%b)

n1 = int(input("输入第一个数字: "))
n2 = int(input("输入第二个数字: "))
print(find_divisor(n1,n2))