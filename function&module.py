
def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
if n>m:
    m,n=n,m

print(factorial(m) // factorial(n) // factorial(m - n))