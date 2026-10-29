from abc import ABC, abstractmethod
from entities.product import Product

# É um "contrato" das ações que a entidade Product pode realizar.
# Você pode mudar a camda de interfaces e a de infra sem afetar isso, mas
# como essa camada depende do produto, se mudar produto dá BO.


# O QUE PRODUCT PODE FAZER

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product | None:
        pass

    @abstractmethod
    def get_by_name(self, product_name: str) -> Product | None:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass
