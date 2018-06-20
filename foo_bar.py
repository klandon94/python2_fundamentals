
#For a given range, prints the number and an identifier: whether it is prime, a perfect square, or neither

print("Foo = Prime, Bar = Perfect square, FooBar = Neither")
for num in range(2,26):
    isPrime = True
    isSquare = False
    for x in range (2,num):
        if num%x == 0:
            isPrime = False
        if num/x == x:
            isSquare = True
    if isPrime:
        print(num,'- Foo')
    elif isSquare:
        print(num,'- Bar')
    else:
        print(num,'- FooBar')
