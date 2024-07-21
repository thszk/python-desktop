import tkinter as tk
from functools import partial
from tarefa import ControleTarefas

'''
Lista de tarefas

_____________ new:icon

[] fazer x    edit:icon delete:icon
[x] fazer y   edit:icon delete:icon
[] teste      edit:icon delete:icon

'''

class App:
    window: tk.Tk
    frame: tk.Frame
    nova_tarefa: tk.StringVar
    tarefas: ControleTarefas

    def __init__(self):
        self.__configurar_tarefas()

        self.__configurar_window()
        self.__configurar_frame()
        self.__configurar_novo()
        self.__configurar_lista()


    def __configurar_tarefas(self):
        self.tarefas = ControleTarefas()


    def __configurar_window(self):
        self.window = tk.Tk()
        self.window.title('Lista de tarefas')
        self.window.geometry('800x300')


    def __configurar_frame(self):
        self.frame = tk.Frame(self.window)
        self.frame.pack()


    def __configurar_novo(self):
        self.nova_tarefa = tk.StringVar()

        frm_novo = tk.LabelFrame(self.frame, text='Nova Tarefa')
        frm_novo.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

        entry = tk.Entry(frm_novo, textvariable=self.nova_tarefa)
        entry.grid(row=1, column=1, sticky=tk.EW)
        entry.bind('<Return>', lambda event: self.__add_tarefa())

        tk.Button(frm_novo, text='Add',  command=self.__add_tarefa).grid(row=1, column=2)


    def __configurar_lista(self):
        self.check_btn_list = []

        frm_lista = tk.LabelFrame(self.frame, text='Tarefas')
        frm_lista.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

        for tarefa in self.tarefas.listar():
            check = tk.BooleanVar(value=tarefa.feito)
            tk.Checkbutton(frm_lista, 
                           text=tarefa.get_descricao(),
                           variable=check,
                           command=partial(self.__alt_feito, tarefa), # com lambda temos um problema de vazamento de escopo
                           ).pack(anchor=tk.W)

            self.check_btn_list.append(check)


    def __add_tarefa(self):
        self.tarefas.add(self.nova_tarefa.get())
        self.nova_tarefa.set('')
        self.__configurar_lista()


    def __alt_feito(self, tarefa):
        tarefa.feito = not tarefa.feito
        self.__configurar_lista()


    def run(self):
        self.window.mainloop()


app = App()
print('App lista de tarefas!')
app.run()