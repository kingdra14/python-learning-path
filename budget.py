from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass
class Transaction:
    description: str
    amount: float
    category: str = "other"
def total_by_category(transactions:list[Transaction]) ->  dict[str, float]:
    totals:dict[str, float] = {}
    for t in transactions:
        totals[t.category] = totals.get(t.category, 0) + t.amount
    return totals

