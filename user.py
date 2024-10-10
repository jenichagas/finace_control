class User:
  def __init__(self, name: str, initial_income: float) -> None:
    self.name = name
    self.initial_income = initial_income

  def show_user(self):
    print(f"Controle financeiro, {self.name}. Salário: R${self.initial_income}")
    

 