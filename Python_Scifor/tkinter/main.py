import tkinter as tk

def submit():
  print("Name of Candidate: ", name_entry.get())
  print("Age of Candidate: ", age_entry.get())
  print("Gender of Candidate: ", gender.get())
  print("Address: ", address_entry.get())
  print("Email Address: ", email_entry.get())
  print("Country:", Country_entry.get())
  print("State: ", state_entry.get())
  print("Diseases:")
  if cold_var.get():
    print(" Cold")
  if cough_var.get():
    print(" Cough")
  if fever_var.get():
    print(" Fever")
  if headache_var.get():
    print(" Headache")
  print("Form submitted!")


window = tk.Tk()
window.title("Covid-19 Vaccine Registration")


name_label = tk.Label(window, text="Name:")
name_label.grid(row=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

age_label = tk.Label(window, text="Age:")
age_label.grid(row=1)
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1)

gender = tk.StringVar()
gender_label = tk.Label(window,text="Gender")
gender_label.grid(row=2)
tk.Radiobutton(window,text="Male",variable=gender ,value="Male").grid(row=2,column=0)
tk.Radiobutton(window,text="Female",variable=gender ,value="Female").grid(row=2,column=1)

address_label = tk.Label(window, text="Address:")
address_label.grid(row=3)
address_entry = tk.Entry(window)
address_entry.grid(row=3, column=1)

email_label = tk.Label(window, text="Email:")
email_label.grid(row=4)
email_entry = tk.Entry(window)
email_entry.grid(row=4, column=1)

country_label = tk.Label(window, text="Country:")
country_label.grid(row=5)
Country_entry = tk.Entry(window)
Country_entry.grid(row=5, column=1)

state_label = tk.Label(window, text="State:")
state_label.grid(row=6)
state_entry = tk.Entry(window)
state_entry.grid(row=6, column=1)

disease_label = tk.Label(window,text="Do you have Any of these diseases: ")
disease_label.grid(row=7)
cold_var = tk.BooleanVar()
cold_check = tk.Checkbutton(window, text="Cold", variable=cold_var)
cold_check.grid(row=8, column=0)

cough_var = tk.BooleanVar()
cough_check = tk.Checkbutton(window, text="Cough", variable=cough_var)
cough_check.grid(row=8, column=1)

fever_var = tk.BooleanVar()
fever_check = tk.Checkbutton(window, text="Fever", variable=fever_var)
fever_check.grid(row=9, column=0)

headache_var = tk.BooleanVar()
headache_check = tk.Checkbutton(window, text="Headache", variable=headache_var)
headache_check.grid(row=9, column=1)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=10, columnspan=2)

output_widget = tk.Listbox(window)
output_widget.grid(row=12, columnspan=2)


window.mainloop()

