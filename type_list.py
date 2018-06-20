# A program that takes a list and prints a message for each element in the list, based on that element's data type
l = ['magical unicorns', 19, 'hello', 98.98, 'world']
l = [19,98.98,200]
l = ['magical', 'unicorns', 22]
sum_str = ''
sum_num = 0
str_am = 0
num_am = 0
for x in l:
    if type(x) == int or type(x) == float:
        sum_num += x
        num_am += 1
    if type(x) == str:
        sum_str += x + ' '
        str_am += 1

if num_am >= 1 and str_am >= 1:
    print('The list you entered is of mixed type')
    print('Sum:', sum_num)
    print('String: ' + sum_str)
elif num_am >= 1:
    print('The list you entered is of integer type')
    print('Sum:', sum_num)
elif str_am >= 1:
    print('The list you entered is of string type')
    print('String: ' + sum_str)