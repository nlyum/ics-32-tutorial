import tkinter as tk

def create_window() -> None:
    window = tk.Tk()
    window.geometry("300x200")
    message = tk.Label(text="ICS32 Example GUI")
    message.pack()
    frame = tk.Frame(window, height = 200, width = 300)
    frame.bind("<Enter>", _on_enter)
    window.mainloop()

def _on_enter(event: tk.Event):
    print(f"Mouse entered window at position x = {event.x}, y = {event.y}")

if __name__ == "__main__":
    create_window()