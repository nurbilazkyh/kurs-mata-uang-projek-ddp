import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def convert_currency():
    try:
        amount = float(entry_amount.get())
        rate = float(entry_rate.get())
        result = amount * rate
        label_result.config(text=f"Result: {result:.2f} {combo_to_currency.get()}")
    except ValueError:
        label_result.config(text="Invalid input, please enter valid numbers.")

root = tk.Tk()
root.title("Currency Converter")

style = Style(theme="flatly")
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input Amount
label_amount = ttk.Label(frame, text="Amount:")
label_amount.grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)
entry_amount = ttk.Entry(frame)
entry_amount.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

# Currency From
label_from_currency = ttk.Label(frame, text="From Currency:")
label_from_currency.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)
combo_from_currency = ttk.Combobox(frame, values=["USD", "EUR", "GBP"])
combo_from_currency.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)
combo_from_currency.set("USD")

# Currency To
label_to_currency = ttk.Label(frame, text="To Currency:")
label_to_currency.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)
combo_to_currency = ttk.Combobox(frame, values=["USD", "EUR", "GBP"])
combo_to_currency.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
combo_to_currency.set("EUR")

# Exchange Rate
label_rate = ttk.Label(frame, text="Exchange Rate:")
label_rate.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)
entry_rate = ttk.Entry(frame)
entry_rate.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

# Convert Button
button_convert = ttk.Button(frame, text="Convert", command=convert_currency)
button_convert.grid(row=4, column=0, columnspan=2, pady=10)

# Result Label
label_result = ttk.Label(frame, text="Result:")
label_result.grid(row=5, column=0, columnspan=2, pady=5)

# Configure grid weights
for i in range(6):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
