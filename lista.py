from zwierze import Dog, Cat
from tkinter import filedialog, messagebox

class Shelter:
    def __init__(self):
        self.animals = []
        self.current_file = None  # śledzenie pliku

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        self.animals = [a for a in self.animals if a.name != name]

    def list_animals(self):
        return self.animals

    def save_to_file(self, filename=None):
        if filename is None:
            filename = self.current_file
        if filename is None:
            return False
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for a in self.animals:
                    f.write(str(a) + '\n')
        except Exception as e:
            print(f"Błąd zapisu: {e}")

    def get_all_animals(self):
        return self.animals  # lub inna lista, w której przechowujesz zwierzęta

    def load_data_from_file(self, filename):
        self.animals = []
        self.current_file = filename
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()  # Usuwanie zbędnych spacji/nowych linii
                    if line.startswith("Kot"):
                        # Parsowanie danych o kocie
                        name = line.split(":", 1)[1].split(",")[0].strip()  # Imię kota
                        color = line.split("kolor:", 1)[1].split(",")[0].strip()  # Kolor kota
                        age = int(line.split("wiek:", 1)[1].split("lat")[0].strip())  # Wiek kota
                        self.add_animal(Cat(name, age, color))  # Dodanie kota do schroniska
                    elif line.startswith("Pies"):
                        # Parsowanie danych o psie
                        name = line.split(":", 1)[1].split(",")[0].strip()  # Imię psa
                        breed = line.split("rasa:", 1)[1].split(",")[0].strip()  # Rasa psa
                        age = int(line.split("wiek:", 1)[1].split("lat")[0].strip())  # Wiek psa
                        self.add_animal(Dog(name, age, breed))  # Dodanie psa do schroniska
        except FileNotFoundError:
            print("Plik nie istnieje. Tworzymy nowy plik.")

    def open_file(self):
        if self.animals:  # jeśli są dane wczytane
            answer = messagebox.askyesnocancel("Otwórz nowy plik",
                                               "Czy chcesz zapisać dane przed otwarciem nowego pliku?")
            if answer is None:
                return  # Anulowano otwieranie
            if answer:
                if self.current_file:
                    self.save_to_file()
                else:
                    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Pliki tekstowe", "*.txt")])
                    if not file_path:
                        return  # Anulowano wybór pliku
                    self.save_to_file(file_path)

        filename = filedialog.askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])
        if filename:
            self.load_data_from_file(filename)
            self.current_file = filename