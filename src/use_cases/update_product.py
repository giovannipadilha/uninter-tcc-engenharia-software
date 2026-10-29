from dataclasses import dataclass
from decimal import Decimal
from use_cases.product_repository import ProductRepository


# MESMA COISA DO CREATE USE CASE


@dataclass
class UpdateProductInput:
    id: int
    name: str
    price: Decimal
    quantity: int


@dataclass
class UpdateProductOutput:
    id: int
    name: str
    price: Decimal
    quantity: int


class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, input_data: UpdateProductInput) -> UpdateProductOutput:
        product = self.repository.get_by_id(product_id=input_data.id)

        if product is None:
            raise ValueError("Produto não encontrado.")

        existing_product = self.repository.get_by_name(product_name=input_data.name)
        if existing_product is not None and existing_product.id != product.id:
            raise ValueError("Já existe um produto com este nome, tente outro.")

        product.change_details(
            name=input_data.name, price=input_data.price, quantity=input_data.quantity
        )

        product_updated = self.repository.update(product=product)

        return UpdateProductOutput(
            id=product_updated.id,
            name=product_updated.name,
            price=product_updated.price,
            quantity=product_updated.quantity,
        )
