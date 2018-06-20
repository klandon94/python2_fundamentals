#A program that compares two lists and prints a message depending on if the inputs are identical or not

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,1]

list_one = ['milk', 'cereal', 'bananas']
list_two = ['milk', 'cereal', 'bannas']

# The easy way is to just compare the two lists with an '==' operator
# x = (list_one == list_two)
# print(x)

isSame = True
if (len(list_one) == len(list_two)):
    for x,y in zip(list_one, list_two):
        if x != y:
            isSame = False
            break   
else:
    isSame = False
if isSame == True:
    print('The lists are the same')
else:
    print('The lists are not the same')
