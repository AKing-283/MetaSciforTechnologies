import tkinter as tk

root = tk.Tk()
root.title("Filter concepts and lambda!!")
result_list = tk.Listbox(root)
result_list.pack()


def filter_display(data, filter_data):
    filtered_data = list(filter(filter_data, data))
    result_list.delete(0, tk.END)
    for i in filtered_data:
        result_list.insert(tk.END, i)


def filter_button(filter_data):
    button = tk.Button(root, text="Filter!!", command=lambda: filter_display(data, filter_data))
    button.pack()
    return button


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
filter_button(lambda x: x % 2 == 0)
filter_button(lambda x: x > 3)
root.mainloop()
