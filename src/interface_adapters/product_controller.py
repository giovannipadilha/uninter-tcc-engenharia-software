from decimal import Decimal

from use_cases.create_product import (
    CreateProductInput,
    CreateProductOutput,
    CreateProductUseCase
)

from use_cases.update_product import (
    UpdateProductInput,
    UpdateProductOutput,
    UpdateProductUseCase
)


class ProductController:
    def __init__(self, create_use_case: CreateProductUseCase, update_use_case: UpdateProductUseCase):
        self.create_use_case = create_use_case
        self.update_use_case = update_use_case


    def create(self, name: str, price: Decimal, quantity: int) -> CreateProductOutput:
        input_data = CreateProductInput(name=name, price=price, quantity=quantity)

        return self.create_use_case.execute(input_data)

    def update(self, id: int, name: str, price: Decimal, quantity: int) -> UpdateProductOutput:
        input_data = UpdateProductInput(id=id, name=name, price=price, quantity=quantity)

        return self.update_use_case.execute(input_data)
