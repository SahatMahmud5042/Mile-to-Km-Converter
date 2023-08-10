import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

mi_label = tkinter.Label(text="Miles", font=("Arial", 16))
mi_label.grid(column=2, row=0)

km_label = tkinter.Label(text="is equal to", font=("Arial", 16))
km_label.grid(column=0, row=1)

km_val = tkinter.Label(text="0", font=("Arial", 16))
km_val.grid(column=1, row=1)

km_text = tkinter.Label(text="Km", font=("Arial", 16))
km_text.grid(column=2, row=1)


def to_km():
    mile = int(input.get())
    km = mile * 1.61
    km_val.config(text=km)


button = tkinter.Button(text="Calculate", command=to_km)
button.grid(column=1, row=2)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
