def gcd(a,b):
    t = a, b
    if a < b:
        a, b = b, a
    r = a % b