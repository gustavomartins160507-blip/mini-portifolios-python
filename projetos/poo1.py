class produtos:
    def __init__(self, codigo, nome, quantidade, preco):
        self.nome = str(nome)
        self.quantidade = int(quantidade)
        self.codigo = str(codigo)
        self.preco = float(preco)
    def mostrar_codigo(self):
        if self.codigo.count('-') == 0:
            return False
        if self.codigo.find('-') != 3:
            return False
        if not self.codigo[:3].isupper():
            return False
        if not self.codigo[4:].isnumeric():
            return False
        print(f'codigo: {self.codigo}')
        return True
    def mostrar_preco(self):
        if self.preco <= 0:
            return False
        print(f'Preço: {self.preco}')
        return True
    def vender(self, venda, saldo):
        venda = int(input('Quantos produtos serão vendidos? '))
        if venda > self.quantidade:
            print('Quantidade insuficiente de produtos para venda')
            return False
        quantidade_final = self.quantidade - venda
        valor_final = venda * self.preco
        saldo_final = saldo + valor_final
        self.quantidade = quantidade_final
        print(f'Saldo: {saldo_final} | Vendido: {venda} | Restante: {quantidade_final}')
        return saldo_final
    def repor(self,nova_quantidade,):
        self.quantidade+=nova_quantidade
        print(f'{self.quantidade}')
p=produtos(codigo='ABC-1234',nome='leite',quantidade=10,preco=5.0)
p.mostrar_codigo()
p.mostrar_preco()
p.vender(0,0)
p.repor(5)
#Nesse codigo é possivel ver que ele atribui as condições dentro das funções, 
# caso elas nao forem corretas o codigo retorna false, então a função não é executada
# as tipagens dos objetos estão setadas na def _init_