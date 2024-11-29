import math

class AsciiArt3DGenerator:
    def __init__(self):
        self.objects = []
        self.width = 50
        self.height = 25

    def add_object(self, obj):
        """Додає 3D-фігуру до сцени."""
        self.objects.append(obj)

    def render(self):
        """Здійснює проекцію всіх об’єктів сцени в 2D і відображає ASCII-арт."""
        canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for obj in self.objects:
            obj.project_to_2d(canvas)
        self.display(canvas)

    def display(self, canvas):
        """Відображає згенерований ASCII-арт."""
        for row in canvas:
            print("".join(row))

    def save_to_file(self, filename):
        """Зберігає ASCII-арт у файл."""
        with open(filename, "w") as file:
            for row in canvas:
                file.write("".join(row) + "\n")
        print(f"ASCII-арт збережено у файл {filename}")

class Cube:
    def __init__(self, size, symbol='#'):
        self.size = size
        self.symbol = symbol

    def project_to_2d(self, canvas):
        """Перетворює 3D-куб у 2D-ASCII-арт шляхом проекції."""
        # Розміщення "куба" як спрощеного прямокутника в 2D.
        center_x, center_y = len(canvas[0]) // 2, len(canvas) // 2
        for i in range(self.size):
            for j in range(self.size):
                x = center_x + i
                y = center_y + j - i // 2  # зміщення для видимості в перспективі
                if 0 <= x < len(canvas[0]) and 0 <= y < len(canvas):
                    canvas[y][x] = self.symbol

class Sphere:
    def __init__(self, radius, symbol='@'):
        self.radius = radius
        self.symbol = symbol

    def project_to_2d(self, canvas):
        """Проектує сферу в 2D-простір, використовуючи кругові рівняння."""
        center_x, center_y = len(canvas[0]) // 2, len(canvas) // 2
        for y in range(-self.radius, self.radius):
            for x in range(-self.radius, self.radius):
                if x**2 + y**2 <= self.radius**2:
                    px = center_x + x
                    py = center_y + y
                    if 0 <= px < len(canvas[0]) and 0 <= py < len(canvas):
                        canvas[py][px] = self.symbol

def main():
    generator = AsciiArt3DGenerator()
    while True:
        print("\n--- ASCII 3D Art Generator ---")
        print("1. Додати куб")
        print("2. Додати сферу")
        print("3. Показати арт")
        print("4. Зберегти арт")
        print("5. Вийти")

        choice = input("Оберіть опцію: ").strip()
        if choice == '1':
            size = int(input("Введіть розмір куба: "))
            symbol = input("Введіть символ для куба: ")
            generator.add_object(Cube(size, symbol))
        elif choice == '2':
            radius = int(input("Введіть радіус сфери: "))
            symbol = input("Введіть символ для сфери: ")
            generator.add_object(Sphere(radius, symbol))
        elif choice == '3':
            generator.render()
        elif choice == '4':
            filename = input("Введіть ім'я файлу для збереження: ")
            generator.save_to_file(filename)
        elif choice == '5':
            print("Дякуємо за використання ASCII Art Generator!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
