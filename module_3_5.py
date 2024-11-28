def get_multiplied_digits(numbers):
    str_num = str(numbers)
    first = int(str_num[0])
    if len(str_num) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_num[1:]))

print(get_multiplied_digits(908005))
