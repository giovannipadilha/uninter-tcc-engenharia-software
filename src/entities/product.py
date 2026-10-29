from dataclasses import dataclass
from decimal import Decimal

# Não depende de nada, tanto a camada de Infra, Adapters e Use Cases pode mudar que isso não quebra!


@dataclass(kw_only=True)
class Product:
    id: int | None = None
    name: str
    price: Decimal
    quantity: int

    def __post_init__(self):
        self._validate(self.name, self.price, self.quantity)

    def _validate(self, name: str, price: Decimal, quantity: int):
        if not name.strip():
            raise ValueError("O nome do produto é obrigatório.")
        if price < 0:
            raise ValueError("O valor do produto não pode ser menor que 0 (zero).")
        if quantity < 0:
            raise ValueError("A quantidade do produto não pode ser menor que 0 (zero).")

    def change_details(self, name: str, price: Decimal, quantity: int):
        self._validate(name, price, quantity)

        self.name = name
        self.price = price
        self.quantity = quantity
