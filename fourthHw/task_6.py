from itertools import count, cycle
def generator(start = 0):
    gen_list = []
    for el in count(start):
        if el > start + 10:
            break
        gen_list.append(el)
    return gen_list

def repeat(gen_list = generator(), stop = 32):
    re_gen_list = []
    gen_list = cycle(gen_list)
    for el in gen_list:
        if len(re_gen_list) > stop:
            break
        re_gen_list.append(el)
    return re_gen_list

print(repeat(generator()))
