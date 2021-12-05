def show_user_data (user_dict):
    """[show_user_data]

    Args:
        user_dict ([dict]): [a dictionary with information entered by the user]

    Returns:
        [str]: [variable with a string containing all information from the dictionary]
    """
    user_info = ''

    for key in user_dict:
        user_info += user_dict[key]
        # looks better f'{user_dict[key]}\n'

    return user_info

user_data = {
    'name': input('Enter your name: '),
    'surname': input('Enter your surname: '),
    'year_of_birth': input('Enter your year of birth: '),
    'city_of_residence': input('Enter your city of residence: '),
    'email': input('Enter your email address: '),
    'phone': input('Enter your phone number: '),

}

print(show_user_data(user_dict = user_data))
