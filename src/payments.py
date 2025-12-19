from typing import Dict, List
from datetime import datetime

# In-memory invoices and payments store for demo purposes
# Invoice: {id, student_email, amount_cents, due_date, status, created_at, payments: [payment_ids]}
# Payment: {id, invoice_id, amount_cents, paid_at}

invoices: Dict[int, Dict] = {}
payments: Dict[int, Dict] = {}

_invoice_seq = 1
_payment_seq = 1


def create_invoice(student_email: str, amount_cents: int, due_date: str = None) -> Dict:
    global _invoice_seq
    invoice_id = _invoice_seq
    _invoice_seq += 1
    invoice = {
        "id": invoice_id,
        "student_email": student_email,
        "amount_cents": amount_cents,
        "due_date": due_date,
        "status": "open",
        "created_at": datetime.utcnow().isoformat(),
        "payments": [],
    }
    invoices[invoice_id] = invoice
    return invoice


def list_invoices() -> List[Dict]:
    return list(invoices.values())


def get_invoice(invoice_id: int) -> Dict:
    return invoices.get(invoice_id)


def record_payment(invoice_id: int, amount_cents: int) -> Dict:
    global _payment_seq
    invoice = invoices.get(invoice_id)
    if not invoice:
        raise KeyError("invoice not found")
    payment_id = _payment_seq
    _payment_seq += 1
    payment = {
        "id": payment_id,
        "invoice_id": invoice_id,
        "amount_cents": amount_cents,
        "paid_at": datetime.utcnow().isoformat(),
    }
    payments[payment_id] = payment
    invoice["payments"].append(payment_id)
    # update invoice status
    paid = sum(payments[p]["amount_cents"] for p in invoice["payments"]) if invoice["payments"] else 0
    if paid >= invoice["amount_cents"]:
        invoice["status"] = "paid"
    else:
        invoice["status"] = "partial"
    return payment
