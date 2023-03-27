def reverse(nums, i, j):

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums

def rotate_array(nums, k):
    
    nums = nums.split()
    size = len(nums)
    if size < 1:
        return []
    if k < 0:
        k = size + k
    for i in range(size):
        nums[i] = int(nums[i])
    k = size - k
    nums = reverse(nums, 0, k-1)
    nums = reverse(nums, k, size-1)
    nums = reverse(nums, 0, size-1)
    return nums

if __name__ == '__main__':

    nums = input('Input list: ')
    k = int(input('Input k: '))
    nums = rotate_array(nums, k)
    print('Rotated list: ', end='')
    print(nums)