
class Savings:

  def __init__(self, total_remainder) -> None:
    self.total_remainder = total_remainder 
    self.savings = total_remainder * 0.40
    self.emergency_savings = total_remainder * 0.20

  def show_savings(self):
    print(f"Reserva para sonho: R${self.savings:.2f}")
    print(f"Reserva de Emergência: R${self.emergency_savings:.2f}")




