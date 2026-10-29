from dataclasses import dataclass
from decimal import Decimal

from entities.product import Product
from use_cases.product_repository import ProductRepository


# DEPENDO DE ENTITY E REPOSITORY

# Regras da aplicação/negócios
# NÃO DEPENDE DE INTERFACES EXTERNAS E INFRA
# FRONTEIRA INTERNA

# COMO PRODUCT PODE FAZER ou DEVE FAZER
# REGRAS PARA CRIAR UMA ENTITY PRODUCT

@dataclass
class CreateProductInput:
    name: str
    price: Decimal
    quantity: int


@dataclass
class CreateProductOutput:
    id: int
    name: str
    price: Decimal
    quantity: int


class CreateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, input_data: CreateProductInput) -> CreateProductOutput:
        existing_product = self.repository.get_by_name(product_name=input_data.name)
        if existing_product is not None:
            raise ValueError("Já existe um produto com este nome, tente outro.")

        product = Product(
            name=input_data.name, price=input_data.price, quantity=input_data.quantity
        )

        product_saved = self.repository.save(product=product)

        return CreateProductOutput(
            id=product_saved.id,
            name=product_saved.name,
            price=product_saved.price,
            quantity=product_saved.quantity,
        )
