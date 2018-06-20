# for row in range(1,13):
#     for col in range(1,13):
#         print(row * col, end='\t')
#     print()

for row in range(13):
    for col in range(13):

        num = row*col

        if num<10:
            space = '  '
        elif 10<=num<100:
            space = ' '
        elif num>=100:
            space = '' 

        if col == 0:
            if row == 0:
                print('x', end='')
            else:
                print(row, end='')

        elif row == 0:
            if col<10:
                print('  ', col, end='')
            else:
                print(' ', col, end='')

        else:
            print(space, num, end='')

    print()