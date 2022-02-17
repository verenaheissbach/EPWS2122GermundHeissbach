from kvs import settings

if __name__ == "__main__":
    print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")

from tkinter import *


# Die folgende Funktion soll ausgeführt werden, wenn der Nutzer den Button Bestätigen anklickt
def button_action():
    # Validierung: keine leeren Felder
    if eingabefeld1.get() == "" or eingabefeld2.get() == "" or eingabefeld3.get() == "" or eingabefeld4.get() == "" or eingabefeld5.get() == "" or eingabefeld6.get() == "":
        submit_label.config(text="Bitte geben Sie alle Werte ein.", fg="red")
        return

    # Validierung: nur numerische Werte
    if not eingabefeld1.get().isdigit() or not eingabefeld2.get().isdigit() or not eingabefeld3.get().isdigit() or not eingabefeld4.get().isdigit() or not eingabefeld5.get().isdigit() or not eingabefeld6.get().isdigit():
        submit_label.config(text="Bitte geben Sie ausschließlich numerische Werte ein.", fg="red")
        return

    # Wasserstand Min Validierung
    if int(eingabefeld3.get()) < 25:
        eingabefeld3.delete(0, 'end')
        eingabefeld3.insert(0, "25")
    elif int(eingabefeld3.get()) > 55:
        eingabefeld3.delete(0, 'end')
        eingabefeld3.insert(0, "55")

    # Wasserstand Max Validierung
    if int(eingabefeld4.get()) < 35:
        eingabefeld4.delete(0, 'end')
        eingabefeld4.insert(0, "35")
    elif int(eingabefeld4.get()) > 55:
        eingabefeld4.delete(0, 'end')
        eingabefeld4.insert(0, "55")

    # Temperatur Min Validierung
    if int(eingabefeld5.get()) < 18:
        eingabefeld5.delete(0, 'end')
        eingabefeld5.insert(0, "18")
    elif int(eingabefeld5.get()) > 25:
        eingabefeld5.delete(0, 'end')
        eingabefeld5.insert(0, "25")

    # Temperatur Max Validierung
    if int(eingabefeld6.get()) < 23:
        eingabefeld6.delete(0, 'end')
        eingabefeld6.insert(0, "23")
    elif int(eingabefeld6.get()) > 35:
        eingabefeld6.delete(0, 'end')
        eingabefeld6.insert(0, "35")

    with open("kvs.py", "w") as file:
        data = "settings = {\n\t\"WATER_GPIO\": %s, \n\t\"WATER_CHANNEL\": %s, \n\t\"WATER_MIN\": %s, " \
               "\n\t\"WATER_MAX\": %s, \n\t\"TEMP_MIN\": %s, \n\t\"TEMP_MAX\": %s\n}" % (
                   eingabefeld1.get(), eingabefeld2.get(), eingabefeld3.get(), eingabefeld4.get(), eingabefeld5.get(),
                   eingabefeld6.get())
        file.seek(0)
        file.write(data)
        file.truncate()

    submit_label.config(text="Die Werte wurden erfolgreich angepasst.", fg="green")


fenster = Tk()
fenster.geometry("420x300")
fenster.title("Aquaponik Überwachungssystem")

# Anweisungslabel
start_lable = Label(fenster, text="Willkommen im Aquaponik-Überwachungssystem.\n Bitte lege die folgenden Werte fest:")
my_lable1 = Label(fenster, text="Wasser GPIO: ")
my_lable2 = Label(fenster, text="Wasser Kanal: ")
my_lable3 = Label(fenster, text="Wasserstand Minimum [cm]: ")
my_lable4 = Label(fenster, text="Wasserstand Maximum [cm]: ")
my_lable5 = Label(fenster, text="Temperatur Minimum [°C]: ")
my_lable6 = Label(fenster, text="Temperatur Maximum [°C]: ")

# Bestätigungslabel nach einer Eingabe und Bestätigung des Nutzers
submit_label = Label(fenster)

# Hier kann der Nutzer eine Eingabe machen
eingabefeld1 = Entry(fenster, bd=5, width=5)
eingabefeld2 = Entry(fenster, bd=5, width=5)
eingabefeld3 = Entry(fenster, bd=5, width=5)
eingabefeld4 = Entry(fenster, bd=5, width=5)
eingabefeld5 = Entry(fenster, bd=5, width=5)
eingabefeld6 = Entry(fenster, bd=5, width=5)

# Default-Werte aus dem Key-Value-Store übernehmen
eingabefeld1.delete(0, 'end')
eingabefeld1.insert(0, settings['WATER_GPIO'])
eingabefeld2.delete(0, 'end')
eingabefeld2.insert(0, settings['WATER_CHANNEL'])
eingabefeld3.delete(0, 'end')
eingabefeld3.insert(0, settings['WATER_MIN'])
eingabefeld4.delete(0, 'end')
eingabefeld4.insert(0, settings['WATER_MAX'])
eingabefeld5.delete(0, 'end')
eingabefeld5.insert(0, settings['TEMP_MIN'])
eingabefeld6.delete(0, 'end')
eingabefeld6.insert(0, settings['TEMP_MAX'])

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
eingabefeld6.grid(row=6, column=1)

submit_button.grid(row=7, column=0)
submit_label.grid(row=8, column=0, columnspan=8)

# Ereignisschleife, warten auf Eingabe des Nutzers
mainloop()
