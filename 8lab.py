import pandas as pd
import matplotlib.pyplot as plt
import os

class CSVVisualizer:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

        # Перевірка наявності файлу, створення, якщо не існує
        if not os.path.exists(self.filename):
            self.create_sample_csv()
        
        self.load_data()

    def create_sample_csv(self):
        # Приклад базового CSV-файлу
        sample_data = {
            "Date": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01"],
            "Value1": [10, 15, 20, 25],
            "Value2": [20, 25, 30, 35]
        }
        df = pd.DataFrame(sample_data)
        df.to_csv(self.filename, index=False)
        print(f"Створено новий CSV-файл із базовими даними: {self.filename}")

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename)
            print("Дані завантажено успішно.")
        except Exception as e:
            print(f"Помилка завантаження даних: {e}")

    def display_data_summary(self):
        if self.data is not None:
            print("Огляд даних:\n", self.data.describe())
        else:
            print("Дані ще не завантажені.")

    def plot_data(self):
        if self.data is not None:
            plt.plot(self.data["Date"], self.data["Value1"], label="Value1")
            plt.plot(self.data["Date"], self.data["Value2"], label="Value2")
            plt.xlabel("Date")
            plt.ylabel("Values")
            plt.legend()
            plt.title("Basic Plot of Value1 and Value2 Over Time")
            plt.show()
        else:
            print("Дані ще не завантажені.")

    def plot_multiple_subplots(self):
        if self.data is not None and len(self.data.columns) > 2:
            fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            axs[0].plot(self.data["Date"], self.data["Value1"], color='b')
            axs[0].set_title("Value1 Over Time")
            axs[1].plot(self.data["Date"], self.data["Value2"], color='r')
            axs[1].set_title("Value2 Over Time")
            plt.show()
        else:
            print("Необхідно більше стовпців для багатопанельної діаграми.")

# Використання класу
visualizer = CSVVisualizer("ваш_файл.csv")
visualizer.display_data_summary()
visualizer.plot_data()
visualizer.plot_multiple_subplots()
