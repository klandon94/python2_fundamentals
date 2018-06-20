#Program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character

word_list = ['hello', 'world', 'my', 'name', 'is', 'Barry', 'WhOa']
char = 'o'
new_list = []

for word in word_list:
    if word.find(char) != -1:
        new_list.append(word)

print(new_list)