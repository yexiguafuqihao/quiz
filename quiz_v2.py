def sum_charaters():

    value = input('Enter an integer: ')
    print('{:<15}{:<15}'.format('Integer', 'Digit sum'))
    total = 0
    for s in str(value):
        total += int(s)
    print('{:<15}{:<15}'.format(value, total))

if __name__ =='__main__':

    sum_charaters()