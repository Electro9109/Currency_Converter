from tkinter import *
from forex_python.converter import CurrencyRates
import threading

root = Tk()
root.title('Currency Converter - Real Time Rates')
root.configure(bg='#f0f0f0')

# Initialize forex converter
converter = CurrencyRates()

e = Entry(root, width=35, borderwidth=5, font=('Arial', 12))
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

# Status label to show loading/error messages
status_label = Label(root, text="Ready", bg='#f0f0f0', fg='green', font=('Arial', 10))
status_label.grid(row=6, column=0, columnspan=5, pady=5)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)
    status_label.config(text="Ready", fg='green')

def equal():
    try:
        amount = float(e.get())
        if amount <= 0:
            status_label.config(text="Please enter a valid amount", fg='red')
            return
            
        # Show loading message
        status_label.config(text="Converting... Please wait", fg='orange')
        root.update()
        
        # Perform conversion in background thread
        def convert_currency():
            try:
                result = 0
                conversion_text = ""
                
                if math == 'dtoi':
                    result = converter.convert('USD', 'INR', amount)
                    conversion_text = f"{amount} USD = {result:.2f} INR"
                elif math == 'itod':
                    result = converter.convert('INR', 'USD', amount)
                    conversion_text = f"{amount} INR = {result:.2f} USD"
                elif math == 'eutoi':
                    result = converter.convert('EUR', 'INR', amount)
                    conversion_text = f"{amount} EUR = {result:.2f} INR"
                elif math == 'itoeu':
                    result = converter.convert('INR', 'EUR', amount)
                    conversion_text = f"{amount} INR = {result:.2f} EUR"
                elif math == 'dtoeu':
                    result = converter.convert('USD', 'EUR', amount)
                    conversion_text = f"{amount} USD = {result:.2f} EUR"
                elif math == 'eutod':
                    result = converter.convert('EUR', 'USD', amount)
                    conversion_text = f"{amount} EUR = {result:.2f} USD"
                elif math == 'itoyen':
                    result = converter.convert('INR', 'JPY', amount)
                    conversion_text = f"{amount} INR = {result:.2f} JPY"
                elif math == 'yentoi':
                    result = converter.convert('JPY', 'INR', amount)
                    conversion_text = f"{amount} JPY = {result:.2f} INR"
                
                # Update GUI in main thread
                root.after(0, lambda: update_result(result, conversion_text))
                
            except Exception as ex:
                root.after(0, lambda: show_error(f"Conversion failed: {str(ex)}"))
        
        # Start conversion in background thread
        thread = threading.Thread(target=convert_currency)
        thread.daemon = True
        thread.start()
        
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')
    except Exception as ex:
        status_label.config(text=f"Error: {str(ex)}", fg='red')

def update_result(result, conversion_text):
    e.delete(0, END)
    e.insert(0, f"{result:.2f}")
    status_label.config(text=conversion_text, fg='green')

def show_error(error_message):
    status_label.config(text=error_message, fg='red')

def dollartoinr():
    first_number = e.get()
    try:
        global fnum, math
        math = 'dtoi'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="Dollar to INR selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def inrtodollar():
    first_number = e.get()
    try:
        global fnum, math
        math = 'itod'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="INR to Dollar selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def eurotoinr():
    first_number = e.get()
    try:
        global fnum, math
        math = 'eutoi'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="Euro to INR selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def inrtoeuro():
    first_number = e.get()
    try:
        global fnum, math
        math = 'itoeu'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="INR to Euro selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def dolltoeuro():
    first_number = e.get()
    try:
        global fnum, math
        math = 'dtoeu'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="Dollar to Euro selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def eurotodoll():
    first_number = e.get()
    try:
        global fnum, math
        math = 'eutod'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="Euro to Dollar selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def inrtoyen():
    first_number = e.get()
    try:
        global fnum, math
        math = 'itoyen'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="INR to Yen selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

def ytoi():
    first_number = e.get()
    try:
        global fnum, math
        math = 'yentoi'
        fnum = float(first_number) if first_number else 0
        status_label.config(text="Yen to INR selected. Click Convert.", fg='blue')
    except ValueError:
        status_label.config(text="Please enter a valid number", fg='red')

# Add decimal point button
def add_decimal():
    current = e.get()
    if '.' not in current:
        e.insert(END, '.')

# Number buttons
but1 = Button(root, text='1', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(1))
but2 = Button(root, text='2', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(2))
but3 = Button(root, text='3', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(3))
but4 = Button(root, text='4', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(4))
but5 = Button(root, text='5', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(5))
but6 = Button(root, text='6', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(6))
but7 = Button(root, text='7', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(7))
but8 = Button(root, text='8', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(8))
but9 = Button(root, text='9', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(9))
but0 = Button(root, text='0', padx=40, pady=20, bg='pink', font=('Arial', 12), command=lambda: button_click(0))

# Decimal point button
but_decimal = Button(root, text='.', padx=40, pady=20, bg='lightblue', font=('Arial', 12), command=add_decimal)

# Control buttons
but_clear = Button(root, text='Clear', padx=35, pady=20, bg='yellow', font=('Arial', 12), command=clear)
but_equal = Button(root, text='Convert', padx=125, pady=20, bg='orange', font=('Arial', 12, 'bold'), command=equal)

# Currency conversion buttons
dtoi = Button(root, text='Dollar to INR', padx=85, pady=20, bg='#D1E231', font=('Arial', 10), command=dollartoinr)
itod = Button(root, text='INR to Dollar', padx=85, pady=20, bg='#D1E231', font=('Arial', 10), command=inrtodollar)

eutoi = Button(root, text='Euro to INR', padx=89, pady=20, bg='#9BC4E2', font=('Arial', 10), command=eurotoinr)
itoeu = Button(root, text='INR to Euro', padx=89, pady=20, bg='#9BC4E2', font=('Arial', 10), command=inrtoeuro)

dtoeu = Button(root, text='Dollar to Euro', padx=83, pady=20, bg='#45CEA2', font=('Arial', 10), command=dolltoeuro)
eutod = Button(root, text='Euro to Dollar', padx=83, pady=20, bg='#45CEA2', font=('Arial', 10), command=eurotodoll)

itoyen = Button(root, text='INR to Yen', padx=99, pady=20, bg='#FC74FD', font=('Arial', 10), command=inrtoyen)
yentoi = Button(root, text='Yen to INR', padx=99, pady=20, bg='#FC74FD', font=('Arial', 10), command=ytoi)

# Grid layout
but7.grid(row=1, column=1)
but8.grid(row=1, column=2)
but9.grid(row=1, column=3)
but4.grid(row=2, column=1)
but5.grid(row=2, column=2)
but6.grid(row=2, column=3)
but1.grid(row=3, column=1)
but2.grid(row=3, column=2)
but3.grid(row=3, column=3)
but0.grid(row=4, column=1)
but_decimal.grid(row=4, column=2)
but_clear.grid(row=4, column=3)
but_equal.grid(row=5, column=1, columnspan=3)

# Currency buttons
dtoeu.grid(row=1, column=0)
eutod.grid(row=2, column=0)
itoyen.grid(row=3, column=0)
yentoi.grid(row=4, column=0)

dtoi.grid(row=1, column=4)
itod.grid(row=2, column=4)
eutoi.grid(row=3, column=4)
itoeu.grid(row=4, column=4)

root.mainloop()
