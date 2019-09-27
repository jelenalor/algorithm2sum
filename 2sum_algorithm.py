""" Load data """
with open(r"text.txt", "r") as f:
    data = f.readlines()
list_of_nums = [int(i) for i in data]

""" Step 1 - Sort the list of numbers"""
list_of_nums = sorted(list_of_nums)
""" i -> first index of the list, j -> last index of the list"""
i = 0
j = len(list_of_nums) - 1
""" Lower and upper bonds of 'sums' we are trying to find"""
lower = -10000
upper = 10000
""" Collect all sums that satisfy the above lower and upper bounds into 'collections' list"""
collection = set([])
""" While will work only when i not equal to j, therefore will iterate over 1/2 of the list of numbers """
while i != j:
    sum_ = list_of_nums[i] + list_of_nums[j]
    if sum_ < lower:
        i += 1
    elif sum_ > upper:
        j -= 1
    else:
        for k in range(i, j + 1)[::-1]:
            sum_a = list_of_nums[i] + list_of_nums[k]
            if sum_a < lower:
                break
            else:
                if list_of_nums[i] != list_of_nums[k] and sum_a not in collection:
                    collection.add(sum_a)
        i += 1
"""The result shows how many numbers from the range between -10k to 10k
 can be achieved by summing two numbers from our list_of_nums"""
print(len(collection))