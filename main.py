from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def calculate(num):
    km = 1.609344 * num
    return km

def button_clicked():
    result = calculate(float(input.get()))
    result_label["text"] = f"{result}"

#label
label1 = Label(text="is equal to", font=("Arial", 24, "bold"))
label2 = Label(text="Miles", font=("Arial", 24, "bold"))
label3 = Label(text="Km", font=("Arial", 24, "bold"))
result_label = Label(text="0", font=("Arial", 24, "bold"))

label1.grid(column=0, row=1)
label2.grid(column=2, row=0)
label3.grid(column=2, row=1)
result_label.grid(column=1, row=1)


#Entry
input = Entry(width=10)
input.grid(column=1, row=0)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
