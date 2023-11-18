class Saque():
  def __init__(self, saldo):
    self.valor = saldo

  def executar(self, saldo):
     if self.valor:
       saldo -= self.valor
     else:
       return False