from tkinter import StringVar

class Operacao:
    def __init__(self, display: StringVar):
        self.__display = display

        self.limpar()


    def set_valor(self, x):
        if self.__operacao == None:
            self.__valor1 += x
        else:
            self.__valor2 += x

        self.__atualizar_display()


    def set_operacao(self, x):
        if len(self.__valor1) > 0:
            self.__operacao = x

        self.__atualizar_display()


    def calcular(self):
        match self.__operacao:
            case '+':
                self.__resultado = float(self.__valor1) + float(self.__valor2)

            case '-':
                self.__resultado = float(self.__valor1) - float(self.__valor2)

            case '*':
                self.__resultado = float(self.__valor1) * float(self.__valor2)

            case '/':
                self.__resultado = float(self.__valor1) / float(self.__valor2)

        self.__atualizar_display()


    def limpar(self):
        self.__valor1 = ''
        self.__valor2 = ''
        self.__operacao = None
        self.__resultado = None

        self.__atualizar_display()


    def __atualizar_display(self):
        novo_valor = '\n'

        if self.__valor1 != '':
            novo_valor = f'{self.__valor1}\n'
            
            if self.__operacao != None:
                novo_valor = f'{self.__valor1} {self.__operacao}\n'

                if self.__valor2 != '':
                    novo_valor = f'{self.__valor1} {self.__operacao} {self.__valor2}\n'

                    if self.__resultado != None:
                        novo_valor = f'{novo_valor} = {self.__resultado}'

        self.__display.set(novo_valor)
        
        