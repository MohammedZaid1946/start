import math
import tkinter as tk
from tkinter import Label, Entry, Button

def calculate():
    f = float(entry_f.get())
    s = float(entry_s.get())
    t = float(entry_t.get())

    result = math.asin(math.sqrt(((f)**2) - ((s)**2)) / (t))
    h = math.degrees(result)
    d = (math.sqrt((f)**2 - (s)**2) / (t))

    result_label.config(text="Acceptance angle: " + str(h))
    numerical_aperture_label.config(text="Numerical Aperture: " + str(d))

# Create the main window
app = tk.Tk()
app.title("Simple App")

# Create input labels and entry widgets
Label(app, text="Enter Core refractive index (n1) value:").grid(row=0, column=0)
entry_f = Entry(app)
entry_f.grid(row=0, column=1)

Label(app, text="Enter Cladding refractive index (n2) value:").grid(row=1, column=0)
entry_s = Entry(app)
entry_s.grid(row=1, column=1)

Label(app, text="Enter n0 value:").grid(row=2, column=0)
entry_t = Entry(app)
entry_t.grid(row=2, column=1)

# Create a button to trigger the calculation
calculate_button = Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Create labels to display the results
result_label = Label(app, text="Ans: ")
result_label.grid(row=4, column=0, columnspan=2)

numerical_aperture_label = Label(app, text="Numerical Aperture: ")
numerical_aperture_label.grid(row=5, column=0, columnspan=2)

# Start the main loop
app.mainloop()
