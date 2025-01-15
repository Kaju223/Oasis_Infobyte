import tkinter as tk
import random
import string
import pyperclip


def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ''

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def on_generate_button_click():
    length = int(password_length_entry.get())
    use_letters = letter_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    password = generate_password(length, use_letters, use_digits, use_symbols)
    password_result_var.set(password)

    # Copy the password to clipboard
    pyperclip.copy(password)


# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Define variables for checkboxes
letter_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

# Password length input
tk.Label(root, text="Enter password length:").grid(row=0, column=0)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=0, column=1)

# Character type checkboxes
tk.Checkbutton(root, text="Include letters", variable=letter_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(root, text="Include digits", variable=digit_var).grid(row=2, column=0, sticky='w')
tk.Checkbutton(root, text="Include symbols", variable=symbol_var).grid(row=3, column=0, sticky='w')

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.grid(row=4, column=0, columnspan=2)

# Display result
tk.Label(root, text="Generated Password:").grid(row=5, column=0, sticky='w')
password_result_var = tk.StringVar()
tk.Entry(root, textvariable=password_result_var, state='readonly', width=40).grid(row=5, column=1)

# Run the application
root.mainloop()
