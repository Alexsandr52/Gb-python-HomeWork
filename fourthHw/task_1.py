from sys import argv
def payroll_preparation(argv_list):
    return argv_list[0] * argv_list[1] + argv_list[2]

argv_list = list(map(float, argv[1:].copy()))
print(payroll_preparation(argv_list))
