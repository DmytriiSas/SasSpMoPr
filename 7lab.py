import requests
import json
import csv
import re
import os
from typing import List, Dict, Any
from datetime import datetime

# Завдання 1: Патерн Repository
class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_data(self, endpoint: str) -> List[Dict[str, Any]]:
        """Виконати GET-запит для отримання даних з API."""
        response = requests.get(f"{self.base_url}/{endpoint}")
        response.raise_for_status()
        return response.json()

# Завдання 1: Патерн Unit of Work
class UnitOfWork:
    def __init__(self):
        self.history = []

    def register_action(self, action: str):
        """Зареєструвати дію в історії."""
        timestamp = datetime.now().isoformat()
        self.history.append(f"{timestamp}: {action}")
        print(f"Action registered: {action}")

    def show_history(self):
        """Відобразити історію запитів."""
        for record in self.history:
            print(record)

# Завдання 2: Інтеграція API
class DataService:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_users(self) -> List[Dict[str, Any]]:
        """Отримати список користувачів з API."""
        return self.api_client.fetch_data("users")

    def get_posts(self) -> List[Dict[str, Any]]:
        """Отримати список постів з API."""
        return self.api_client.fetch_data("posts")

# Завдання 3: Введення користувача
class UserInterface:
    def __init__(self, data_service: DataService, unit_of_work: UnitOfWork):
        self.data_service = data_service
        self.unit_of_work = unit_of_work

    def show_menu(self):
        """Показати головне меню."""
        print("\n--- API Client Menu ---")
        print("1. Show Users")
        print("2. Show Posts")
        print("3. Show History")
        print("4. Exit")

    def get_user_choice(self) -> str:
        return input("Enter your choice: ")

    def display_users(self):
        users = self.data_service.get_users()
        self.unit_of_work.register_action("Fetched users")
        print("\nUsers:")
        for user in users:
            print(f"{user['id']}: {user['name']} - {user['email']}")

    def display_posts(self):
        posts = self.data_service.get_posts()
        self.unit_of_work.register_action("Fetched posts")
        print("\nPosts:")
        for post in posts:
            print(f"{post['id']}: {post['title']}")

    def display_history(self):
        self.unit_of_work.show_history()

# Завдання 6: Збереження даних
class DataExporter:
    @staticmethod
    def export_to_json(data: List[Dict[str, Any]], filename: str):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data exported to {filename}")

    @staticmethod
    def export_to_csv(data: List[Dict[str, Any]], filename: str):
        if data:
            keys = data[0].keys()
            with open(filename, "w", newline='') as file:
                dict_writer = csv.DictWriter(file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
            print(f"Data exported to {filename}")

# Завдання 8: Ведення історії обчислень
class HistoryManager:
    def __init__(self, unit_of_work: UnitOfWork):
        self.unit_of_work = unit_of_work

    def save_history(self, filename: str):
        with open(filename, "w") as file:
            for record in self.unit_of_work.history:
                file.write(record + "\n")
        print(f"History saved to {filename}")

# Основний код
def main():
    base_url = "https://jsonplaceholder.typicode.com"  # Завдання 1: API для роботи
    api_client = APIClient(base_url)
    data_service = DataService(api_client)
    unit_of_work = UnitOfWork()
    user_interface = UserInterface(data_service, unit_of_work)
    history_manager = HistoryManager(unit_of_work)

    while True:
        user_interface.show_menu()
        choice = user_interface.get_user_choice()

        if choice == "1":
            user_interface.display_users()
        elif choice == "2":
            user_interface.display_posts()
        elif choice == "3":
            user_interface.display_history()
        elif choice == "4":
            history_manager.save_history("history.txt")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
