str_for_code = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def shift_encode(string):
    global str_for_code
    encoded_str = ''
    for i in string:
        if str_for_code.index(i) == len(str_for_code) - 1:
            encoded_str += str_for_code[0]
        else:
            encoded_str += str_for_code[str_for_code.index(i) + 1]
    return encoded_str


def shift_decode(string):
    global str_for_code
    decoded_str = ''
    for i in string:
        if str_for_code.index(i) == 0:
            decoded_str += str_for_code[len(str_for_code) - 1]
        else:
            decoded_str += str_for_code[str_for_code.index(i) - 1]
    return decoded_str


print(shift_encode('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))
