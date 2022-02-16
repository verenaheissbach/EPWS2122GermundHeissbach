from settings import settings

if __name__ == "__main__":
    print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")

from tkinter import *

# Die folgende Funktion soll ausgeführt werden, wenn der Nutzer den Button Bestätigen anklickt
def button_action():
    with open("kvs.py", "w") as file:
        data = "settings = {\n\t\"WATER_GPIO\": %s, \n\t\"WATER_CHANNEL\": %s, \n\t\"WATER_MIN\": %s, " \
               "\n\t\"WATER_MAX\": %s, \n\t\"WATERING_TIME\": %s, \n\t\"TEMP_MAX\": %s, \n\t\"TEMP_MIN\": %s\n}" % (
                   eingabefeld1.get(), eingabefeld2.get(), eingabefeld3.get(), eingabefeld4.get(), eingabefeld5.get(),
                   eingabefeld6.get(), eingabefeld7.get())
        file.seek(0)
        file.write(data)
        file.truncate()

    submit_label.config(text="Die Werte wurden erfolgreich angepasst.")


fenster = Tk()
fenster.geometry("410x280")
fenster.title("Aquaponik Überwachungssystem")

# Anweisungslabel
start_lable = Label(fenster, text="Willkommen im Aquaponik-Überwachungssystem.\n Bitte lege die folgenden Werte fest:")
my_lable1 = Label(fenster, text="Wasser GPIO: ")
my_lable2 = Label(fenster, text="Wasser Kanal: ")
my_lable3 = Label(fenster, text="Wasserstand Minimum [cm]: ")
my_lable4 = Label(fenster, text="Wasserstand Maximum [cm]: ")
my_lable5 = Label(fenster, text="Bewässerungszeit [s]: ")
my_lable6 = Label(fenster, text="Temperatur Minimum [°C]: ")
my_lable7 = Label(fenster, text="Temperatur Maximum [°C]: ")

# Bestätigungslabel nach einer Eingabe und Bestätigung des Nutzers
submit_label = Label(fenster)

# Hier kann der Nutzer eine Eingabe machen
eingabefeld1 = Entry(fenster, bd=5, width=5)
eingabefeld2 = Entry(fenster, bd=5, width=5)
eingabefeld3 = Entry(fenster, bd=5, width=5)
eingabefeld4 = Entry(fenster, bd=5, width=5)
eingabefeld5 = Entry(fenster, bd=5, width=5)
eingabefeld6 = Entry(fenster, bd=5, width=5)
eingabefeld7 = Entry(fenster, bd=5, width=5)

# Default-Werte aus dem Key-Value-Store übernehmen
eingabefeld1.insert(0, settings['WATER_GPIO'])
eingabefeld2.insert(0, settings['WATER_CHANNEL'])
eingabefeld3.insert(0, settings['WATER_MIN'])
eingabefeld4.insert(0, settings['WATER_MAX'])
eingabefeld5.insert(0, settings['WATERING_TIME'])
eingabefeld6.insert(0, settings['TEMP_MIN'])
eingabefeld7.insert(0, settings['TEMP_MAX'])

# Erstellen der Buttons
submit_button = Button(fenster, text="Bestätigen", command=button_action)

# Hinzufügen der Komponenten in das Fenster
start_lable.grid(row=0, column=0)

my_lable1.grid(row=1, column=0)
eingabefeld1.grid(row=1, column=1)
my_lable2.grid(row=2, column=0)
eingabefeld2.grid(row=2, column=1)
my_lable3.grid(row=3, column=0)
eingabefeld3.grid(row=3, column=1)
my_lable4.grid(row=4, column=0)
eingabefeld4.grid(row=4, column=1)
my_lable5.grid(row=5, column=0)
eingabefeld5.grid(row=5, column=1)
my_lable6.grid(row=6, column=0)
eingabefeld6.grid(row=5, column=1)
my_lable7.grid(row=6, column=0)
eingabefeld7.grid(row=6, column=1)

submit_button.grid(row=7, column=0)
submit_label.grid(row=8, column=0, columnspan=8)

# Ereignisschleife, warten auf Eingabe des Nutzers
mainloop()
