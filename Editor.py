## Exercise 13 - Text fields

# Create a GUI that consists of a text field, five buttons and two labels
# The Buttons should be able to:
# insert some text into your text field (one at the beginning and one at the end)
# clear the whole text field
# print out the text into the terminal
# display how many characters the current text has in a label
# The second label should be used to display which button was pressed
# last (just add a label2.config(text=“You pressed Button ...”) to your functions)

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title("Text Editor")

# frame for buttons and output
text_man_frame = tk.Frame(root)
count_frame = tk.Frame(root)


# font sizes
header_font = font.Font(size = 25)
normal_font = font.Font(size = 15)

# define functions
def InsertStart():
    label_button.config(text = "You pressed the button 'Insert Start'")
    text.insert(1.0, "Start\n")

def InsertEnd():
    label_button.config(text = "You pressed the button 'Insert end'")
    text.insert("end", "\nEnd")

def ClearText():
    label_button.config(text = "You pressed the button 'Clear'")
    text.delete(1.0, "end")
    label_count.config(text = "")

def PrintTerminal():
    label_button.config(text = "You pressed the button 'Print'")
    content = text.get(1.0, "end-1c")
    print(content)

def CountChar():
    label_button.config(text = "You pressed the button 'Count Characters'")
    label_count.config(text = f"Your text has {len(text.get(1.0, 'end-1c'))} characters")

# create text field
text = tk.Text(root, font = normal_font)

# create buttons
button_insert_start = tk.Button(text_man_frame, text = "Insert Start", font = normal_font, command = InsertStart)
button_insert_end = tk.Button(text_man_frame, text = "Insert End", font = normal_font, command = InsertEnd)
button_clear = tk.Button(text_man_frame, text = "Clear", font = normal_font, command = ClearText)
button_print = tk.Button(root, text = "Print", font = normal_font, command = PrintTerminal)
button_count = tk.Button(count_frame, text = "Count Characters", font = normal_font, command = CountChar)

# create labels
label_count = tk.Label(count_frame, font = normal_font, width = 30)
label_button = tk.Label(root, text = "You pressed no button yet", font = normal_font, width = 45)

# pack canvas
text.pack()
label_button.pack(side = "top")

text_man_frame.pack()
button_insert_start.pack(side = "left")
button_insert_end.pack( side = "left")
button_clear.pack(side = "left")

count_frame.pack()
button_count.pack(side = "left")
label_count.pack(side = "left")

button_print.pack()

root.mainloop()
