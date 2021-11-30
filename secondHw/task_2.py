active_list = input('Enter elements separated by a space: ').split()
index = 0

while index < len(active_list):
    if active_list[index] == active_list[-1] and index > 0: break

    active_list[index], active_list[index + 1] = active_list[index + 1], active_list[index]
    index += 2

print(active_list)
