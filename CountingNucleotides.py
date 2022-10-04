## Group Exercise 2 - Counting Nucleotides

# Create a GUI that allows the user to input a nucleotide sequence and get the number of:
# Guanine
# Adenine
# Cytosine
# Thymine
# Uracil
# Associate each nucleotide with its own button and label

import tkinter as tk
import re
import tkinter.font as font

root = tk.Tk()
root.title("Nucleotide Counter")
# frame for buttons and output
A_frame = tk.Frame(root)
C_frame = tk.Frame(root)
T_frame = tk.Frame(root)
G_frame = tk.Frame(root)
U_frame = tk.Frame(root)
input_frame = tk.Frame(root)

# font sizes
header_font = font.Font(size = 25)
normal_font = font.Font(size = 15)

# Defining functions
def CountAll():
    if re.search("^[A,C,T,G,U]+$", input_sequence.get()):
        A = input_sequence.get().count("A")
        C = input_sequence.get().count("C")
        T = input_sequence.get().count("T")
        G = input_sequence.get().count("G")
        U = input_sequence.get().count("U")
        label_A.config(text = f"A = {A}")
        label_C.config(text = f"C = {C}")
        label_G.config(text = f"G = {G}")
        label_T.config(text = f"T = {T}")
        label_U.config(text = f"U = {U}")
        label_error.config(text = "")
    else:
        label_error.config(text = "Invalid Input!")
        label_A.config(text = "")
        label_C.config(text = "")
        label_G.config(text = "")
        label_T.config(text = "")
        label_U.config(text = "")

def CountA():
    if re.search("^[A,C,T,G,U]+$", input_sequence.get()):
        A = input_sequence.get().count("A")
        label_A.config(text = f"A = {A}")
        label_C.config(text = "")
        label_G.config(text = "")
        label_T.config(text = "")
        label_U.config(text = "")
        label_error.config(text = "")

def CountC():
    if re.search("^[A,C,T,G,U]+$", input_sequence.get()):
        C = input_sequence.get().count("C")
        label_A.config(text = "")
        label_C.config(text = f"C = {C}")
        label_G.config(text = "")
        label_T.config(text = "")
        label_U.config(text = "")
        label_error.config(text = "")

def CountT():
    if re.search("^[A,C,T,G,U]+$", input_sequence.get()):
        T = input_sequence.get().count("T")
        label_A.config(text = "")
        label_C.config(text = "")
        label_G.config(text = "")
        label_T.config(text = f"T = {T}")
        label_U.config(text = "")
        label_error.config(text = "")

def CountG():
    if re.search("^[A,C,T,G,U]+$", input_sequence.get()):
        G = input_sequence.get().count("G")
        label_A.config(text = "")
        label_C.config(text = "")
        label_G.config(text = f"G = {G}")
        label_T.config(text = "")
        label_U.config(text = "")
        label_error.config(text = "")

def CountU():
    if re.search("^[A,C,T,G,U]+$", input_sequence.get()):
        U = input_sequence.get().count("U")
        label_A.config(text = "")
        label_C.config(text = "")
        label_G.config(text = "")
        label_T.config(text = "")
        label_U.config(text = f"U = {U}")
        label_error.config(text = "")

def DelEntry():
    entry_sequence.delete(0, tk.END)


# Creating necessary Labels
label_header = tk.Label(root, text = "Nucleotide Counter", bd = 35, font = header_font)
label_input = tk.Label(root, text = "Enter your nucleotide sequence", font = normal_font)
label_error = tk.Label(root, font = normal_font)
label_A = tk.Label(A_frame, font = normal_font, width = 10, anchor = "w")
label_C = tk.Label(C_frame, font = normal_font, width = 10, anchor = "w")
label_T = tk.Label(T_frame, font = normal_font, width = 10, anchor = "w")
label_G = tk.Label(G_frame, font = normal_font, width = 10, anchor = "w")
label_U = tk.Label(U_frame, font = normal_font, width = 10, anchor = "w")


# Creating entry fields
input_sequence = tk.StringVar()
entry_sequence = tk.Entry(input_frame, textvariable = input_sequence, font = normal_font)
entry_sequence.insert(0,"ACTGU")

# Creating Buttons
button_all = tk.Button(root, text = "Count All", command = CountAll, font = normal_font)
button_a = tk.Button(A_frame, text = "Count A", command = CountA, font = normal_font)
button_c = tk.Button(C_frame, text = "Count C", command = CountC, font = normal_font)
button_t = tk.Button(T_frame, text = "Count T", command = CountT, font = normal_font)
button_g = tk.Button(G_frame, text = "Count G", command = CountG, font = normal_font)
button_u = tk.Button(U_frame, text = "Count U", command = CountU, font = normal_font)
button_del = tk.Button(input_frame, text = "Clear", command = DelEntry, font = normal_font)

# packing everyting on the canvas
label_header.pack()
label_input.pack()
input_frame.pack()
entry_sequence.pack(side = "left")
button_del.pack(side = "left")
label_error.pack()

button_all.pack()

A_frame.pack()
button_a.pack(side = "left")
label_A.pack(side = "left")

C_frame.pack()
button_c.pack(side = "left")
label_C.pack(side = "left")

G_frame.pack()
button_g.pack(side = "left")
label_G.pack(side = "left")

T_frame.pack()
button_t.pack(side = "left")
label_T.pack(side = "left")

U_frame.pack()
button_u.pack(side = "left")
label_U.pack(side = "left")

root.mainloop()
