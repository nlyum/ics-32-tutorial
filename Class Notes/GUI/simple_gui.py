# our goal is to learn event-based programming!
# in event-based programming, we have three entities:

# 1) The event - such as clicking a button, hovering over text, 
# 2) The event source - such as the button
# 3) The event handler - the function that is called when the event occurs


import tkinter as tk

def my_click():
    textbox.insert(tk.END, "something!")


root = tk.Tk()

root.geometry("500x500") # setting the size of the window

root.title("My First GUI") # set the title

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 18)) # widgets
textbox.pack(padx=10)

button = tk.Button(root, text="click me", command=my_click)
button.pack(padx=20)

root.mainloop()