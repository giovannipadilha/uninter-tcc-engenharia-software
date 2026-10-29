from fastapi import FastAPI
from infrastructure.product_api import router

app = FastAPI()

app.include_router(router=router)
