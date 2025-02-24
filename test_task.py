def list_handling(lst):
    '''
    Обработка списка чисел:
    1. Удаление дублирующихся значений
    2. Удаление всех нечётных значений
    3. Сортирует значения по убыванию

    :param lst: список чисел
    :return: list
    '''

    # удаляем дубликаты через преобразование ко множеству
    set_lst = set(lst)

    #оставляем только четные числа
    lst_chet = list(filter(lambda x: x % 2 == 0, set_lst))

    #сортируем по убыванию
    res = sorted(lst_chet,reverse=True)
    return res



def list_handling_long(lst):
    '''
    Та же самая функция, что и list_handling, но без использования встроенных функций
    
    Обработка списка чисел:
    1. Удаление дублирующихся значений
    2. Удаление всех нечётных значений
    3. Сортирует значения по убыванию

    :param lst: список чисел
    :return: list
    '''

    #удаляем из списка дублирующиеся и нечетные элементы
    res = []
    for value in lst:
        if value not in res:
            if value % 2 == 0:
               res.append(value)

    #сортируем получившийся список
    for i in range(len(res)-1):
        for j in range(len(res)-1-i):
            if res[j] < res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]

    return res



def check_palindrome(text):
    '''
    Проверяет введенную строку, является ли она палиндромом (то есть, читается ли
    в обратном порядке так же, как в прямом).

    :param text: Строка, которую необходимо проверить
    :return: bool
    '''

    if type(text) != str:
        raise TypeError("Проверяемый текст должен быть строкой")
    return text.lower() == text.lower()[::-1]
