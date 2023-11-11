from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class Transaction:
    id: UUID
    created_at: datetime
    amount: int
    from_id: UUID
    to_id: UUID
    currency_id: UUID
    category_id: UUID
