from fastapi import FastAPI

app = FastAPI(
    title="CartNest API",
    description="REST API for the CartNest e-commerce platform.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "CartNest",
        "message": "Welcome to CartNest API",
        "status": "running",
    }


@app.get("/health/live")
def liveness():
    return {"status": "alive"}


@app.get("/health/ready")
def readiness():
    return {"status": "ready"}


@app.get("/api/v1/products")
def list_products():
    return {
        "items": [
            {
                "id": 1,
                "name": "Wireless Headphones",
                "price": 79.99,
                "currency": "USD",
            },
            {
                "id": 2,
                "name": "Mechanical Keyboard",
                "price": 109.99,
                "currency": "USD",
            },
            {
                "id": 3,
                "name": "Smart Watch",
                "price": 149.99,
                "currency": "USD",
            },
        ],
        "total": 3,
    }