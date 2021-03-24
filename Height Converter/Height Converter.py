from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Feet to Meter")
window.configure(background="lightgreen")
window.geometry("400x400")
window.resizable(width=False, height=False)

ft_lbl = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

mt_lbl = Label(window, text="Meter", bg="purple", fg="white", width=14)
mt_lbl.grid(column=0, row=1, padx=15, pady=15)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=ft_value, width=14)
mt_entry.grid(column=1, row=1)
mt_entry.delete(0, 'end')

convert_btn = Button(window, text="Convert", bg="blue",
                     fg="white", width=14, command="")
convert_btn.grid(column=0, row=3, padx=15)

window.mainloop()
