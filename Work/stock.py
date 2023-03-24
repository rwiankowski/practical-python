class Stock:

    def __init__(self, name:str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    def cost(self) -> float:
        return self.shares * self.shares

    def sell(self, amount: int):
        self.shares -= amount

