from fastapi import FastAPI

from routers.balance import balance_router

app = FastAPI()

app.include_router(balance_router)