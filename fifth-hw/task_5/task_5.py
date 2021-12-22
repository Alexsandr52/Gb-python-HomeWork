examples = '1 2 3 4 5 6 7 8'
with open('fifth-hw/task_5/task_5.txt', 'w') as file:
    file.writelines(examples)

with open('fifth-hw/task_5/task_5.txt', 'r') as file:
    nums = file.read()
    nums = list(map(int, nums.split()))
    print(sum(nums))
