from fastapi import FastAPI
from sales_api.routes import customers

app = FastAPI()

app.include_router(customers.router)

@app.get("/")
def read_root():
    return {"message": "Hello AdventureWorks"}