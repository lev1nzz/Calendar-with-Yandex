from tkinter import *

from calenday import Calendar

import io
import sys

def get_calendar():
    try:
        year = int(user_input.get())
        current_calendar = Calendar(year)
        
        # Перехватываем вывод print в буфер
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        # Вызываем метод печати календаря (вывод идет в buffer)
        current_calendar.print_calendar(year)
        
        # Возвращаем стандартный вывод
        sys.stdout = old_stdout
        
        # Получаем текст из буфера
        calendar_text = buffer.getvalue()
        
        # Выводим в текстовое поле
        text_area.delete(1.0, END)
        text_area.insert(1.0, calendar_text)
        
    except ValueError:
        text_area.delete(1.0, END)
        text_area.insert(1.0, "Ошибка: введите корректный год")

# Создаем окно
root = Tk()
root.title("Календарь")

# Поле для ввода года
Label(root, text="Введите год:").pack(pady=5)
user_input = StringVar()
entry = Entry(root, textvariable=user_input, width=20)
entry.pack(pady=5)

# Кнопка для отображения календаря
Button(root, text="Показать календарь", command=get_calendar).pack(pady=5)

# Текстовое поле для вывода календаря
text_area = Text(root, width=50, height=25, font=("Courier", 9))
text_area.pack(pady=10, padx=10)

# Добавляем прокрутку
scrollbar = Scrollbar(root, command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

root.mainloop()