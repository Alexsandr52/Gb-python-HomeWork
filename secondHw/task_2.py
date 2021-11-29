user_list_input = input('Enter elements separated by a space: ')
active_list = list(user_list_input.split())
index = 0

while index < len(active_list):
    if index % 2 == 0:
        active_list[index], active_list[index + 1] = active_list[index + 1], active_list[index]
    else:
        index += 1
        continue
    index += 1

print(active_list)