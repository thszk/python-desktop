import tkinter as tk
from operacao import Operacao

root = tk.Tk()
root.title('Calculadora')
root.resizable(False, False)

display = tk.StringVar() # variável para ser utilizada nos widgets tkinter
operacao = Operacao(display) # cria o controlador de operações

frame = tk.Frame(root) # agrupador dos widgets
frame.grid()

# widget para o "visor"
label = tk.Label(frame, textvariable=display)
label.grid(row=1, rowspan=2, columnspan=5, sticky='wens')

# widgets para os "botões"
# 1a linha
tk.Button(frame, text="7", command=lambda: operacao.set_valor('7'), width=5, height=2).grid(row=3, column=1)
tk.Button(frame, text="8", command=lambda: operacao.set_valor('8'), width=5, height=2).grid(row=3, column=2)
tk.Button(frame, text="9", command=lambda: operacao.set_valor('9'), width=5, height=2).grid(row=3, column=3)
tk.Button(frame, text="÷", command=lambda: operacao.set_operacao('/'), width=5, height=2).grid(row=3, column=4)

# 2a linha
tk.Button(frame, text="4", command=lambda: operacao.set_valor('4'), width=5, height=2).grid(row=4, column=1)
tk.Button(frame, text="5", command=lambda: operacao.set_valor('5'), width=5, height=2).grid(row=4, column=2)
tk.Button(frame, text="6", command=lambda: operacao.set_valor('6'), width=5, height=2).grid(row=4, column=3)
tk.Button(frame, text="x", command=lambda: operacao.set_operacao('*'), width=5, height=2).grid(row=4, column=4)

# 3a linha
tk.Button(frame, text="1", command=lambda: operacao.set_valor('1'), width=5, height=2).grid(row=5, column=1)
tk.Button(frame, text="2", command=lambda: operacao.set_valor('2'), width=5, height=2).grid(row=5, column=2)
tk.Button(frame, text="3", command=lambda: operacao.set_valor('3'), width=5, height=2).grid(row=5, column=3)
tk.Button(frame, text="-", command=lambda: operacao.set_operacao('-'), width=5, height=2).grid(row=5, column=4)

# 4a linha
tk.Button(frame, text=",", command=lambda: operacao.set_valor('.'), width=5, height=2).grid(row=6, column=1)
tk.Button(frame, text="0", command=lambda: operacao.set_valor('0'), width=5, height=2).grid(row=6, column=2)
tk.Button(frame, text="+", command=lambda: operacao.set_operacao('+'), width=5, height=2).grid(row=6, column=4)
tk.Button(frame, text="=", command=operacao.calcular, width=5, height=2).grid(row=6, column=3)

# 5a linha
tk.Button(frame, text="Limpar", command=operacao.limpar, height=2).grid(row=7, columnspan=5, sticky=tk.EW)

root.mainloop()