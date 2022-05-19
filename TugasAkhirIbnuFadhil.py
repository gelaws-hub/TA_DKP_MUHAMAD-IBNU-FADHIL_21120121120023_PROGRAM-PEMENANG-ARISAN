#Tugas TA

#List Modul yang digunakan
#1. Modul 1 : Variable
#2. Modul 2 : if-else
#3. Modul 3 : Perulangan for (untuk membuat loading bar)
#4. Modul 4 : Function
#5. Modul 7 : Stack
#6. Modul 8 : GUI

#import librari tkinter, random dan time
from tkinter import *
from tkinter import messagebox
import random
from tkinter.ttk import Progressbar
from tkinter.messagebox import *
import time

#inisialisasi Data dan GUI
calon = []
window = Tk()

#push data stack
def stackPush():
    data = userInput.get()
    calon.append(data)
    userInput.set("")

#pop data stack    
def stackPop():
    calon.pop()

#tampil data stack
def tampilData():
    global showNama
    showNama.configure(state="normal")
    showNama.delete(1.0,"end")
    showNama.insert("end", "Calon Pemenang : \n")
    showNama.insert("end", '\n'.join(calon))
    showNama.configure(state="disabled")

#algortima loading bar dan random function
def randomFunction():
    global tampilWinner
    pb['value'] = 0
    for i in range(100):
        window.update_idletasks()
        pb['value'] += 1
        time.sleep(1/100)
    tampilWinner.configure(state="normal")
    if calon:
        winner = random.choice(calon)
        calon.remove(winner)
        tampilWinner.insert("end","Selamat kepada ")
        tampilWinner.insert("end", winner)
        tampilWinner.insert("end", '\n')
    else:
        messagebox.showwarning("Peringatan!", "Tidak ditemukan kandidat")
    tampilWinner.configure(state="disabled")

#inisialisasi window GUI
window.geometry("320x550")
window.title("Program Pemenang Arisan") 

#cetak labelKel23 dan labelNama
labelKel23 = Label(window, text="Program Pemenang Arisan").pack(side= TOP)
labelnama = Label(window,text = "Masukkan Nama calon pemenang arisan : \n").pack(side=TOP)

#memasukkan user input
userInput = StringVar()
entry = Entry(window,textvariable=userInput).pack(side=TOP)

#buttons
buttonSubmit = Button(window, text="Submit", command=lambda: [stackPush(), tampilData()]).pack(pady=5)
buttonPop = Button(window, text= "Pop Data", command=lambda: [stackPop(), tampilData()]).pack(pady=5)

#tampil Calon Pemenang
showNama = Text(window, width=30, height= 10)
showNama.insert("end", "Calon Pemenang : ")
showNama.insert("end", '\n'.join(calon))
showNama.configure(state="disabled")
showNama.pack(pady=5)

#Generate dan show winner
buttonGenerate = Button(window, text="Generate Pemenang", command=lambda: [randomFunction(), tampilData()]).pack()
tampilWinner = Text(window, width=30, height= 5)
tampilWinner.insert("end", "Pemenang adalah : \n")
tampilWinner.configure(state="disabled")
tampilWinner.pack(pady=5)

#loading...
pb = Progressbar(
    window,
    orient = HORIZONTAL,
    length = 100,
    mode = 'determinate'
    )
pb.pack(side= BOTTOM, pady=35)

#loop window
window.mainloop()
