import random
def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)

nums_list = [1, 2, 3]
nums_list_copy = nums_list[:]
some_dict = {1: 'text', 2: 'another text'}
some_dict_copy = some_dict.copy()
uniq_nums = {1, 2, 3}
uniq_nums_copy = uniq_nums.copy()
common_dict = {1: nums_list_copy, 2: some_dict_copy, 3: uniq_nums_copy, 4: (10, 20, 30)}
change_dict(common_dict)
print(common_dict)
print(nums_list)
print(some_dict)
print(uniq_nums)