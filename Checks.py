## Exercise 15 - Checks

# Create a GUI with:
# 1 Button
# 5 Labels
# 5 Check Buttons
# On Button click the current status of the five Check Buttons should be displayed in the corresponding Label

import tkinter as tk
import tkinter.font as font

# frames
root = tk.Tk()
root.geometry("400x170")
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)

# font
normal_font = font.Font(size = 15)

# VarVars
value1 = tk.BooleanVar()
value1.set(False)
value2 = tk.BooleanVar()
value2.set(False)
value3 = tk.BooleanVar()
value3.set(False)
value4 = tk.BooleanVar()
value4.set(False)
value5 = tk.BooleanVar()
value5.set(False)
value_names = [value1, value2, value3, value4, value5]

# labels
label1 = tk.Label(frame1, font = normal_font, width = 7, anchor = "w")
label2 = tk.Label(frame2, font = normal_font, width = 7, anchor = "w")
label3 = tk.Label(frame3, font = normal_font, width = 7, anchor = "w")
label4 = tk.Label(frame4, font = normal_font, width = 7, anchor = "w")
label5 = tk.Label(frame5, font = normal_font, width = 7, anchor = "w")
label_names = [label1, label2, label3, label4, label5]

# functions
def check_status():
    counter = 0
    for i in value_names:
        status_check = i.get()
        if status_check:
            label_names[counter].config(text = f": True")
            counter+=1
        else:
            label_names[counter].config(text = f": False")
            counter+=1

# buttons
button_check = tk.Button(root, text = "Check Status", command = check_status, font = normal_font)

# check boxes
check1 = tk.Checkbutton(frame1, text = "Box 1", var = value1, font =normal_font)
check2 = tk.Checkbutton(frame2, text = "Box 2", var = value2, font =normal_font)
check3 = tk.Checkbutton(frame3, text = "Box 3", var = value3, font =normal_font)
check4 = tk.Checkbutton(frame4, text = "Box 4", var = value4, font =normal_font)
check5 = tk.Checkbutton(frame5, text = "Box 5", var = value5, font =normal_font)

# canvas
frame1.pack()
check1.pack(side = "left")
label1.pack(side = "left")

frame2.pack()
check2.pack(side = "left")
label2.pack(side = "left")

frame3.pack()
check3.pack(side = "left")
label3.pack(side = "left")

frame4.pack()
check4.pack(side = "left")
label4.pack(side = "left")

frame5.pack()
check5.pack(side = "left")
label5.pack(side = "left")

button_check.pack(side = "bottom")

root.mainloop()
