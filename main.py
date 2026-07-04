import tkinter as tk 

root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")

expression = ""

def press(value):
    global expression
    expression += value
    btn_result.delete(0, tk.END)
    btn_result.insert(0, expression)

def evaluate_expression():
    global expression
    result = eval(expression)
    print(result)

root.grid_rowconfigure(0 , weight=1)
root.grid_rowconfigure(1 , weight=1)
root.grid_rowconfigure(2 , weight=1)
root.grid_rowconfigure(3 , weight=1)
root.grid_rowconfigure(4 , weight=1)
root.grid_rowconfigure(5 , weight=1)
root.grid_columnconfigure(0 , weight=1)
root.grid_columnconfigure(1 , weight=1)
root.grid_columnconfigure(2 , weight=1)
root.grid_columnconfigure(3 , weight=1)

btn_result = tk.Entry(border = "5")
btn_result.grid(row = 0 , column = 0, columnspan = 6, sticky = "news")

btn_leftbracket = tk.Button(text = "(", font = ("arial" , 15), border = "5", command = lambda : press("("))
btn_leftbracket.grid(row =1, column = 0, sticky = "news")
btn_rightbracket = tk.Button(text = ")", font = ("arial" , 15), border = "5", command = lambda : press(")"))
btn_rightbracket.grid(row = 1, column = 1, sticky = "news")
btn_percent = tk.Button(text = "%", font = ("arial" , 15), border = "5", command = lambda : press("%"))
btn_percent.grid(row = 1, column = 2, sticky = "news")
btn_add = tk.Button(text = "+", font = ("arial" , 15), border = "5", command = lambda : press("+"))
btn_add.grid(row =1, column = 3, sticky = "news")

btn_7 = tk.Button(text = "7", font = ("arial" , 15), border = "5", command = lambda : press("7"))
btn_7.grid(row =2, column = 0, sticky = "news")
btn_8 = tk.Button(text = "8", font = ("arial" , 15), border = "5", command = lambda : press("8"))
btn_8.grid(row = 2, column = 1, sticky = "news")
btn_9 = tk.Button(text = "9", font = ("arial" , 15), border = "5", command = lambda : press("9"))
btn_9.grid(row = 2, column = 2, sticky = "news")
btn_sub = tk.Button(text = "-", font = ("arial" , 15), border = "5", command = lambda : press("-"))
btn_sub.grid(row =2, column = 3, sticky = "news")

btn_4 = tk.Button(text = "4", font = ("arial" , 15), border = "5", command = lambda : press("4"))
btn_4.grid(row =3, column = 0, sticky = "news")
btn_5 = tk.Button(text = "5", font = ("arial" , 15), border = "5", command = lambda : press("5"))
btn_5.grid(row = 3, column = 1, sticky = "news")
btn_6 = tk.Button(text = "6", font = ("arial" , 15), border = "5", command = lambda : press("6"))
btn_6.grid(row = 3, column = 2, sticky = "news")
btn_divide = tk.Button(text = "÷", font = ("arial" , 15), border = "5", command = lambda : press("/"))
btn_divide.grid(row =3, column = 3, sticky = "news")

btn_1= tk.Button(text = "1", font = ("arial" , 15), border = "5", command = lambda : press("1"))
btn_1.grid(row =4, column = 0, sticky = "news")
btn_2 =tk.Button(text = "2", font = ("arial" , 15), border = "5", command = lambda : press("2"))
btn_2.grid(row = 4, column = 1, sticky = "news")
btn_3 = tk.Button(text = "3", font = ("arial" , 15), border = "5", command = lambda : press("3"))
btn_3.grid(row = 4, column = 2, sticky = "news")
btn_product = tk.Button(text = "x", font = ("arial" , 15), border = "5", command = lambda : press("*"))
btn_product.grid(row =4, column = 3, sticky = "news")

btn_backspace = tk.Button(text = "⌫", font = ("arial" , 15))
btn_backspace.grid(row =5, column = 0, sticky = "news")
btn_0 = tk.Button(text = "0", font = ("arial" , 15), border = "5", command = lambda : press("0"))
btn_0.grid(row = 5, column = 1, sticky = "news")
btn_dot = tk.Button(text = ".", font = ("arial" , 15), border = "5", command = lambda : press("."))
btn_dot.grid(row = 5, column = 2, sticky = "news")
btn_equal = tk.Button(text = "=", font = ("arial" , 15), border = "5", command = evaluate_expression)
btn_equal.grid(row =5, column = 3, sticky = "news")


root.mainloop()