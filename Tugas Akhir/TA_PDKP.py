#Tugas TA
#Muhamad Ibnu Fadhil

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
from turtle import bgcolor
from xml.etree.ElementTree import C14NWriterTarget

#setting GUI warna dan dimensi
window_x=960
window_y=540
warnaBG = "#0178ba"
warnaBox = "#005ea4"
warnaText = "white"
warnaButton1 = "#305F72"
warnaButton2 = "#cb185a"

#inisialisasi Data dan GUI
calon = []
window = Tk()
window.resizable(width=False, height=False)

#background UI
bgimage = PhotoImage(file="Tugas Akhir/bg_image.png")
bg1 = Label(window, image=bgimage).place(x=0, y=0, relwidth=1, relheight=1)

#push data stack
def stackPush():
    data = userInput.get()
    calon.append(data)
    userInput.set("")

#pop data stack    
def stackPop():
    if calon:
        calon.pop()
    else:
       messagebox.showwarning("Peringatan!", "Tidak ditemukan kandidat") 

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
    pb = Progressbar(
    window,
    orient = HORIZONTAL,
    length = 500,
    mode = 'determinate'
    )
    pb.pack(side= BOTTOM, pady=35)
    pb['value'] = 0
    for i in range(100):
        window.update_idletasks()
        pb['value'] += 1
        time.sleep(1/50)

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
    pb['value']=0
    pb.destroy()

#inisialisasi window GUI
window.geometry(f"{window_x}x{window_y}")
window.title("Program Pemenang Arisan") 

#cetak label
labelKel23 = Label(window, text="Program Pemenang Arisan", font="Helvetica 20  bold", fg= "white", bg= warnaBG).place(x=460, y=5, anchor=N)
labelnama = Label(window,text ="Nama", font="Helvetica 14 bold",fg= warnaText, bg= warnaBG).place(x=70, y=58,)

#memasukkan user input
userInput = StringVar()
entry = Entry(window,textvariable=userInput, font= "Helvetica 14", bg= warnaBox, fg= warnaText).place(x=140, y=60)

#buttons
buttonSubmit = Button(window, text="Submit", command=lambda: [stackPush(), tampilData()],font= "Helvetica 11 bold",fg="White", bg=warnaButton1).place(x=370, y=72, anchor=W)
buttonPop = Button(window, text= "Pop data", command=lambda: [stackPop(), tampilData()],font= "Helvetica 11 bold",fg="White", bg=warnaButton1).place(x=435, y=72, anchor=W)
buttonGenerate = Button(window, text="Generate Pemenang", command=lambda: [randomFunction(), tampilData()], font="Helvetica 11 bold", fg="White", bg=warnaButton2)
buttonGenerate.place(x=530, y=72, anchor=W)

#tampil Calon Pemenang
showNama = Text(window, width=49, height= 10, font="Helvetica 12",bg=warnaBox, fg= warnaText)
showNama.insert("end", "Calon Pemenang : ")
showNama.insert("end", '\n'.join(calon))
showNama.configure(state="disabled")
showNama.place(x= 70, y=100)

#Generate dan show winner
tampilWinner = Text(window, width=30, height= 10, font="Helvetica 12", bg= warnaBox, fg= warnaText)
tampilWinner.insert("end", "Pemenang adalah : \n")
tampilWinner.configure(state="disabled")
tampilWinner.place(x= 530, y=100)

#loop window
window.mainloop()
