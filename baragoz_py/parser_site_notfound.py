from collections import Counter  # Преобразует список в словарь подсчитывая уникальные элементы


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res

    return wrapper


@benchmark
def nah(dat):
    # dat = input("Введите дату отбора вида ММ за 2017г: ")  # получаем дату отбора
    # dat = str(dat) + ".2017"
    otbor = []  # список отобранного за месяц
    with open("notfound.txt", "r") as f:  # открываем файл ненайденного с сайта
        for line in f:  # читаем построчно
            if dat in line:  # если дата содержится в строке лога:
                otbor.append(line[20:])  # добавляем ее в список исключая первые 20 символов(это дата и время)
    otbor = [line.rstrip() for line in otbor]  # удаляем '\n' из всех эелементов инче зашкварит csv
    schet = Counter(otbor)  # FUCKING MAGIC!!! получаем словарь где ключ - элемент, а значение - кол-во повторов
    out = list(schet.items())  # обратная сортировака по значению
    out.sort(key=lambda item: item[1], reverse=True)  # обратная сортировака по значению
    with open("NotFound_" + dat + ".csv", "w") as f:  # Сохраняем в файл
        for line in out:
            f.write(line[0] + ';' + str(line[1]) + '\n')

nah("05.2017")