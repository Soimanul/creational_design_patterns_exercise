
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None
    _balance: float

    def __new__(cls, initial_amount: float = 0.0):
      # TODO: Singleton pattern implementation
      if cls._instance is None:
        cls._instance = super().__new__(cls)
        cls._instance._balance = initial_amount
      return cls._instance

    def __init__(self, initial_amount: float = 0.0):
        if not hasattr(self, "_balance"):
            self._balance = initial_amount

    def allocate(self, amount: float) -> None:
      # TODO: Allocate amount from the budget
      if amount <= 0:
        raise ValueError("Allocation must be positive")
      if amount > self._balance:
        raise ValueError("Insufficient funds")
      self._balance -= amount

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
