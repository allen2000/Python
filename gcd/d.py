def gcd(a, b):
   if a > b:
       smaller = b
   else:
       smaller = a
 
   for i in range(1,smaller + 1):
       if((a % i == 0) and (b % i == 0)):
           gcd = i
   return gcd

n1 = int(input("输入第一个数字: "))
n2 = int(input("输入第二个数字: "))
 
print( n1,"和", n2,"的最大公约数为", gcd(n1, n2))