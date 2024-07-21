from typing import List
from uuid import uuid4

class Tarefa:
    def __init__(self, descricao):
        self.__descricao = descricao
        self.__id = uuid4()
        
        self.feito = False


    def __str__(self):
        return f'Tarefa(id="{self.__id}", feito={self.feito}, descricao="{self.__descricao}")'


    def get_descricao(self):
        return self.__descricao


    def get_id(self):
        return self.__id


class ControleTarefas():
    def __init__(self):
        self.__tarefas: List[Tarefa] = [
            Tarefa('1 Donec lacinia enim vitae suscipit accumsan.'),
            Tarefa('2 Donec dictum leo ut ipsum interdum ullamcorper.'),
            Tarefa('3 Cras venenatis dolor in interdum venenatis.'),
            Tarefa('4 Nullam sed augue mollis, lacinia leo a, imperdiet nulla.'),
            Tarefa('5 Pellentesque commodo ante ultrices felis consectetur, quis pharetra sem fringilla.'),
            Tarefa('6 Nunc imperdiet libero at felis rhoncus dapibus.'),
        ]
        self.__tarefas[3].feito=True


    def add(self, descricao: str):
        if len(descricao) > 0:
            tarefa = Tarefa(descricao)
            self.__tarefas.append(tarefa)
            print(tarefa)


    def listar(self):
        # for tarefa in self.__tarefas:
        #     print(tarefa)
        return self.__tarefas


    def excluir(self, id):
        indice = None

        for tarefa in self.__tarefas:
            if tarefa.get_id() == id:
                indice = self.__tarefas.index(tarefa)
                break

        if indice != None:
            self.__tarefas.pop(indice)
