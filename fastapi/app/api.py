from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.clients.payment_client import PaymentClient
from app.db.payments_repository import PaymentsRepository

app = FastAPI(title="Python API Practices – FastAPI")

client = PaymentClient()
repo = PaymentsRepository()


class CreatePaymentRequest(BaseModel):
    amount: int
    currency: str


@app.post("/api/payments")
async def create_payment(payload: CreatePaymentRequest):
    if payload.amount <= 0:
        raise HTTPException(status_code=400, detail="amount must be > 0")

    payment = await client.create_payment(
        amount=payload.amount,
        currency=payload.currency,
        idempotency_key="demo-fastapi",
    )
    return repo.save(payment)
