# ***Exercício 4: Crie uma classe chamada `Conta_bancaria` com um atributo `saldo` inicializado com 0. Em seguida, crie métodos `deposito` e `saque` que atualizem o saldo. Crie um objeto da classe `ContaBancaria`, faça um depósito e um saque, e imprima o saldo resultante.***


from saque import Saque
from deposito import Deposito



class ContaBancaria:
  def __init__(self, saldo=0):
    self.saldo = saldo

  def depositar(self, valor):
    deposito = Deposito(valor)
    self.saldo = deposito.executar2(valor)
    print (f'O Deposito é de r$: {valor}, Saldo atual é de: R$ {self.saldo}')

  def sacar(self, valor):
    saque = Saque(valor)
    saldo_atual = saque.executar(self.saldo)
    if saldo_atual is not False:
      self.saldo = saldo_atual
      print (f'Saque de R$: {valor}, Saldo atual é de: R$ {self.saldo}')
    else:
      print ('Saldo insuficiente')

if __name__ == '__main__':
  conta = ContaBancaria(50)
  conta.depositar(20)
  conta.sacar(10)

______________________TKINTER