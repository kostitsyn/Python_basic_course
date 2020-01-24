def int_func_one(text):
    """Возвращает строку со слововом с первой прописной буквы."""
    return text.title()


def int_func_two(text):
    """Возвращает строку со словами с первыми прописными буквами, оставляя другие в исходном регистре (задание со *)."""
    orig_list_text = text.split()
    result_list = []
    for i in orig_list_text:
        if i[0].islower():
            word_list = list(i)
            up_sym = (word_list.pop(0)).upper()
            word_list.insert(0, up_sym)
            i = ''.join(word_list)
        result_list.append(i)
        result_str = ' '.join(result_list)
    return result_str


print(int_func_one(input('Введите слово, состоящее из латинских строчных букв: ')))
print(int_func_two(input('Введите строку из слов состоящих из букв разного регистра, разделенных пробелом: ')))
