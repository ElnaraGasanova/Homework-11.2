def str_upper(data: str):

    """Функция возвращает строку со
    всеми заглавными буквами"""

    data_up = data.upper()
    return data_up


if __name__ == "__main__":
    print(str_upper("заглавные все буквы"))

def str_title(data: str):

    """Функция возвращает заглавными
    первые буквы каждого слова в строке"""

    data_tit = data.title()
    return data_tit


if __name__ == "__main__":

    print(str_title("заглавные первые буквы"))