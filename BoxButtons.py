## Exercise 16 - Radio Buttons

# Create two GUIs
# One with normal Radio Buttons
# One with a Button Box
# Each should contain at least six Radio Buttons
# Create a Function that is coupled with the Buttons for each GUI

import tkinter as tk
import tkinter.font as font

# frames
root = tk.Tk()
root.geometry("500x150")
frame_radiob = tk.Frame(root)

# font
normal_font = font.Font(size = 10)
header_font = font.Font(size = 15)

# functions
def changeLan():
    lan = var_lan.get()
    if lan == "german":
        radio_german.config(text = "Deutsch")
        radio_english.config(text = "Englisch")
        radio_spanish.config(text = "Spanisch")
        radio_french.config(text = "Französisch")
        radio_danish.config(text = "Dänisch")
        radio_italian.config(text = "Italienisch")
        label_header.config(text = "Bitte wähle eine Sprache aus")
    elif lan == "english":
        radio_german.config(text = "German")
        radio_english.config(text = "English")
        radio_spanish.config(text = "Spanish")
        radio_french.config(text = "French")
        radio_danish.config(text = "Danish")
        radio_italian.config(text = "Italian")
        label_header.config(text = "Please select a language")
    elif lan == "spanish":
        radio_german.config(text = "Alemán")
        radio_english.config(text = "Inglés")
        radio_spanish.config(text = "Español")
        radio_french.config(text = "Francés")
        radio_danish.config(text = "Danés")
        radio_italian.config(text = "Italiano")
        label_header.config(text = "Por favor, seleccione un idioma")
    elif lan == "french":
        radio_german.config(text = "Allemand")
        radio_english.config(text = "Anglais")
        radio_spanish.config(text = "Espagnol")
        radio_french.config(text = "Français")
        radio_danish.config(text = "Danois")
        radio_italian.config(text = "Italien")
        label_header.config(text = "Veuillez choisir une langue")
    elif lan == "danish":
        radio_german.config(text = "Tysk")
        radio_english.config(text = "Engelsk")
        radio_spanish.config(text = "Spansk")
        radio_french.config(text = "Fransk")
        radio_danish.config(text = "Dansk")
        radio_italian.config(text = "Italiensk")
        label_header.config(text = "Vælg venligst et sprog")
    elif lan == "italian":
        radio_german.config(text = "Tedesco")
        radio_english.config(text = "Inglese")
        radio_spanish.config(text = "Spagnolo")
        radio_french.config(text = "Francese")
        radio_danish.config(text = "Danese")
        radio_italian.config(text = "Italiano")
        label_header.config(text = "Selezionare una lingua")

# variables
var_lan = tk.StringVar()
var_lan.set("English")

# radio buttons
radio_german = tk.Radiobutton(frame_radiob, text = "German", variable = var_lan, value = "german", command = changeLan, font = normal_font, indicator = 0, width = 15)
radio_english = tk.Radiobutton(frame_radiob, text = "English", variable = var_lan, value = "english", command = changeLan, font = normal_font, indicator = 0, width = 15)
radio_spanish = tk.Radiobutton(frame_radiob, text = "Spanish", variable = var_lan, value = "spanish", command = changeLan, font = normal_font, indicator = 0, width = 15)
radio_french = tk.Radiobutton(frame_radiob, text = "French", variable = var_lan, value = "french", command = changeLan, font = normal_font, indicator = 0, width = 15)
radio_danish = tk.Radiobutton(frame_radiob, text = "Danish", variable = var_lan, value = "danish", command = changeLan, font = normal_font, indicator = 0, width = 15)
radio_italian = tk.Radiobutton(frame_radiob, text = "Italian", variable = var_lan, value = "italian", command = changeLan, font = normal_font, indicator = 0, width = 15)

# labels
label_header = tk.Label(root, text = "Please select a language", font = header_font, width = 40)

# First Canvas
label_header.pack()
frame_radiob.pack(anchor = "n")
radio_german.pack(anchor = "w")
radio_english.pack(anchor = "w")
radio_spanish.pack(anchor = "w")
radio_french.pack(anchor = "w")
radio_danish.pack(anchor = "w")
radio_italian.pack(anchor = "w")

root.mainloop()
