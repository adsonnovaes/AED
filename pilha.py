class pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        self.iterando = None

    class no:
        def __init__(self,valor):
            self.valor = valor
            self.proximo = None


    def __len__(self):
        return self.tamanho

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterando is None:
            self.iterando = self.topo
        else:
            self.iterando = self.iterando.proximo

        if self.iterando is not None:
            return self.iterando.valor

        raise StopIteration

    def push(self,valor):
        novo = self.no(valor)

        if self.topo is None:
            self.topo = novo

        elif self.topo is not None:
            novo.proximo = self.topo
            self.topo = novo

        self.tamanho += 1
        self.iterando = None

    def pop(self):
        if self.topo is not None:
            aux = self.topo
            self.topo = aux.proximo
            aux.proximo = None
            self.tamanho -= 1
            self.iterando = None

            return aux


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        pilha = '['
        for j, i in enumerate(self):
            pilha += i.__repr__()
            if j < len(self) - 1:
                pilha += ', '

        pilha += ']'

        return pilha



teste = pilha()
teste.push(1)
teste.push(2)
teste.push(3)
teste.push(4)
teste.pop()
print(teste)
teste.pop()
print(teste)
teste.push(3)
print(teste)