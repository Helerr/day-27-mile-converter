from tkinter import *


def convert_to_km():
    miles_converted = round(float(miles_input.get()) * 1.609)
    kilometer_result_label.config(text=f"{miles_converted}")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

GLOBAL_FONT = ("Arial", 12, "normal")

# textbox for user to input the amount of miles to be converted
miles_input = Entry(width=5, font=GLOBAL_FONT, justify="center")
miles_input.grid(row=0, column=1)
miles_input.insert(END, "0")

miles_label = Label(text="Miles", font=GLOBAL_FONT)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to", font=GLOBAL_FONT)
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0", font=GLOBAL_FONT)
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="Km", font=GLOBAL_FONT)
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=convert_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
