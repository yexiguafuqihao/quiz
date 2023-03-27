def time_converter():

    value = int(input('Number of seconds: '))
    if value < 1:
        print('{} second = {} second'.format(value, value))
        return
    d = value // 86400
    h = (value % 86400) // 3600
    m = (value % 86400 % 3600) // 60
    s = (value % 86400 % 3600) % 60

    line = ' '
    if d > 1:
        line += '{} days '.format(d)
    elif 0 < d < 2:
        line += '{} day '.format(d)
    if h > 1:
        line += '{} hours '.format(h)
    elif 0 < h < 2:
        line += '{} hour '.format(h)
    
    if m > 1:
        line += '{} minutes '.format(m)
    elif 0 < m < 2:
        line += '{} minute '.format(m)
    if s > 1:
        line += '{} seconds '.format(s)
    elif 0 < s < 2:
        line += '{} second '.format(s)
    
    line = '{} seconds ='.format(value) + line[:-1]
    print(line)
    
    
if __name__ =='__main__':

    time_converter()
