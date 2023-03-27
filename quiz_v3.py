def median_num():

    line = input('Input list: ')
    nums = []
    for s in line.split(' '):
        if s == '' or s == ' ':
            continue
        nums.append(int(s))
    nums.sort()
    n = len(nums)
    i = n // 2
    if n % 2 == 0:
        median = 0.5 * (nums[i-1] + nums[i])
    else:
        median = nums[i]
    print('Median: {:.1f}'.format(median))

if __name__ =='__main__':

    median_num()