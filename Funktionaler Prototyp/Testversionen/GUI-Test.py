if __name__ == "__main__":
	print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")



#Tutorial https://pythonbuch.com/gui.html
from tkinter import *


#Die folgende Funktion soll ausgeführt werden, wenn der Nutzer den Button Klick me anklickt
def button_action():
    entry_text = eingabefeld.get()
    if(entry_text == ""):
        welcome_label.config(text ="Bitte einen Wert eingeben.")
    else:
        entry_text = "Der Wert wurde erfolgreich angepasst: " + entry_text
        welcome_label.config(text=entry_text)

fenster = Tk()
fenster.title("Aquaponik Überwachungssystem")

#Anweisungslabel
start_lable = Label(fenster, text="Wilkommen im Aquaponik-Überwachungssystem. Bitte lege die folgenden Werte fest")
my_lable = Label(fenster, text="Wasserstandswert Min. [cm]: ")
my_lable1 = Label(fenster, text="Wasserstandswert Max. [cm]: ")
my_lable2 = Label(fenster, text="Temperatur Minimum [°C]: ")
my_lable3 = Label(fenster, text="Temperatur Maximum [°C]: ")

#In diesem Label wird nach dem Klick auf den Button der Nutzer mit seinem eingegebenen Namen begrüßt
welcome_label = Label(fenster)

#Hier kann der Nutzer eine Eingabe machen
eingabefeld = Entry(fenster, bd=5, width=5)
eingabefeld2 = Entry(fenster, bd=5, width=5)
eingabefeld3 = Entry(fenster, bd=5, width=5)
eingabefeld4 = Entry(fenster, bd=5, width=5)


welcome_button = Button(fenster, text="Bestätigen", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)
measure_button = Button(fenster, text="Messung starten",command=fenster.quit)

#Nun fügen wir die Komponenten unserem Fenster hinzu
start_lable.grid(row=0, column=0)

my_lable.grid(row=1, column=0)
eingabefeld.grid(row=1, column=1)
my_lable1.grid(row=2, column=0)
eingabefeld2.grid(row=2, column=1)
my_lable2.grid(row=3, column=0)
eingabefeld3.grid(row=3,column=1)
my_lable3.grid(row=4, column=0)
eingabefeld4.grid(row=4, column=1)

measure_button.grid(row=6, column=0)
welcome_button.grid(row=5, column=1)
exit_button.grid(row=6, column=1)
welcome_label.grid(row=7, column= 0, columnspan=7)

mainloop()
