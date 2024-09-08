import tkinter as tk
def submit(name_entry, std_entry, caste_entry, email_entry):
    name = name_entry.get()
    std = std_entry.get()
    caste = caste_entry.get()
    email_id = email_entry.get()

    print("Form Submitted!")
    print(f"Name is {name}")
    print(f"Standard/grade: {std}")
    print(f"Caste: {caste}")
    print(f"Email ID: {email_id}")


root = tk.Tk()
root.title("School registration form!!")
root.config(bg="Green")

name = tk.Label(root, text="Name:")
name.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

std = tk.Label(root, text="Standard/grade:")
std.grid(row=1, column=0)

std_entry = tk.Entry(root)
std_entry.grid(row=1, column=1)

caste = tk.Label(root, text="Enter your caste:")
caste.grid(row=2, column=0)

caste_entry = tk.Entry(root)
caste_entry.grid(row=2, column=1)

email_id = tk.Label(root, text="Enter your email:")
email_id.grid(row=3, column=0)

email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=lambda: submit(name_entry, std_entry, caste_entry, email_entry))
submit_button.grid(row=4, columnspan=2)

root.mainloop()
