from expenses import Expenses
class Control:
  def __init__(self) -> None:
    self.expenses = []

  def add_expenses(self, expenses):
    self.expenses.append(expenses)

  def calculate_total_value(self):
    return sum([expenses.value for expenses in self.expenses])
    
  def calculate_remaining(self, initial_income):
    total_expenses = self.calculate_total_value()
    return initial_income - total_expenses
  
  def show_itens(self):
    for expenses in self.expenses:
      print(expenses)
  
        