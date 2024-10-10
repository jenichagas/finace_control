from control_expenses import Control
from expenses import Expenses
from user import User
from savings import Savings

user = User("Jeniffer", 3000)

control_expenses = Control()

expense01 = Expenses(" água", 98)
expense02 = Expenses(" telefone", 50)
expense03 = Expenses("Shoppe", 300)
expense04 = Expenses("Ração", 100)
expense05 = Expenses("Mercado", 1000)
expense06 = Expenses("Internet", 100)

control_expenses.add_expenses(expense01)
control_expenses.add_expenses(expense02)
control_expenses.add_expenses(expense03)
control_expenses.add_expenses(expense04)
control_expenses.add_expenses(expense05)
control_expenses.add_expenses(expense06)

user.show_user()
control_expenses.show_itens()


total_expenses = control_expenses.calculate_total_value()
remaining = control_expenses.calculate_remaining(user.initial_income)
print(f"Total de despesas: R${total_expenses}")
print(f"Valor que sobrou: R${remaining}")

savings = Savings(remaining)
savings.show_savings()




