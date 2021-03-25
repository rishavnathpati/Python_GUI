from tkinter import Button, DoubleVar, Entry, IntVar, Label, StringVar, Tk


class TipCalulator:
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background="Blue")
        window.geometry("375x250")
        window.resizable(width=False, height=False)

        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percents = Label(window,
                             text="Tip Percentage",
                             bg="purple",
                             fg="white")
        tip_percents.grid(column=0, row=0, padx=15)

        bill_amount = Label(window, text="Bill Amount", bg="black", fg="white")
        bill_amount.grid(column=1, row=0, padx=15)

        window.mainloop()


TipCalulator()
