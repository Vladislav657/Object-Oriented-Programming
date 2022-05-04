alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]


def check_pin(pin):
    return len(pin) == 4 and pin.count(pin[0]) != 4 and pin != '1234'


def check_pass(password):
    return len(password) >= 8 and any(map(str.isdigit, password)) and any(map(str.isalpha, password))


def check_mail(mail):
    return '@' in mail and '.' in mail


def check_name(name):
    global alphabet
    for i in name:
        if i not in alphabet:
            return False
    return True
