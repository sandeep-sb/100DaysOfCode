import tkinter


# Function to calculate km from miles
def calculate_km():
    miles = float(user_input.get())
    km_from_miles = round(miles * 1.609, 2)
    converted_label.config(text=f"{km_from_miles}")


window = tkinter.Tk()
window.title("miles-to-km-convertor")
window.config(padx=100, pady=100)

# Entry point
user_input = tkinter.Entry()
user_input.grid(row=0, column=1)

# Label 1 for miles
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

# Label 2 for equality
equal_label = tkinter.Label(text="is equal to ")
equal_label.grid(row=1, column=0)

# Label 3 for converted value
converted_label = tkinter.Label(text="0")
converted_label.grid(row=1, column=1)

# Label 4 for Km
km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

# Button for conversion
button = tkinter.Button(text="calculate", command=calculate_km)
button.grid(row=2, column=1)

window.mainloop()
