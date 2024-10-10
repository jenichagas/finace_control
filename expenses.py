class Expenses:

  def __init__(self, identification: str, value: float) -> None:
    self.name = identification 
    self.value = value

  def __str__(self):
    return f"Conta: {self.name}, Valor: {self.value}"