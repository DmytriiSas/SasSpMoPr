import os
import logging
import pydoc

# Налаштування логування
logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Бібліотека класів
class FileManager:
    """Клас для роботи з файлами."""
    def read_file(self, file_path: str) -> str:
        """Читає файл."""
        logging.info(f"Читається файл: {file_path}")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            logging.error(f"Помилка читання файлу: {e}")
            return str(e)

    def write_file(self, file_path: str, content: str) -> None:
        """Записує в файл."""
        logging.info(f"Запис у файл: {file_path}")
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
        except Exception as e:
            logging.error(f"Помилка запису у файл: {e}")


class Calculator:
    """Калькулятор базових операцій."""
    @staticmethod
    def add(a: float, b: float) -> float:
        """Додає два числа."""
        result = a + b
        logging.info(f"Додавання {a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Віднімає два числа."""
        result = a - b
        logging.info(f"Віднімання {a} - {b} = {result}")
        return result


class DataProcessor:
    """Обробка даних."""
    def sort_data(self, data: list) -> list:
        """Сортує список."""
        logging.info(f"Сортування даних: {data}")
        return sorted(data)


class Logger:
    """Утиліта для роботи з логами."""
    def show_logs(self):
        """Виводить лог-файл."""
        fm = FileManager()
        logs = fm.read_file("app.log")
        print(logs)


# Runner (Facade Pattern)
class Runner:
    """Runner для запуску додатків."""
    def __init__(self):
        self.file_manager = FileManager()
        self.calculator = Calculator()
        self.data_processor = DataProcessor()
        self.logger = Logger()

    def show_menu(self):
        """Головне меню."""
        while True:
            print("\n=== Головне меню ===")
            print("1. Читати файл")
            print("2. Записати у файл")
            print("3. Калькулятор")
            print("4. Сортувати дані")
            print("5. Логи")
            print("6. Вихід")
            choice = input("Оберіть опцію: ")

            if choice == "1":
                file_path = input("Введіть шлях до файлу: ")
                print(self.file_manager.read_file(file_path))
            elif choice == "2":
                file_path = input("Введіть шлях до файлу: ")
                content = input("Введіть контент: ")
                self.file_manager.write_file(file_path, content)
            elif choice == "3":
                a = float(input("Перше число: "))
                b = float(input("Друге число: "))
                print(f"Результат: {self.calculator.add(a, b)}")
            elif choice == "4":
                data = input("Введіть список чисел через кому: ").split(",")
                data = [int(x) for x in data]
                print(f"Відсортований список: {self.data_processor.sort_data(data)}")
            elif choice == "5":
                self.logger.show_logs()
            elif choice == "6":
                print("До побачення!")
                break
            else:
                print("Невірний вибір, спробуйте знову.")


# Запуск Runner
if __name__ == "__main__":
    runner = Runner()
    runner.show_menu()
