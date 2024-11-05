import tkinter as tk

def fash_lingaind():
    num1 = int(number1_entre.get())
    num2 = int(number2_entre.get())
    return num1, num2


def ger_xing(value):
    number3_entre.delete(0, 'end')
    number3_entre.insert(0, value)


def lande():
    num1, num2 = fash_lingaind()
    res = num1 + num2
    ger_xing(res)


def sin():
    pass





window = tk.Tk()
window.title('Ресовать')
window.geometry('420x420')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=4, height=4, command=lande)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=4, height=4)
button_sub.place(x=150, y=200)
button_mol = tk.Button(window, text='*', width=4, height=4)
button_mol.place(x=200, y=200)
button_div = tk.Button(window, text='/', width=4, height=4)
button_div.place(x=250, y=200)
number1_entre = tk.Entry(window, width=20)
number1_entre.place(x=150, y=80)
number2_entre = tk.Entry(window, width=20)
number2_entre.place(x=150, y=160)
number3_entre = tk.Entry(window, width=20)
number3_entre.place(x=150, y=300)
number1 = tk.Label(window, text='Вести первое число')
number1.place(x=150, y=50)
number2 = tk.Label(window, text='Вести второе число')
number2.place(x=150, y=130)
number3 = tk.Label(window, text='Ответ')
number3.place(x=150, y=270)
window.mainloop()