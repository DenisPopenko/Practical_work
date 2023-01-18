import random
def change(nums):
    lst = list(nums)
    index = random.randint(0, 4)
    print(index)
    print(nums[index])
    value = random.randint(100, 1000)
    lst[index] = value
    nums = tuple(lst)
    return nums, value

my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums_2, rand_val_2 = change(new_nums)
rand_val += rand_val_2
print(new_nums_2, rand_val)