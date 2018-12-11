class fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.iterando = None
        self.tamanho = 0

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
            self.iterando = self.fim
        else:
            self.iterando = self.iterando.proximo

        if self.iterando is not None:
            return self.iterando.valor

        raise StopIteration

    def inserir(self,novo):
        novo.proximo = self.fim
        self.fim = novo

    def enqueue(self,valor):
        novo = self.no(valor)

        if self.inicio is None:
            self.inicio = self.fim  = novo

        elif self.inicio is not None:
            self.inserir(novo)

        self.iterando = None
        self.tamanho += 1

    def dequeue(self):
        i = 0
        atual = self.fim
        while i <= len(self)-1:
            if atual is None:
                break
            if atual.proximo == self.inicio:
                self.inicio = atual
                atual.proximo = None
                self.tamanho -= 1

                break

            i += 1
            atual = atual.proximo

        self.iterando = None



    def __repr__(self):
        return self.__str__()

    def __str__(self):
        fila = '['
        for j,i in enumerate(self):
            fila += i.__repr__()
            if j < len(self) - 1:
                fila += ', '

        fila += ']'

        return fila





teste = fila()
teste.enqueue(5)
teste.enqueue(6)
teste.enqueue(7)
teste.dequeue()
print(teste)
