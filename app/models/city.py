from sqlalchemy import CheckConstraint, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str] = mapped_column(String(50))
    days_delivery: Mapped[int] = mapped_column(
        CheckConstraint("days_delivery > 0", name="check_days_delivery_positive"),
    )

    clients: Mapped[list["Client"]] = relationship(
        back_populates="city", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return self.name_city
