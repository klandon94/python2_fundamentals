# x = 3
# y = type(3)
# if (y == str):
#     print('true')
# else:
#     print('false')

# Given some value, tests the value for its type
x = [1,9,10,3,3,3,3,3,333,3]
if (type(x) == int):
    if (x >= 100):
        print("That's a big number!")
    else:
        print("That's a small number")
elif (type(x) == str):
    if (len(x) >= 50):
        print("Long sentence")
    else:
        print("Short sentence")
elif (type(x) == list):
    if (len(x) >= 10):
        print("Big list!")
    else:
        print("Short list")
