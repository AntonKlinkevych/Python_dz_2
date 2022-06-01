def convert_to_preferred_format(sec):
    day = sec // 86400
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print("Дней:",day)
    print("Часов:",hour)
    print("Минут:",min)
    print("Секунд:",sec)
    return "%02d:%02d:%02d:%02d" % (day, hour, min, sec)

num = int(input("Введите количество секунд:"))
print("Время в формате Unix  -",convert_to_preferred_format(num))





