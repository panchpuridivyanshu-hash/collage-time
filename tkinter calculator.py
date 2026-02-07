import tkinter as tk

# Function to update expression in the entry box
def press(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate the final expression
def equal():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error")

# Function to clear the entry
def clear():
    entry_text.set("")

# Main GUI window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

# Entry box
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=equal)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col, sticky="nsew")

# Clear Button
clear_btn = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Make rows and columns expandable
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Run the main loop
root.mainloop()
