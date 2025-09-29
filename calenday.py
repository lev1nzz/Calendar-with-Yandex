'''
Its calendar docstring test
'''

year = 2030

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


def is_leap_year(year):
    if year % 4 != 0:
        is_leap = False
    else:
        is_leap = True

    if year % 100 == 0:
        is_leap = False
    if year % 400 == 0:
        is_leap = True
    return is_leap


def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:
        duration = 30
    elif month_index == 1:
        duration = 29 if is_leap_year(year_value) else 28
    else:
        duration = 31
    return duration


def print_days(days_in_month, start_day):
    space = '   ' * start_day
    print(space, end='')
    for day in range(1, days_in_month + 1):
        if day < 10:
            print(day, end='  ')
        else:
            print(day, end=' ')
        if (day + start_day) % 7 == 0:
            print()
    if (days_in_month + start_day) % 7 != 0:
        print()
    

def get_starting_day(year):
    d = 1
    m = 13
    y = year - 1
    h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7          


def abjust_start_day(start_day, days_in_month):
    results = (start_day + days_in_month) % 7 
    return results


def print_header(year_value, month_index):
    print(months[month_index], year_value)
    print('Пн Вт Ср Чт Пт Сб Вс')  


def print_calendar(year):
    start_day = get_starting_day(year)
    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration(year, month_number)
        print_days(duration, start_day)
        start_day = abjust_start_day(start_day, duration)
        print()
        
        
print_calendar(year)