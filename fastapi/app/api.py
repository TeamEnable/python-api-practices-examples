from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services.payments import create_payment


app = FastAPI(title="Python API Practices – FastAPI")


class CreatePaymentRequest(BaseModel):
    amount: int
    currency: str


@app.post("/api/payments")
async def create_payment_endpoint(payload: CreatePaymentRequest):
    if payload.amount <= 0:
        raise HTTPException(status_code=400, detail="amount must be > 0")
    return await create_payment(amount=payload.amount, currency=payload.currency)
