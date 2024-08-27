import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def Calculate():
    try:
        height = float(heightInput.get("1.0", tk.END).strip())
        weight = float(weightInput.get("1.0", tk.END).strip())
        
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        
        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)
        output.config(text='BMI: {:.2f}'.format(bmi))
    except ValueError as e:
        output.config(text=str(e))
    

    

    # Dodaj kod do obliczeń BMI

root = ttk.Window('Kalkulator BMI')
root.geometry('600x600')
root.resizable(0, 0)

heightAndWeightInput = ttk.Frame(root)
heightAndWeightInput.columnconfigure(0, weight=1)
heightAndWeightInput.columnconfigure(1, weight=1)
heightAndWeightInput.pack(padx=10, pady=20, fill='x')

ttk.Label(heightAndWeightInput, text='Height input(cm):', font=('Arial', 24, 'bold')).grid(row=0, column=0)
heightInput = ttk.Text(heightAndWeightInput, height=1, width=10, font=('Arial', 24, 'bold'))
heightInput.grid(row=1, column=0)

ttk.Label(heightAndWeightInput, text='Weight input(kg):', font=('Arial', 24, 'bold')).grid(row=0, column=1)
weightInput = ttk.Text(heightAndWeightInput, height=1, width=10, font=('Arial', 24, 'bold'))
weightInput.grid(row=1, column=1)

calculateButton = tk.Button(root, text='Calculate BMI', command=Calculate)
calculateButton.config(font=('Arial', 14, 'bold'), height=2, width=15)
calculateButton.pack(side='top')

output = ttk.Label(root, text='')
output.pack()

root.mainloop()
