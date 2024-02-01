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

class SortingApp:
    def __init__(self, root):
        """
        Инициализация объекта графического приложения.

        Parameters:
        - root: Объект Tkinter Tk, корневое окно приложения.
        """
        self.root = root                            # Присвоение переданного корневого окна объекту приложения
        self.root.title('Sorting App')              # Установка заголовка главного окна приложения

        # Переменные для хранения данных в приложении
        self.input_sequence = tk.StringVar()        # Строковая переменная для ввода последовательности чисел
        self.selected_sorting = tk.StringVar()      # Строковая переменная для выбранного алгоритма сортировки
        self.sorting_algorithms = ['Bubble Sort',
                                   'Selection Sort',
                                   'Insertion Sort']    # Список доступных алгоритмов сортировки
        self.create_widgets()                           # Создание виджетов интерфейса

    def create_widgets(self):
        """
            Создание элементов интерфейса.

            - Создает поле ввода текста с меткой для последовательности чисел.
            - Создает раскрывающийся список для выбора алгоритма сортировки.
            - Создает кнопку "Start" для запуска сортировки.
            - Создает поле вывода текста для отображения отсортированной последовательности и времени сортировки.
            """

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
        """
        Обработка нажатия кнопки Start.

        - Получает введенную последовательность из текстового поля ввода.
        - Преобразует строку в список чисел, обрабатывая возможные ошибки.
        - Выбирает функцию сортировки в соответствии с выбранным алгоритмом.
        - Замеряет время выполнения сортировки с использованием timeit.
        - Выводит отсортированную последовательность и время сортировки в текстовое поле вывода.
        """

        sequence_str = self.input_sequence.get()                                # Получение введенной последовательности
        try:
            sequence = [int(num.strip()) for num in sequence_str.split(',')]    # Преобразование строки в список чисел
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
        """
        Возвращает соответствующую функцию сортировки для выбранного алгоритма.

        Parameters:
        - algorithm: Строка с названием выбранного алгоритма сортировки.

        Returns:
        - Функция сортировки для выбранного алгоритма или None, если алгоритм не распознан.
        """
        if algorithm == 'Bubble Sort':
            return self.bubble_sort             # Возвращает функцию сортировки пузырьком
        elif algorithm == 'Selection Sort':
            return self.selection_sort          # Возвращает функцию сортировки выбором
        elif algorithm == 'Insertion Sort':
            return self.insertion_sort          # Возвращает функцию сортировки вставкой
        else:
            return None                         # Возвращает None, если алгоритм не распознан

    @staticmethod
    def bubble_sort(sequence):
        """
        Реализация алгоритма сортировки пузырьком.

        Parameters:
        - sequence: Список, который нужно отсортировать.

        Returns:
        - Отсортированный список.

        Алгоритм:
        1. Проходим по всем элементам списка, начиная с первого.
        2. Для каждого элемента сравниваем его со следующим элементом.
        3. Если текущий элемент больше следующего, меняем их местами.
        4. После первого прохода на последнем месте оказывается наибольший элемент.
        5. Повторяем шаги 1-4 для оставшихся элементов, исключая уже отсортированные.
        """
        n = len(sequence)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Сравниваем соседние элементы и меняем их местами, если необходимо
                if sequence[j] > sequence[j + 1]:
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
        return sequence

    @staticmethod
    def selection_sort(sequence):
        """
        Реализация алгоритма сортировки выбором.

        Parameters:
        - sequence: Список, который нужно отсортировать.

        Returns:
        - Отсортированный список.

        Алгоритм:
        1. Проходим по всем элементам списка.
        2. Для каждого элемента находим минимальный элемент среди оставшихся.
        3. Меняем местами текущий элемент с найденным минимальным элементом.
        4. Повторяем шаги 1-3 для каждого элемента.
        """
        n = len(sequence)
        for i in range(n):
            min_index = i
            # Поиск минимального элемента в оставшейся части списка
            for j in range(i + 1, n):
                if sequence[j] < sequence[min_index]:
                    min_index = j
            sequence[i], sequence[min_index] = sequence[min_index], sequence[i] # Обмен текущего элемента с минимальным
        return sequence

    @staticmethod
    def insertion_sort(sequence):
        """
        Реализация алгоритма сортировки вставкой.

        Parameters:
        - sequence: Список, который нужно отсортировать.

        Returns:
        - Отсортированный список.

        Алгоритм:
        1. Проходим по элементам списка, начиная со второго.
        2. На каждом шаге берем текущий элемент и вставляем его на правильное место
           среди уже отсортированной части списка слева.
        3. Повторяем шаг 2 для всех элементов.
        """
        for i in range(1, len(sequence)):
            key = sequence[i]
            j = i - 1
            # Поиск места для вставки текущего элемента
            while j >= 0 and key < sequence[j]:
                sequence[j + 1] = sequence[j]
                j -= 1
            sequence[j + 1] = key           # Вставка текущего элемента на найденное место
        return sequence

if __name__ == '__main__':
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()