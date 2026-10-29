from decimal import Decimal

from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from pydantic import BaseModel, ConfigDict

from infrastructure.database import get_connection
from interface_adapters.product_controller import ProductController
from interface_adapters.product_gateway import ProductGateway
from use_cases.create_product import CreateProductUseCase
from use_cases.update_product import UpdateProductUseCase

router = APIRouter()


# ONDE TUDO OCORRE, ONDE O GATEWAY CONCRETO É USADO JUNTAMENTE DO CONTROLLER
# FRONTEIRA EXTERNA


class ProductRequest(BaseModel):
    name: str
    price: Decimal
    quantity: int


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: Decimal
    quantity: int


def get_gateway():
    connection = get_connection()
    try:
        yield ProductGateway(connection)
    finally:
        connection.close()


def get_controller(gateway: ProductGateway = Depends(get_gateway)) -> ProductController:
    return ProductController(
        create_use_case=CreateProductUseCase(gateway),
        update_use_case=UpdateProductUseCase(gateway)
    )


@router.post("/products", response_model=ProductResponse, status_code=201)
def create_product(
    product: ProductRequest, controller: ProductController = Depends(get_controller)
):
    try:
        return controller.create(
            name=product.name, price=product.price, quantity=product.quantity
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, product: ProductRequest, controller: ProductController = Depends(get_controller)
):
    try:
        return controller.update(
            id=product_id,
            name=product.name,
            price=product.price,
            quantity=product.quantity
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
