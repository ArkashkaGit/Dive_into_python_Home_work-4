# 2. Напишите функцию:
# * принимающую на вход только ключевые параметры и возвращающую словарь,
# * где ключ — значение переданного аргумента,
# * значение — имя аргумента. Если ключ не хешируем,
# * используйте его строковое представление.

def hashable_dicts(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict


print(hashable_dicts(students=["Jon", "Sara"], \
                     three_frends={1: "Boris", 2: "Gurgen", 3: "Bob"}))