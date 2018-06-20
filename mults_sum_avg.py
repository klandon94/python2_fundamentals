# Prints all the odd numbers from 1 to 1000 using a for loop
for count in range(1,1001):
    if(count%2 == 1):
        print(count)

# Prints all the multiples of 5 from 5 to 1,000,000
for count in range(5,1000000):
    if(count%5 == 0):
        print(count)

# Prints the sum of all the values in the list
a = [1,2,5,10,255,3]
sum = 0
for val in a:
    sum+=val
print(sum)
print(sum/len(a)) # Prints the average of the values in the list

# Separate program that will print just the average of values
a = [10,20,30,40]
sum = 0
for val in a:
    sum+=val
print(sum/len(a))