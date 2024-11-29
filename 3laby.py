import pyfiglet
from colorama import Fore, Style, init

# Ініціалізуємо бібліотеку colorama для роботи з кольорами
init(autoreset=True)

class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.font = "slant"
        self.color = Fore.WHITE
        self.symbol = "#"

    def get_user_input(self):
        # Введення користувача для тексту
        self.text = input("Vvedit' slovo abo frazu dlia ASCII-artu: ")
    
    def choose_font(self):
        # Вибір шрифту
        fonts = pyfiglet.FigletFont.getFonts()
        print("Dostupni shrifti:")
        for i, font in enumerate(fonts[:10], 1):  # Вивести лише кілька прикладів шрифтів
            print(f"{i}. {font}")
        
        font_choice = input("Vyberit' nomer shryftu abo vvedit' svoi: ")
        if font_choice.isdigit() and int(font_choice) <= len(fonts[:10]):
            self.font = fonts[int(font_choice) - 1]
        else:
            self.font = font_choice if font_choice in fonts else "slant"
    
    def choose_color(self):
        # Вибір кольору тексту
        colors = {
            "1": Fore.RED, "2": Fore.GREEN, "3": Fore.BLUE,
            "4": Fore.YELLOW, "5": Fore.MAGENTA, "6": Fore.CYAN, "7": Fore.WHITE
        }
        print("Dostupni kol'ory: 1. Chervonyi 2. Zelenyi 3. Synii 4. Zhouvtyi 5. Fioletovyi 6. Biryzovyi 7. Bilyi")
        color_choice = input("Vyberit' kol'ir za nomerom: ")
        self.color = colors.get(color_choice, Fore.WHITE)

    def generate_ascii_art(self):
        # Генерація ASCII-арту
        figlet = pyfiglet.Figlet(font=self.font)
        ascii_art = figlet.renderText(self.text)
        return ascii_art
    
    def preview_art(self):
        # Попередній перегляд ASCII-арту
        ascii_art = self.generate_ascii_art()
        print("\nPoperednij perehliad:")
        print(self.color + ascii_art)

    def save_to_file(self, ascii_art):
        # Збереження у файл
        with open("ascii_art.txt", "w", encoding="utf-8") as file:
            file.write(ascii_art)
        print("ASCII-art zberezheno u faili 'ascii_art.txt'")
    
    def run(self):
        # Основний інтерфейс користувача
        print("Vitajemo u ASCII ART Generatori!")
        self.get_user_input()
        self.choose_font()
        self.choose_color()
        
        self.preview_art()
        
        save_choice = input("Bazhaete zberehty ASCII-art u fail? (tak/ni): ").strip().lower()
        if save_choice == "tak":
            ascii_art = self.generate_ascii_art()
            self.save_to_file(ascii_art)
        
        print("Diakujemo za vykorystannia ASCII ART Generatora!")

# Запуск генератора
if __name__ == "__main__":
    generator = ASCIIArtGenerator()
    generator.run()
