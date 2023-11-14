import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = round(weight / (height ** 2), 2)
        result_label.config(text=f"Your BMI is: {bmi}")

        # Provide BMI suggestions
        if bmi < 18.5:
            suggestion = "Underweight - You may want to gain some weight."
        elif 18.5 <= bmi < 24.9:
            suggestion = "Normal weight - Keep it up!"
        elif 25 <= bmi < 29.9:
            suggestion = "Overweight - Consider losing some weight for better health."
        else:
            suggestion = "Obese - It's important to focus on a healthy lifestyle."

        suggestion_label.config(text=suggestion)

    except ValueError:
        result_label.config(text="Please enter valid values for weight and height.")
        suggestion_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place widgets
weight_label = ttk.Label(window, text="Enter Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = ttk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = ttk.Label(window, text="Enter Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = ttk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = ttk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

suggestion_label = ttk.Label(window, text="")
suggestion_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
window.mainloop()
