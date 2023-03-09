
#Eingaben hier#
#beta = 82   #Eingabe80°= Rücklauf10° // Eingabe100° =Vorlauf10°
#gamma = 18  # SAW-Winkel unten
#a = 100      # Hub

# ergibt sich aus oberer Eingabe
#alpha = (180 - beta - gamma)
# c =       # Verfahrweg, das Ergebnis der Rechnung

def math1():
    import math as m
    gamma = float(move_value.get())
    a = float(stroke_value.get())
    beta = float(forward_back_value.get())
    alpha = (180 - beta - gamma)
    c = m.sin(m.pi / 180 * gamma) * a / (m.sin(m.pi / 180 * alpha)) #umgestellter Sinussatz für meine Anwendung
    c = (round(c, 2))
    result1 = ttk.Label(way_frame, text=c)
    result1.grid()

#ab hier zweiter Rechner angehängt

def math2():
    import math as m
    saw = float(eingabefeld_wert.get())
    stroke = float(eingabefel_wert.get())
    x = float ((saw) / (stroke))
    result2 = (m.atan(x) * (180/m.pi))
    #result = (math.tan((2 * math.pi * angle) / 360)) * (stroke)
    result2=round(result2,2)
    textausgabe = ttk.Label(angle_frame,text=result2)
    textausgabe.grid( column=2)


import tkinter as tk
from tkinter import ttk


#Hauptenster Position;Name, Größe
root = tk.Tk()
root.title("SAW-Rechner")
root.geometry("550x660+1320+180")
# Breite x Länge + Position rechts-links + oben-unten



# zwei Frames angelegt_ Weg & Winkel Programme vereint
way_frame = ttk.LabelFrame(root,)
way_frame.grid(padx=5, pady=10 ,column=0, row=0, sticky="ns")

angle_frame= ttk.LabelFrame(root)
angle_frame.grid(pady=10, column=2,row=0, padx=30, sticky="ns")

pic_frame = ttk.LabelFrame(root)
pic_frame.grid(pady=10, column=1, row=0)

reset_frame = ttk.LabelFrame(root)
reset_frame.grid(column=1, row=5)

#---------------------------------------------------------------


info_label = ttk.Label(way_frame, text="Schrägenwinkel unten")
info_label.grid( column=0, row=0,)


# Eingabe Winkel unten am SAW
move_value=tk.StringVar()
move=ttk.Entry(way_frame, textvariable=move_value)
move.grid(column=0, row=1)

info_label0 = ttk.Label(way_frame, text="Hub")
info_label0.grid(column=0, row=2)

# Eingabe Hub
stroke_value=tk.StringVar()
stroke=ttk.Entry(way_frame, textvariable=stroke_value)
stroke.grid(column=0, row=3)

#voreilend,  oder rückziehend
info_label2 = ttk.Label(way_frame, text=" 90° / Vor / Rück")
info_label2.grid(column=0, row=4)


#oberer Winkel vor_zurück
forward_back_value=tk.StringVar()
forward_back = ttk.Entry(way_frame, textvariable=forward_back_value)
forward_back.grid(column=0, row=5)


result_button = ttk.Button(way_frame, text="SAW Fahrweg", command=math1)
result_button.grid(column=0, row=6)



#Reset Button plaziert, läuft noch nicht, rest okay!!!

#def reset_1():
    #reset_button.delete(0,"end")

#all_commands =  command=lambda:[reset_1()]
#reset_button = ttk.Button(root, text="Reset alle Werte" ,command= all_commands)
#reset_button.grid()


#Bild einfügen, Größen über Paint anpassen

from PIL import Image, ImageTk

image = Image.open('add.GIF')
python_image = ImageTk.PhotoImage(image)

image_label = tk.Label(pic_frame, image=python_image)
image_label.grid(column=0, row=0)


# ab hier zweites Programm angehängt

#Fenster Position;Name, Größe
showing = ttk.Label(angle_frame,text="SAW-Fahrweg")
showing.grid(column=2, row=0)

eingabefeld_wert=tk.StringVar()
eingabefeld=ttk.Entry(angle_frame, textvariable=eingabefeld_wert)
eingabefeld.grid(column=2, row=1)

info_label = ttk.Label(angle_frame, text="Hub")
info_label.grid(column=2, row=2)

eingabefel_wert=tk.StringVar()
eingabefel=ttk.Entry(angle_frame, textvariable=eingabefel_wert)
eingabefel.grid(column=2, row=3)

schaltf1 = ttk.Button(angle_frame, text="Schrägenwinkel ist:", command=math2)
schaltf1.grid(column=2, row=4)


root.mainloop()


