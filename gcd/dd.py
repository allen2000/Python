def gcd(a, b):
    t=0
    if a > b:
      t = b
    else:
      t = a
   list0 = [i for i in range(1,t + 1)]
   if((a % i == 0) and (b % i == 0)):
       gcd = i
   return gcd

n1 = int(input("输入第一个数字: "))
n2 = int(input("输入第二个数字: "))
 
print( n1,"和", n2,"的最大公约数为", gcd(n1, n2))