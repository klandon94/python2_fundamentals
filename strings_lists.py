# Find and replace
words = "It's thanksgiving day. It's my birthday too!"
print(words.find("day"))
print(words.replace("day", "month"))

# Min and max
x = [2,54,-2,7,12,98]
print('min:',min(x),',','max:',max(x))

# First and last
x = ['hello', 2, 54, -2, 7, 12, 98, 'world']
print(x[0], x[len(x)-1])
print([x[0],x[len(x)-1]])

# New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
x1 = x[:len(x)//2]
x2 = x[len(x)//2:]
x2.insert(0,x1)
print(x2)