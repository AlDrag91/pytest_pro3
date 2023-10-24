def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. в ином случае возвращает значение default.
    :param collection: Словарь исходный.
    :param key: ключ.
    :param default: значение по-умолчанию.
    :return: Значение из словаря или значение default
    """

    if collection == {}:
        return default

    if collection[key] == collection[key]:
        return collection[key]




