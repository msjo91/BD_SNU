from tkinter import Tk, ttk, StringVar, PhotoImage, END
from tkinter.messagebox import showinfo

# Parent window and title
root = Tk()
root.title("profile")

# ttk.Frame()
frame = ttk.Frame(root)
# Same as "frame = ttk.Frame(root, padding=(5, 10), borderwidth=2, relief=SUNKEN)"
frame['padding'] = (5, 10)
frame['borderwidth'] = 2
frame['relief'] = 'sunken'
frame.pack()

tmp_btn = ttk.Button(frame, text="Temp Button")
tmp_btn.pack()

# ttk.Label()
content = StringVar()
label1 = ttk.Label(root, text="Full name")
label1['textvariable'] = content
content.set("New value to display")
label1.pack()

# PhotoImage()
label2 = ttk.Label(root)
image = PhotoImage(file="wiggle.gif")
label2['image'] = image
label2.pack()


# Button command function
def hello():
    showinfo("Hello", "It's me, {}".format(name.get()))
    content.set(name.get())


# ttk.Button()
btn = ttk.Button(root, text="Introduction", command=hello)
btn.pack()


# Placeholder event handler
def clear_entry(event, entry):
    """Unfortunately, this will remove whatever is inserted."""
    entry.delete(0, END)


# Placeholder text
placeholder = "Insert name"

# ttk.Entry()
username = StringVar()
name = ttk.Entry(root, textvariable=username)
name.insert(0, placeholder)

# Bind event handler (Click then remove text)
name.bind("<Button-1>", lambda event: clear_entry(event, name))
name.pack(pady=5)

# ttk.Radiobutton()
location = StringVar()
home = ttk.Radiobutton(text="Home", variable=location, value="Home")
school = ttk.Radiobutton(text="School", variable=location, value="School")
library = ttk.Radiobutton(text="Library", variable=location, value="Library")
home.pack()
school.pack()
library.pack()

# ttk.Combobox()
address_var = StringVar()
address = ttk.Combobox(root, textvariable=address_var)
address.bind('<<ComboboxSelected>>')
address.set("Region")
address['values'] = ('서울', '경기', '경상', '전라', '충청', '강원', '제주')
address.pack()

root.mainloop()
