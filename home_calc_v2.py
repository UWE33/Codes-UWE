
import tkinter as tk
from tkinter import ttk

def formel():
    strom_f =float(strom_wert.get())
    pelets_f=float(pelets_wert.get())
    wasser_f = float(wasser_wert.get())
    abwasser_f = float(abwasser_wert.get())
    muell_f =float(muell_wert.get())
    abschlag_f = float(abschlag_wert.get())
    telefon_f = float(telefon_wert.get())
    gez_f = float(gez_wert.get())
    grundsteuer_f = float(grundsteuer_wert.get())
    versicherung_f = float(versicherung_wert.get())
    kamin_f = float(kamin_wert.get())

    kosten_tobi = (strom_f + wasser_f+ +abwasser_f + pelets_f +
                   versicherung_f + kamin_f + grundsteuer_f)

    kosten_momdad = muell_f + telefon_f + gez_f
    abschlag = (abschlag_f*12)
    berechnung = ((kosten_tobi + kosten_momdad)/2) -kosten_momdad - abschlag

    result = ttk.Label(click_frame, text=berechnung)
    result.grid(column=0, row=0)


root = tk.Tk()
root.title("home_calculator")
root.geometry("600x300+100+350")


# frames_aufgeteilt 3x
tobi_frame = ttk.LabelFrame(root, relief="ridge", text="Kosten Tobi")
tobi_frame.grid(column=0, row=0)

momdad_frame = ttk.LabelFrame(root, relief="ridge", text="Kosten Mom & Dad")
momdad_frame.grid(column=0, row=1)

click_frame = ttk.LabelFrame(root, relief="ridge")
click_frame.grid(column=1, row=0)


#Strom
strom = ttk.Label(tobi_frame, text="Strom")
strom.grid(column=0, row=0)

strom_wert = tk.StringVar()
strom_eingabe = ttk.Entry(tobi_frame, textvariable=strom_wert)
strom_eingabe.grid(column=2, row=0)

#Pellets
strom = ttk.Label(tobi_frame, text="Pellets")
strom.grid(column=0, row=1)

pelets_wert = tk.StringVar()
pelets_eingabe = ttk.Entry(tobi_frame, textvariable=pelets_wert)
pelets_eingabe.grid(column=2, row=1)

#Wasser
wasser = ttk.Label(tobi_frame, text="Wasser")
wasser.grid(column=0, row=2)

wasser_wert =tk.StringVar()
wasser_eingabe = ttk.Entry(tobi_frame, textvariable=wasser_wert)
wasser_eingabe.grid(column=2, row=2)

#Abwasser
abwasser = ttk.Label(tobi_frame, text="Abwasser")
abwasser.grid(column=0, row=3)

abwasser_wert =tk.StringVar()
abwasser_eingabe = ttk.Entry(tobi_frame, textvariable=abwasser_wert)
abwasser_eingabe.grid(column=2, row=3)

#Versicherung
versicherung = ttk.Label(tobi_frame, text="Gebäudeversicherung")
versicherung.grid(column=0, row=4)

versicherung_wert =tk.StringVar()
versicherung_eingabe = ttk.Entry(tobi_frame, textvariable=versicherung_wert)
versicherung_eingabe.grid(column=2, row=4)

#Kaminkehrer
kamin = ttk.Label(tobi_frame, text="Kaminkehrer")
kamin.grid(column=0, row=5)

kamin_wert =tk.StringVar()
kamin_eingabe = ttk.Entry(tobi_frame, textvariable=kamin_wert)
kamin_eingabe.grid(column=2, row=5)

#Grundsteuer
grundsteuer = ttk.Label(tobi_frame, text="Grundsteuer")
grundsteuer.grid(column=0, row=6)

grundsteuer_wert =tk.StringVar()
grundsteuer_eingabe = ttk.Entry(tobi_frame, textvariable=grundsteuer_wert)
grundsteuer_eingabe.grid(column=2, row=6)

#Berechnungsknopf
calc_button = ttk.Button(click_frame, command=formel, text="Berechnung hier klicken, bei + Nachzahlung")
calc_button.grid(column=1, row=5)

#calc_button = ttk.Button(tobi_frame, command=root.destroy, text="Programm schließen")
#calc_button.grid(column=1, row=6, sticky="w")



#Reset Button der Werte
def reset_1():
    wasser_eingabe.delete(0,"end")

def reset_2():
    strom_eingabe.delete(0,"end")

def reset_3():
    muell_eingabe.delete(0,"end")

def reset_4():
    telefon_eingabe.delete(0,"end")

def reset_5():
    gez_eingabe.delete(0,"end")

def reset_6():
    versicherung_eingabe.delete(0,"end")

def reset_7():
    abschlag_eingabe.delete(0,"end")

def reset_8():
    kamin_eingabe.delete(0,"end")

def reset_9():
    pelets_eingabe.delete(0,"end")

def reset_10():
    abwasser_eingabe.delete(0,"end")

def reset_11():
    grundsteuer_eingabe.delete(0,"end")

all_commands =  command=lambda:[reset_1(),reset_2(),reset_3(),
                                reset_4(),reset_5(), reset_6(),
                                reset_7(), reset_8(),reset_9(),
                                reset_10(),reset_11()]



res = ttk.Button(click_frame, text="Reset alle Werte" , command= all_commands)
res.grid(column=1, row=7)


muelltonne = ttk.Label(momdad_frame, text="Mülltonne")
muelltonne.grid(column=0, row=2)

muell_wert= tk.StringVar()
muell_eingabe = ttk.Entry(momdad_frame, textvariable=muell_wert)
muell_eingabe.grid(column=1, row=2)


telefon = ttk.Label(momdad_frame, text="Telefon/Internet")
telefon.grid(column=0, row=3)

telefon_wert= tk.StringVar()
telefon_eingabe = ttk.Entry(momdad_frame, textvariable=telefon_wert)
telefon_eingabe.grid(column=1, row=3)


gez = ttk.Label(momdad_frame, text="GEZ")
gez.grid(column=0, row=4)

gez_wert= tk.StringVar()
gez_eingabe = ttk.Entry(momdad_frame, textvariable=gez_wert)
gez_eingabe.grid(column=1, row=4)



abschlag = ttk.Label(momdad_frame, text="mon. Abschlagszahlung Mom&Dad")
abschlag.grid(column=0, row=5)

abschlag_wert= tk.StringVar()
abschlag_eingabe = ttk.Entry(momdad_frame, textvariable=abschlag_wert)
abschlag_eingabe.grid(column=1, row=5)



#for item in label_1.keys():
#   print(item,":", label_1[item])

root.mainloop()