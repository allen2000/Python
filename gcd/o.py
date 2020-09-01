def gcd(a,b):
    t = a, b
    if a < b:
        a, b = b, a
    r = a % b
    while r != 0:
        print(a,b,r)
        a = b
        b = r
        r = a % b
    print("GCD(%d, %d) is %d" % (t + (b, )))

gcd(34,21)
