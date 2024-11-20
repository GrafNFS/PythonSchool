from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def update_base_two_label(event):
    code = base_two_combobox.get()
    name = currencies[code]
    b_two_label.config(text=name)

def update_target_label(event):
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base_two_code = base_two_combobox.get()
    msg_exchange = ""

    if target_code and base_code and base_two_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            response_two = requests.get(f'https://open.er-api.com/v6/latest/{base_two_code}')
            response_two.raise_for_status()

            data = response.json()
            data_two = response_two.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                msg_exchange = f"Курс {exchange_rate:.1f} {target} за 1 {base}"
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")

            if target_code in data_two['rates']:
                exchange_rate_two = data_two['rates'][target_code]
                base_two = currencies[base_two_code]
                target_two = currencies[target_code]
                msg_exchange = msg_exchange + f"\nКурс {exchange_rate_two:.1f} {target_two} за 1 {base_two}"
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")

            mb.showinfo("Курс обмена", msg_exchange)
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

if __name__ == "__main__":
    window = Tk()
    window.title("Курс обмена валюты")
    window.geometry("360x400")

    Label(text="Базовая валюта:").pack(padx=10, pady=5)
    base_combobox = ttk.Combobox(values=list(currencies.keys()))
    base_combobox.pack(padx=10, pady=5)
    base_combobox.bind("<<ComboboxSelected>>", update_base_label)

    b_label = ttk.Label()
    b_label.pack(padx=10, pady=10)

    Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
    base_two_combobox = ttk.Combobox(values=list(currencies.keys()))
    base_two_combobox.pack(padx=10, pady=5)
    base_two_combobox.bind("<<ComboboxSelected>>", update_base_two_label)

    b_two_label = ttk.Label()
    b_two_label.pack(padx=10, pady=10)

    Label(text="Целевая валюта:").pack(padx=10, pady=5)
    target_combobox = ttk.Combobox(values=list(currencies.keys()))
    target_combobox.pack(padx=10, pady=5)
    target_combobox.bind("<<ComboboxSelected>>", update_target_label)

    t_label = ttk.Label()
    t_label.pack(padx=10, pady=10)

    Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

    window.mainloop()