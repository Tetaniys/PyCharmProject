import os


def build_note(note_text: str, note_name: str):  # создание файла
    try:
        file_path = f"{note_name}.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(note_text)
    except:
        print('произолшла ошибка при создании файла')


def create_note():  # создание заметки
    try:
        note_name = input("Введите название заметки: ")
        note_text = input("Введите текст заметки: ")
        build_note(note_text, note_name)
    except:
        print('произолшла ошибка при создании заметки')


def read_note():  # вывод заметки
    try:
        note_name = input("Введите название заметки: ")
        file_path = f"{note_name}.txt"
        # Проверяем существование файла
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"Содержимое заметки '{note_name}':\n{content}")
        else:
            print(f"Заметка '{note_name}' не найдена.")
    except:
        print('произошла ошибка при выводе заметки')


def edit_note():  # редактор  заметки
    try:
        note_name = input("Введите название заметки: ")
        file_path = f"{note_name}.txt"

        if os.path.exists(file_path):
            # Открываем и читаем содержимое файла
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print("\nТекущее содержимое заметки:")
                print(content)

            # Запрашиваем новый текст
            new_content = input("\nВведите новый текст заметки: ")

            # Перезаписываем файл новым содержимым
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print("Заметка обновлена.")
        else:
            print("Заметка не найдена.")
    except:
        print('произошла ошибка ппри редактировании зззаметки')


def delete_note():
    try:
        note_name = input("Введите название заметки: ")
        file_path = f"{note_name}.txt"

        if os.path.exists(file_path):
            os.remove(file_path)
            print('Заметка удалена')
        else:
            print('заметка не найдена')
    except:
        print('Произошла ошибка при удалении зааметки')


def main():
    try:
        print('Выберете варианты действия числом')
        print('')
        print('1. Создать заметку')
        print('2. Прочитать заметку')
        print('3. Удалить заметку')
        print('4. Редактировать заметку')
        print('5. Отсорттировать заметку по длине текста')
        print('6. Выход')

        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            create_note()
        elif choice == '2':
            read_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            display_sorted_notes()
        elif choice == '6':
            print("Выход из программы.")
            return
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")
    except:
        print('Произошла ошибка в меню')


def display_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]

        if not notes:
            print('Нет доступных заметок')
            return
        # Сортируем по размеру файла
        notes.sort(key=lambda filename: os.path.getsize(filename))

        print("\nСписок заметок (от самых коротких к самым длинным):")
        for note in notes:
            print(f"- {note}")
    except:
        print('Произошла ошибка при выводе заметок')


def read_note_content(note_name):
    try:
        """Читает содержимое заметки"""
        with open(note_name, 'r', encoding='utf-8') as f:
            content = f.read()
        return content.strip()
    except:
        print('Произошла ошибка при чтении заметки')


def display_sorted_notes():
    try:
        notes = []  # Список пар ('название_заметки', длина_текста)

        # Собираем все заметки (*.txt) и измеряем длину их содержимого
        for file in os.listdir():
            if file.endswith('.txt'):
                content_length = len(read_note_content(file))
                notes.append((file, content_length))

        # Сортируем заметки по длине текста в обратном порядке (от большей к меньшей)
        sorted_notes = sorted(notes, key=lambda x: x[1], reverse=True)

        # Печатаем результат
        print("\nЗаметки от самой длинной к самой короткой:")
        for note, length in sorted_notes:
            print(f"{note}: {length} символов")
    except:
        print('Произошла ошибка ппри сортировки заметок')
