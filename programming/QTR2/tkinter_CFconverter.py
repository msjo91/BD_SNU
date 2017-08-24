from tkinter import Tk, ttk, StringVar

# Parent window
root = Tk()

# Title
root.title("Celsius to Fahrenheit")

# ttk.Frame()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

# Variables
celsius = StringVar()
fahrenheit = StringVar()

# ttk.Entry()
cel_entry = ttk.Entry(mainframe, width=7, textvariable=celsius)
cel_entry.grid(column=2, row=1)

# Labeling
ttk.Label(mainframe, text="Celsius").grid(column=3, row=1)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2)
ttk.Label(mainframe, textvariable=fahrenheit).grid(column=2, row=2)
ttk.Label(mainframe, text="Fahrenheit").grid(column=3, row=2)


# Calculate command function
def calculate(*args):
    try:
        val = float(celsius.get())
        fahrenheit.set(val * 9 / 5 + 32)
    except ValueError:
        pass


# Button command
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3)

# Give padding to each child
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Receive all keyboard events until other window gets the focus
cel_entry.focus()

# Bind
root.bind('<Return>', calculate)

root.mainloop()
