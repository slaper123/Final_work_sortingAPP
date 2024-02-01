# Итоговый проект.

# Реализовать графическую программу с использованием библиотеки Tkinter, которая состоит из поля ввода текста,
# раскрывающегося списка и полем вывода надписи и кнопки.

# Логика работы программы:

# 1. Пользователь вводит последовательность чисел через запятую
# 2. Выбирает один из вариантов сортировки
# 3. После нажатия на кнопку Start происходит сортировка последовательности с последующим выводом в текстовое поле вывода
# 4. Реализовать вывод времени затраченного на сортировку

# Код должен содержать комментарии, а также все необходимые проверки на исключения.
# Код должен быть максимально читаем. При написании следует прибегнуть к стандартным библиотекам тестирования!

# Ссылка на GitHub https://github.com/slaper123/Final_work_sortingAPP.git

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import timeit
import unittest
from unittest.mock import patch

class SortingApp:
    def __init__(self, root=None):
        # Инициализация объекта графического приложения.
        if root is None:
            root = tk.Tk()

        self.root = root
        self.root.title('Sorting App')

        # Переменные
        self.input_sequence = tk.StringVar()
        self.selected_sorting = tk.StringVar()
        self.sorting_algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']

        # Создание виджетов интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Создание элементов интерфейса.


        # Label для ввода текста
        input_label = tk.Label(self.root, text='Введите последовательность чисел (через запятую):')
        input_label.pack(pady=5)

        # Entry для ввода текста, связано с переменной input_sequence
        input_entry = tk.Entry(self.root, textvariable=self.input_sequence)
        input_entry.pack(pady=5)

        # Label для выбора алгоритма сортировки
        sorting_label = tk.Label(self.root, text='Выберите алгоритм сортировки:')
        sorting_label.pack(pady=5)

        # Combobox для выбора алгоритма сортировки, связан с переменной selected_sorting
        sorting_combobox = ttk.Combobox(self.root, textvariable=self.selected_sorting, values=self.sorting_algorithms)
        sorting_combobox.pack(pady=5)

        # Кнопка для запуска сортировки, при нажатии вызывает метод sort_sequence
        start_button = tk.Button(self.root, text='Start', command=self.sort_sequence)
        start_button.pack(pady=10)

        # Label для вывода текста с информацией о содержимом поля вывода
        output_label = tk.Label(self.root, text='Отсортированная последовательность:')
        output_label.pack(pady=5)

        # Text для вывода отсортированной последовательности и времени сортировки
        self.output_text = tk.Text(self.root, height=5, width=40)
        self.output_text.pack(pady=5)

    def sort_sequence(self):
        # Обработка нажатия кнопки Start.

        sequence_str = self.input_sequence.get()    # Получение введенной последовательности

        try:
            # Преобразование строки в список чисел
            sequence = [int(num.strip()) for num in sequence_str.split(',')]
        except ValueError:
            # В случае ошибки (например, ввод нечисловых данных), показывает сообщение об ошибке
            # и завершает выполнение функции.
            messagebox.showerror('Ошибка', 'Введите корректную последовательность чисел.')
            return

        # Выбор алгоритма сортировки
        # Получение выбранного пользователем алгоритма сортировки из выпадающего списка
        selected_algorithm = self.selected_sorting.get()

        # Получение соответствующей функции сортировки по выбранному алгоритму
        sorting_function = self.get_sorting_function(selected_algorithm)

        # Проверка, что функция сортировки была успешно получена
        if sorting_function is None:
            # Если функция не была получена (например, если алгоритм не выбран),
            # выводится сообщение об ошибке и завершается выполнение функции.
            messagebox.showerror('Ошибка', 'Выберите алгоритм сортировки.')
            return

        # Замер времени выполнения сортировки с использованием модуля timeit
        # Время замеряется с использованием анонимной функции (lambda), чтобы избежать передачи изменяемых объектов
        # и сохранить исходную последовательность для дальнейшего сравнения.
        elapsed_time = timeit.timeit(lambda: sorting_function(sequence.copy()), number=1)

        # Получение отсортированной последовательности с использованием выбранного алгоритма сортировки
        sorted_sequence = sorting_function(sequence)

        # Вывод отсортированной последовательности и времени затраченного на сортировку в текстовое поле
        self.output_text.delete(1.0, tk.END)    # Очистка текстового поля перед выводом
        self.output_text.insert(tk.END, ', '.join(map(str, sorted_sequence))) #Вывод отсортированной последовательности
        self.output_text.insert(tk.END, f'\n\nВремя сортировки: {elapsed_time:.6f} секунд') # Вывод времени сортировки

    def get_sorting_function(self, algorithm):
        # Получение функции сортировки по выбранному алгоритму

        if algorithm == 'Bubble Sort':
            return self.bubble_sort
        elif algorithm == 'Selection Sort':
            return self.selection_sort
        elif algorithm == 'Insertion Sort':
            return self.insertion_sort
        else:
            return None

    @staticmethod
    def bubble_sort(sequence):
        # Алгоритм сортировки пузырьком
        n = len(sequence)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if sequence[j] > sequence[j + 1]:
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
        return sequence

    @staticmethod
    def selection_sort(sequence):
        # Алгоритм сортировки выбором
        n = len(sequence)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if sequence[j] < sequence[min_index]:
                    min_index = j
            sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
        return sequence

    @staticmethod
    def insertion_sort(sequence):
        # Алгоритм сортировки вставкой
        for i in range(1, len(sequence)):
            key = sequence[i]
            j = i - 1
            while j >= 0 and key < sequence[j]:
                sequence[j + 1] = sequence[j]
                j -= 1
            sequence[j + 1] = key
        return sequence


    def run_sorting_app(self):
        self.root = tk.Tk()
        self.app = SortingApp(self.root)
        self.root.mainloop()

class TestSortingApp(unittest.TestCase):
    def test_bubble_sort(self):
        """
            Тест проверяет тест:
            - Правильность работы алгоритма сортировки пузырьком.
            - Соответствие отсортированной последовательности ожидаемой (с использованием встроенной функции sorted).
            """
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]        # Создание тестируемой последовательности
        sorted_sequence = SortingApp.bubble_sort(sequence)  # Вызов тестируемого метода bubble_sort

        # Проверка, что отсортированная последовательность совпадает с ожидаемой
        self.assertEqual(sorted_sequence, sorted(sequence))

    def test_selection_sort(self):
        """
           Тест проверяет :
           - Правильность работы алгоритма сортировки выбором.
           - Соответствие отсортированной последовательности ожидаемой (с использованием встроенной функции sorted).
           """
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]            # Создание тестируемой последовательности
        sorted_sequence = SortingApp.selection_sort(sequence)   # Вызов тестируемого метода selection_sort

        # Проверка, что отсортированная последовательность совпадает с ожидаемой
        self.assertEqual(sorted_sequence, sorted(sequence))

    def test_insertion_sort(self):
        """
           Тест проверяет :
           - Правильность работы алгоритма сортировки вставкой.
           - Соответствие отсортированной последовательности ожидаемой (с использованием встроенной функции sorted).
           """
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]            # Создание тестируемой последовательности
        sorted_sequence = SortingApp.insertion_sort(sequence)   # Вызов тестируемого метода insertion_sort

        # Проверка, что отсортированная последовательность совпадает с ожидаемой
        self.assertEqual(sorted_sequence, sorted(sequence))

    def test_sort_sequence_with_valid_input(self):
        """
        Тест проверяет корректность работы приложения при правильном вводе.
        После сортировки ожидается, что выводится отсортированная последовательность чисел,
        и в поле вывода также присутствует информация о времени, затраченном на сортировку.
        """

        app = SortingApp(None)                                    # Создание экземпляра приложения SortingApp
        app.input_sequence.set('3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5') # Установка валидной корректной чисел в поле ввода
        app.selected_sorting.set('Bubble Sort') # Установка выбранного алгоритма сортировки - "Bubble Sort"
        app.sort_sequence()                     # Вызов метода sort_sequence

        # Проверка, что текст в поле вывода соответствует ожидаемому регулярному выражению
        self.assertRegex(app.output_text.get("1.0", tk.END), r'^\d+(, \d+)*\n\nВремя сортировки: \d+\.\d+ секунд$')

    def test_sort_sequence_with_invalid_input(self):
        """
        Этот тест проверяет, что приложение корректно обрабатывает ситуацию с некорректным вводом
        """

        app = SortingApp(None)                      # Создание экземпляра приложения SortingApp
        app.input_sequence.set('invalid_sequence')  # Установка невалидной последовательности в поле ввода

        # Перед вызовом sort_sequence убедимся, что messagebox.showerror был вызван
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            app.sort_sequence()                     # Вызов метода sort_sequence с невалидным вводом
            mock_showerror.assert_called_once()     # Проверка, что метод showerror был вызван один раз

    def test_sort_sequence_with_no_algorithm_selected(self):
        """
        Этот тест проверяет, что если пользователь пытается запустить сортировку без выбора алгоритма,
        приложение корректно выводит сообщение об ошибке. В этом случае, ожидается вызов messagebox.showerror.
        """

        app = SortingApp(None)                                      # Создание объекта приложения
        app.input_sequence.set('3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5')   # Установка вводной последовательности

        # Перед вызовом sort_sequence убеждаемся, что messagebox.showerror был вызван
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            app.sort_sequence()                         # Вызов метода sort_sequence
            mock_showerror.assert_called_once()         # Проверка вызова messagebox.showerror

if __name__ == '__main__':
    unittest.main()