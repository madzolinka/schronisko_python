import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, ttk, PhotoImage
from PIL import Image, ImageTk
from zwierze import Dog, Cat
from lista import Shelter

class ShelterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Schronisko dla zwierząt")
        self.shelter = Shelter()
        self.sort_ascending = True
        self.animals = []

        image = Image.open("pics/tlo.png")  #tło
        bg_image = ImageTk.PhotoImage(image)
        root.geometry(f"{image.width}x{image.height}")
        root.resizable(False, False)
        imgico = PhotoImage(file="pics/ikona.ico")
        self.root.iconphoto(False, imgico)

        # Utwórz Canvas z tłem
        self.canvas = tk.Canvas(root, width=image.width, height=image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        self.bg_image = bg_image  # przechowuj referencję, by obraz się nie zgubił

        menu_frame = tk.Frame(self.canvas, bg="")
        menu_frame.pack(pady=20, padx=(0, 290))

        btns = [
            ("Dodaj psa", self.add_dog),
            ("Dodaj kota", self.add_cat),
            ("Wyświetl wszystkie", self.show_all),
            ("Usuń po imieniu", self.remove_animal),
            ("Zapisz do pliku", self.save_to_file),
            ("Otwórz plik", self.shelter.open_file)]

        for i, (label, command) in enumerate(btns):
            tk.Button(menu_frame, text=label, command=command, width=20,
                      font=("Comic Sans MS", 10), bg="#c1d6ec", fg="#103051") \
                .grid(row=i, column=0, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def add_dog(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj psa")

        add_window.geometry("200x250")
        add_window.resizable(False, False)
        add_window.configure(bg="#f8d4e9")


        tk.Label(add_window, text="Imię:",font=("Comic Sans MS", 10), bg="#f8d4e9", fg="#993355").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Wiek:",font=("Comic Sans MS", 10), bg="#f8d4e9", fg="#993355").pack(pady=5)
        age_entry = tk.Entry(add_window)
        age_entry.pack(pady=5)

        tk.Label(add_window, text="Rasa:",font=("Comic Sans MS", 10), bg="#f8d4e9", fg="#993355").pack(pady=5)
        breed_entry = tk.Entry(add_window)
        breed_entry.pack(pady=5)

        def submit_dog():
            name = name_entry.get()
            age = age_entry.get()
            breed = breed_entry.get()

            if not name or not age or not breed:
                messagebox.showwarning("Błąd", "Wszystkie pola muszą być wypełnione.")
                return

            if not name.isalnum():
                messagebox.showwarning("Błąd", "Imię nie może zawierać znaków specjalnych.")
                return

            try:
                age = int(age)
            except ValueError:
                messagebox.showwarning("Błąd", "Wiek musi być liczbą.")
                return

            if age <= 0:
                messagebox.showwarning("Błąd", "Wiek musi być większy niż 0.")
                return

            self.shelter.add_animal(Dog(name, age, breed))
            messagebox.showinfo("Dodano", f"Dodano psa: {name}")
            add_window.destroy()

        submit_button = tk.Button(add_window, text="Dodaj psa", command=submit_dog,font=("Comic Sans MS", 10, "bold") ,bg="#f5bede", fg="#76233f")
        submit_button.pack(pady=10)

    def add_cat(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj kota")

        add_window.geometry("200x250")
        add_window.resizable(False, False)
        add_window.configure(bg="#f6cfa1")

        tk.Label(add_window, text="Imię:",font=("Comic Sans MS", 10), bg="#f6cfa1", fg="#913f13").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Wiek:",font=("Comic Sans MS", 10), bg="#f6cfa1", fg="#913f13").pack(pady=5)
        age_entry = tk.Entry(add_window)
        age_entry.pack(pady=5)

        tk.Label(add_window, text="Kolor:",font=("Comic Sans MS", 10), bg="#f6cfa1", fg="#913f13").pack(pady=5)
        color_entry = tk.Entry(add_window)
        color_entry.pack(pady=5)

        def submit_cat():
            name = name_entry.get()
            age = age_entry.get()
            color = color_entry.get()

            if not name or not age or not color:
                messagebox.showwarning("Błąd", "Wszystkie pola muszą być wypełnione.")
                return

            if not name.isalnum():
                messagebox.showwarning("Błąd", "Imię nie może zawierać znaków specjalnych.")
                return

            try:
                age = int(age)
            except ValueError:
                messagebox.showwarning("Błąd", "Wiek musi być liczbą.")
                return

            if age <= 0:
                messagebox.showwarning("Błąd", "Wiek musi być większy niż 0.")
                return

            self.shelter.add_animal(Cat(name, age, color))
            messagebox.showinfo("Dodano", f"Dodano kota: {name}")
            add_window.destroy()

        submit_button = tk.Button(add_window, text="Dodaj kota", command=submit_cat,font=("Comic Sans MS", 10, "bold") ,bg="#f1bd80", fg="#70310f")
        submit_button.pack(pady=10)


    def show_all(self):
        animals = self.shelter.list_animals()
        self.show_in_new_window("Wszystkie zwierzęta", animals)

    def remove_animal(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Usuń zwierzę")
        remove_window.geometry("200x100")
        remove_window.configure(bg="#f8b5b5")
        remove_window.resizable(False, False)

        tk.Label(remove_window, text="Imię:", font=("Comic Sans MS", 10),bg="#f8b5b5", fg="#8f1313").pack(pady=5)
        name_entry = tk.Entry(remove_window)
        name_entry.pack(pady=5)

        def submit_remove():
            name = name_entry.get()
            if name:
                self.shelter.remove_animal(name)
                messagebox.showinfo("Usunięto", f"Usunięto zwierzę o imieniu: {name}")
                remove_window.destroy()

        tk.Button(remove_window, text="Usuń", command=submit_remove,bg="#f19696", fg="#660a0a", font=("Comic Sans MS", 10, "bold")).pack(pady=3)

    def save_to_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if filename:
            self.shelter.save_to_file(filename)
            messagebox.showinfo("Zapisano", f"Dane zapisane do: {filename}")

    def refresh_table(self, frame, animals=None, title="", sort_by=None, parent=None, canvas=None,
                      species_filter="Wszystkie"):
        if animals is None:
            animals = self.shelter.get_all_animals()

        # FILTR
        if species_filter != "Wszystkie":
            cls = Dog if species_filter == "Psy" else Cat
            animals = [a for a in animals if isinstance(a, cls)]

        # SORT
        if sort_by == "age":
            animals = sorted(animals, key=lambda x: x.age, reverse=not self.sort_ascending)

        # Odśwież tabelę
        for w in frame.winfo_children(): w.destroy()
        self.show_in_new_window(title, animals, reuse_frame=frame, sort_by=sort_by,
                                parent_window=parent, canvas=canvas, species_filter=species_filter)

    def show_in_new_window(self, title, animals, reuse_frame=None, sort_by=None, parent_window=None, canvas=None,
                           species_filter="Wszystkie"):
        if reuse_frame and parent_window and canvas:
            frame = reuse_frame
            for w in frame.winfo_children(): w.destroy()
        else:
            parent_window = tk.Toplevel(self.root)
            parent_window.title(title)
            parent_window.geometry(f"470x{self.root.winfo_height()}")
            parent_window.resizable(False, False)

            canvas = tk.Canvas(parent_window, bg="#e6f4e6")
            scrollbar = tk.Scrollbar(parent_window, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=scrollbar.set)
            frame = tk.Frame(canvas, bg="#e6f4e6")
            canvas.create_window((0, 0), window=frame, anchor="nw")
            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)

        def limited_mouse_wheel(event):
            if event.delta > 0 and canvas.yview()[0] <= 0:
                return
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        parent_window.bind_all("<MouseWheel>", limited_mouse_wheel)

        headers = ["Gatunek", "Imię", "Wiek", "Rasa/Kolor"]
        for col, h in enumerate(headers):
            if h == "Wiek":
                def toggle_sort():
                    self.sort_ascending = not self.sort_ascending
                    self.refresh_table(frame, title=title, sort_by="age",
                                       parent=parent_window, canvas=canvas, species_filter=species_filter)

                btn = tk.Button(frame, text=f"Wiek {'🔼' if self.sort_ascending else '🔽'}",
                                font=("Comic Sans MS", 11, "bold"),
                                bg="#b2d8b2", fg="#0e6c0e", relief="ridge", borderwidth=1, padx=10, pady=6,
                                command=toggle_sort)
                btn.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

            elif h == "Gatunek":
                next_filter = {"Wszystkie": "Psy", "Psy": "Koty", "Koty": "Wszystkie"}[species_filter]
                btn = tk.Button(frame, text=species_filter, font=("Comic Sans MS", 11, "bold"),
                                bg="#b2d8b2", fg="#0e6c0e", relief="ridge", borderwidth=1, padx=10, pady=6,
                                command=lambda: self.refresh_table(frame, title=title,
                                                                   parent=parent_window, canvas=canvas,
                                                                   species_filter=next_filter)
                                )
                btn.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)
            else:
                tk.Label(frame, text=h, font=("Comic Sans MS", 11, "bold"), bg="#b2d8b2", fg="#0e6c0e",
                         relief="ridge", borderwidth=1, padx=10, pady=6).grid(row=0, column=col, sticky="nsew", padx=1,
                                                                              pady=1)

        for row, animal in enumerate(animals, start=1):
            values = ["🐶" if isinstance(animal, Dog) else "🐱", animal.name, animal.age,
                      animal.breed if isinstance(animal, Dog) else animal.color]
            for col, val in enumerate(values):
                tk.Label(frame, text=val, font=("Comic Sans MS", 10), bg="#d9f2d9", fg="#0e6c0e",
                         relief="ridge", borderwidth=1, padx=8, pady=4).grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def on_exit(self):
        def ask_save():
            answer = messagebox.askyesnocancel("Zamknij", "Czy chcesz zapisać dane przed wyjściem?")
            if answer is None:
                return False
            if answer:
                if self.shelter.current_file:
                    self.shelter.save_to_file()
                    return True
                else:
                    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Pliki tekstowe", "*.txt")])
                    if not file_path:
                        return ask_save()
                    self.shelter.save_to_file(file_path)
                    return True
            else:
                return True

        if ask_save():
            self.root.destroy()

# Uruchomienie GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ShelterApp(root)
    root.mainloop()