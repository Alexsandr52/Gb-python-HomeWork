def division(num_1, num_2):
    """[division]

    Args:
        num_1 ([float]): [Gets the numerator]
        num_2 ([float]): [Gets the denominator]

    Returns:
        [float]: [returns the quotient of arguments]
    """
    if num_2 == 0:
        return 'Can\'t divide by zero'
    
    return round(num_1 / num_2, 4)

user_input = input('Enter tow numbers with spaces: ').split()
user_input = list(map(float, user_input))

print(division(user_input[0], user_input[1]))