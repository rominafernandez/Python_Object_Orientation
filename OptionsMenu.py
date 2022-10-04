## Exercise 14 - Options Menu

# Create three Menus
# Two should contain at least seven colors
# One should contain at least seven protein names
# Use functions to change the background color, the text
# color of a Label and the text displayed in that Label
# corresponding to the chosen Option.

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.geometry("500x100")
menu_frame = tk.Frame(root)
label_frame = tk.Frame(root)

# font sizes
normal_font = font.Font(size = 15)

# define VarVars
bg_col = tk.StringVar()
bg_col.set("snow")
text_col = tk.StringVar()
text_col.set("gray1")
protein1 = tk.StringVar()
protein1.set("IRF1")

# define functions
def change_bgcolor(choice):
    label_protein.config(bg=bg_col.get())

def change_text_color(choice):
    label_protein.config(fg=text_col.get())

def change_text(choice):
    label_protein.config(text=protein1.get())

# define labels
label_protein = tk.Label(root, text = protein1.get(), bg = bg_col.get(), fg = text_col.get(), font = normal_font, bd = 15, width = 40)
label_space = tk.Label(root, text="")
label_bgcol = tk.Label(label_frame, text = "Background Color", width = 20)
label_textcol = tk.Label(label_frame, text = "Text Color", width = 20)
label_protein_title = tk.Label(label_frame, text = "Protein", width = 20)

# menu
colors = ["gray1","snow","dark green","steel blue","dark violet","hot pink","gray","yellow"]
proteins = ["IRF1","PRDM1","GP130","MAPK","Actin","SERPNB2","IL6"]

menu_bgcolor = tk.OptionMenu(menu_frame, bg_col, *colors, command = change_bgcolor)
menu_bgcolor.config(width = 15)

menu_text_color = tk.OptionMenu(menu_frame, text_col, *colors, command = change_text_color)
menu_text_color.config(width = 15)

menu_proteins = tk.OptionMenu(menu_frame, protein1, *proteins, command = change_text)
menu_proteins.config(width = 15)

# Canvas
label_frame.pack(side = "top")
label_bgcol.pack(side = "left")
label_textcol.pack(side = "left")
label_protein_title.pack(side = "left")

menu_frame.pack(side = "top")
menu_bgcolor.pack(side = "left")
menu_text_color.pack(side = "left")
menu_proteins.pack(side = "left")
label_space.pack()
label_protein.pack()

root.mainloop()
