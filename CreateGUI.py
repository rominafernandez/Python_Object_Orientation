## Exercise 11 - Creating Labels

# Create a GUI that contains three different Labels
# Please use texts with a biological or biochemical background, we will need these labels later

import tkinter as tk
import random

root = tk.Tk()
label_intro = tk.Label(root, text = "Welcome to the random display program", font = 20, bd = 20)
label_intro.pack()
label_description = tk.Label(root, text = "Here you can see different Proteins")
label_description.pack()
label_prot1 = tk.Label(root, text = "Protein = PRDM1", width = 20, anchor = "w")
label_prot1.pack()
label_input = tk.Label(root, text = "Enter a new Protein:", pady = 5)

## Exercise 12 - Using Buttons

# Use your GUI from Exercise 11 and add two Buttons to it
# Each Button should change the text in one of your three-pre-defined labels
proteins = ["PRDM1", "IRF1", "IL6", "MAPK", "Actin"]
organisms = ["Homo sapiens", "Mus Musculus", "Canis lupus"]

def ChangeProt():
    item = random.choice(proteins)
    value = label_prot1["text"].split()
    while item == value[2]:
        item = random.choice(proteins)
    label_prot1.config(text = f"Protein = {item}")

def ChangeOrganism():
    item = random.choice(organisms)
    value = label_prot1["text"].split()
    while item == value[2]:
        item = random.choice(organisms)
    label_prot1.config(text = f"Organism = {item}")

def ChangeDisplay():
    if button3["text"] == "Protein -> Organism":
        label_description.config(text="Here you can see different Organisms")
        label_prot1.config(text="Organism = Homo sapiens", width = 25)
        button2.config(text="Change the Organism", command = ChangeOrganism)
        button3.config(text="Organism -> Protein")
        button4.config(command=AddOrganism)
        label_input.config(text="Enter a new Organism:")
    elif button3["text"] == "Organism -> Protein":
        label_description.config(text="Here you can see different Proteins")
        label_prot1.config(text="Protein = PRDM1", width = 20)
        button2.config(text="Change the Protein", command = ChangeProt)
        button3.config(text="Protein -> Organism")
        button4.config(command=AddProtein)
        label_input.config(text="Enter a new Protein:")

def AddProtein():
    if input1.get() != "":
        proteins.append(input1.get())
    edit1.delete(0, tk.END)

def AddOrganism():
    if input1.get() != "":
        organisms.append(input1.get())
    edit1.delete(0, tk.END)



button1 = tk.Button(root, text="Close", command = root.destroy)
button2 = tk.Button(root, text="Change the Protein", command = ChangeProt)
button3 = tk.Button(root, text="Protein -> Organism", command = ChangeDisplay)
input1 = tk.StringVar()
edit1 = tk.Entry(root, textvariable = input1, highlightcolor = "white")
button4 = tk.Button(root, text="Submit", command = AddProtein)


button2.pack()
label_input.pack()
edit1.pack()
button4.pack()
button3.pack()
button1.pack()


root.mainloop()
