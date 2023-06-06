from tkinter import *


def arial():
    typed_text = text_box.get("1.0", END)
    changed_font.config(text=typed_text, font=("Arial"))


def algerian():
    typed_text = text_box.get("1.0", END)
    changed_font.config(text=typed_text, font=("Algerian"))


def elephant():
    typed_text = text_box.get("1.0", END)
    changed_font.config(text=typed_text, font=("Elephant"))


def magneto():
    typed_text = text_box.get("1.0", END)
    changed_font.config(text=typed_text, font=("Magneto"))


def forte():
    typed_text = text_box.get("1.0", END)
    changed_font.config(text=typed_text, font=("Forte"))


window = Tk()
window.title("Different Font Styles")
window.config(padx=20, pady=20)

top_label = Label(text="Welcome to the fontsy.....")
top_label.grid(row=0, column=1)

text_box = Text(height=5, width=40)
text_box.grid(row=1, column=1)
text_box.config(padx=10, pady=10)

changed_font = Label(text="Typed text will appear here")
changed_font.grid(row=7, column=1)

change_label = Label(text="PRESS BUTTON \n TO CHANGE FONT")
change_label.grid(row=1, column=2)

arial_black_button = Button(text="Arial BLack", width=10, command=arial, activeforeground="blue")
arial_black_button.grid(row=2, column=2)

algerian_button = Button(text="Algerian", width=10, command=algerian, activeforeground="blue")
algerian_button.grid(row=3, column=2)

elephant_button = Button(text="Elephant", width=10, command=elephant, activeforeground="blue")
elephant_button.grid(row=4, column=2)

magneto_button = Button(text="Magneto", width=10, command=magneto, activeforeground="blue")
magneto_button.grid(row=5, column=2)

forte_button = Button(text="Forte", width=10, command=forte, activeforeground="blue")
forte_button.grid(row=6, column=2)

window.mainloop()
