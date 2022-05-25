import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Lista Elementos")

        self.listbox = tk.Listbox(self, selectforeground="#ffffff",
                                  selectbackground="#00aa00",
                                  selectborderwidth=5)
        self.listbox.pack()

        self.pack()
        items = (
            "Python",
            "C",
            "C++",
            "Java"
        )
        self.listbox.insert(0, *items)



main_window = tk.Tk()
app = Application(main_window)
app.mainloop()