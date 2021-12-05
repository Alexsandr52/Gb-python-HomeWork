def sum_in_list(user_list):
    return sum(user_list)
    
sum_elem = 0
s_examination = True
while s_examination:
    user_input = input('Enter numbers thru the spase or "S" to stop: ').split()
    
    if 'S' in user_input:
        del user_input[user_input.index('S'):]
        s_examination = False

    user_input = list(map(float,user_input))
    sum_elem += sum_in_list(user_input)

print(sum_elem)
