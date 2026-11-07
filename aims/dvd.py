"""Thông tin một DVD trong danh mục."""
from dataclasses import dataclass

@dataclass(frozen=True)
class DigitalVideoDisc:
    title: str
    category: str = ""
    director: str = ""
    length: int = 0
    cost: float = 0.0

    def __str__(self):
        details = self.category or "Chưa phân loại"
        return f"{self.title} ({details}) - {self.cost:.2f} $"
