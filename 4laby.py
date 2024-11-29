# Завдання 1-10: Розробка ASCII ART генератора для візуалізації 2D-фігур

def print_menu():
    print("\n--- ASCII Art Generator ---")
    print("1. Створити новий ASCII-арт")
    print("2. Вийти")

def get_user_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print("Невірний вибір. Спробуйте ще раз.")

def get_ascii_symbols():
    # Завдання 2: Набір символів
    return ['@', '#', '*', '=', '-', ':', '.', ' ']

def get_canvas_size():
    # Завдання 3: Розміри Art-у
    width = int(input("Введіть ширину ASCII-арту (10-100): "))
    height = int(input("Введіть висоту ASCII-арту (5-50): "))
    width = max(10, min(width, 100))
    height = max(5, min(height, 50))
    return width, height

def align_text(ascii_art, width, align):
    # Завдання 5: Вирівнювання тексту
    aligned_art = []
    for line in ascii_art:
        if align == "центр":
            aligned_art.append(line.center(width))
        elif align == "право":
            aligned_art.append(line.rjust(width))
        else:
            aligned_art.append(line.ljust(width))
    return aligned_art

def generate_ascii_art(user_text, width, height, symbols, align="ліво"):
    # Завдання 4: Функція генерації Art-у
    ascii_art = []
    symbol_count = len(symbols)
    for y in range(height):
        line = []
        for x in range(width):
            char_index = (x + y) % len(user_text) % symbol_count
            line.append(symbols[char_index])
        ascii_art.append("".join(line))
    return align_text(ascii_art, width, align)

def display_ascii_art(ascii_art):
    # Завдання 6: Відображення мистецтва
    for line in ascii_art:
        print(line)

def save_ascii_art(ascii_art, filename):
    # Завдання 7: Збереження у файл
    with open(filename, "w") as file:
        for line in ascii_art:
            file.write(line + "\n")
    print(f"ASCII-арт збережено у файл {filename}")

def main():
    while True:
        print_menu()
        choice = get_user_choice("Виберіть опцію (1-2): ", ['1', '2'])
        
        if choice == '2':
            print("Дякуємо за використання ASCII Art Generator!")
            break

        # Завдання 1: Введення користувача
        user_text = input("Введіть текст для ASCII-арту: ")
        symbols = get_ascii_symbols()
        
        # Завдання 3: Розміри Art-у
        width, height = get_canvas_size()
        
        # Завдання 5: Вирівнювання тексту
        align_choice = get_user_choice("Виберіть вирівнювання (ліво, центр, право): ", ['ліво', 'центр', 'право'])
        
        # Завдання 4: Генерація ASCII-арту
        ascii_art = generate_ascii_art(user_text, width, height, symbols, align=align_choice)
        
        # Завдання 9: Функція попереднього перегляду
        preview_choice = get_user_choice("Бажаєте переглянути попередній перегляд ASCII-арту? (так/ні): ", ['так', 'ні'])
        if preview_choice == 'так':
            display_ascii_art(ascii_art)
        
        # Завдання 7: Збереження у файл
        save_choice = get_user_choice("Бажаєте зберегти ASCII-арт у файл? (так/ні): ", ['так', 'ні'])
        if save_choice == 'так':
            filename = input("Введіть ім'я файлу для збереження: ")
            save_ascii_art(ascii_art, filename)

if __name__ == "__main__":
    main()
