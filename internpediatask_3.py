import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_rates():
    """Fetches conversion rates and updates the rates dict."""
    api_key = "2c8cfc121ade2941fd511518"
    url = f"https://v6.exchangerate-api.com/v6/2c8cfc121ade2941fd511518/latest/USD"
    response = requests.get(url)
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to retrieve data")
        return None
    data = response.json()
    return data['conversion_rates']

def convert_currency():
    """Converts the amount from from_currency to to_currency."""
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        result = amount * rates[from_currency] / rates[to_currency]
        result_label.config(text=f"Converted Amount: {result:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
    except KeyError:
        messagebox.showerror("Error", "Currency conversion error.")
root = tk.Tk()
root.title("Currency Converter")
rates = get_rates()
if not rates:
    root.destroy()

currency_options = list(rates.keys())
from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="From Currency:").grid(row=1, column=0)
from_currency_combo = ttk.Combobox(root, textvariable=from_currency_var, values=currency_options)
from_currency_combo.grid(row=1, column=1)
from_currency_combo.set("USD")

tk.Label(root, text="To Currency:").grid(row=2, column=0)
to_currency_combo = ttk.Combobox(root, textvariable=to_currency_var, values=currency_options)
to_currency_combo.grid(row=2, column=1)
to_currency_combo.set("EUR")

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=1)

result_label = tk.Label(root, text="Converted Amount:")
result_label.grid(row=4, columnspan=2)

root.mainloop()
