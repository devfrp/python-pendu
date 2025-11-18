import tkinter as tk
from tkinter import messagebox
from choix_mot import choix_mot
import os, sys
import csv
import random

#pour compiler avec pyinstaller
def resource_path(relative_path):
    
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def choix_mot():
    csv_path = resource_path("dico.csv")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        mots = [row[0] for row in reader]

    return random.choice(mots)

#code de l'application graphique
class Pendugraphique(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pendu")
        self.resizable(True, True)

        self.mot_a_trouver = choix_mot().upper()
        self.lettres_trouvees = set()
        self.tentatives_restantes = 7
        self.lettres_deja_tapees = set()

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(padx=10, pady=10)

        self.ascii_var = tk.StringVar(value='')
        self.ascii_lbl = tk.Label(self.top_frame, textvariable=self.ascii_var, font=('Courier', 12), justify='left')
        self.ascii_lbl.grid(row=0, column=0, rowspan=2, sticky='nw')

        self.word_frame = tk.Frame(self.top_frame)
        self.word_frame.grid(row=0, column=1, sticky='w', padx=(10,0))
        self.letter_vars = []
        for ch in self.mot_a_trouver:
            var = tk.StringVar(value='_' if ch != ' ' else ' ')
            lbl = tk.Label(self.word_frame, textvariable=var, font=('Consolas', 18), width=2)
            lbl.pack(side='left')
            self.letter_vars.append((var, ch))

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=(0,10))


        self.letter_buttons = {}
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, ch in enumerate(alphabet):
            btn = tk.Button(self.buttons_frame, text=ch, width=3, command=lambda c=ch: self.lettre(c))
            btn.grid(row=i//9, column=i%9, padx=2, pady=2)
            self.letter_buttons[ch] = btn

        self.status_var = tk.StringVar(value=f'Tentatives restantes: {self.tentatives_restantes}')
        self.status_lbl = tk.Label(self, textvariable=self.status_var)
        self.status_lbl.pack(pady=(0,10))

        self.pendu()

    def lettre(self, letter):
        letter = letter.upper()
        btn = self.letter_buttons.get(letter)
        if btn:
            btn.config(state='disabled')
        


        if letter in self.mot_a_trouver:
            self.lettres_trouvees.add(letter)
            for var, ch in self.letter_vars:
                if ch == letter:
                    var.set(letter)
        else:
            self.tentatives_restantes -= 1
            self.pendu()

        self.status_var.set(f'Tentatives restantes: {self.tentatives_restantes}')
        self.check_fin()

    def check_fin(self):
        won = all(var.get() != '_' for var, _ in self.letter_vars)
        if won:
            messagebox.showinfo('Gagné', f'Bravo ! Vous avez trouvé: {self.mot_a_trouver}')
            self.destroy()
        elif self.tentatives_restantes <= 0:
            self.montrer_mot()
            messagebox.showinfo('Perdu', f'Vous avez perdu. Le mot était: {self.mot_a_trouver}')
            self.destroy()

    def montrer_mot(self):
        for var, ch in self.letter_vars:
            var.set(ch)

    def pendu(self):
        self.ascii_var.set(self.pedu_ascii())

    def pedu_ascii(self):
        t = self.tentatives_restantes
        if t == 0:
            return (
"  ======Y==\n"
" ||/    |\n"
" ||     O\n"
" ||    /|\\ \n"
" ||    / \\ \n"
"/||\n"
"=========="
            )
        if t == 1:
            return (
" ||/    |\n"
" ||     O\n"
" ||    /|\\ \n"
" ||    / \\ \n"
"/||\n"
"=========="
            )
        elif t == 2:
            return (
" ||     O\n"
" ||    /|\\ \n"
" ||    / \\ \n"
"/||\n"
"=========="
            )
        elif t == 3:
            return (
" ||    /|\\ \n"
" ||    / \\ \n"
"/||\n"
"=========="
            )
        elif t == 4:
            return (
" ||    / \\ \n"
"/||\n"
"=========="
            )
        elif t == 5:
            return (
"/||\n"
"=========="
            )
        elif t == 6:
            return ("==========")
        else:
            return ('')


if __name__ == '__main__':
    app = Pendugraphique()
    app.mainloop()


