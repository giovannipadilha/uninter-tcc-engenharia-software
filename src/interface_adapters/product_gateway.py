import sqlite3
from decimal import Decimal

from entities.product import Product
from use_cases.product_repository import ProductRepository


# IMPLEMENTAÇÃO CONCRETA DO "CONTRATO" (REPOSITORY) DE AÇÕES DE PRODUCT


class ProductGateway(ProductRepository):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection


    def save(self, product: Product) -> Product:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
            (product.name, str(product.price), product.quantity)
        )

        self.connection.commit()
        product.id = cursor.lastrowid

        return product

    def get_by_id(self, product_id: int) -> Product | None:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT id, name, price, quantity FROM products where id = ?",
            (product_id)
        )

        row = cursor.fetchone()

        return self._row_to_product(row) if row else None

    def get_by_name(self, product_name: str) -> Product | None:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT id, name, price, quantity FROM products where name = ?",
            (product_name)
        )

        row = cursor.fetchone()

        return self._row_to_product(row) if row else None

    def update(self, product: Product) -> Product:
        cursor = self.connection.cursor()

        cursor.execute(
            "UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?",
            (product.name, product.price, product.quantity, product.id)
        )

        row = cursor.fetchone()

        return self._row_to_product(row) if row else None
    
    @staticmethod
    def _row_to_product(row: tuple) -> Product:
        id_, name, price, quantiy = row

        return Product(id=id_, name=name, price=Decimal(price), quantity=quantiy)
