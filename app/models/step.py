from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class BuyStep(Base):
    __tablename__ = "buy_step"

    id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.id", ondelete="CASCADE"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.id", ondelete="CASCADE"))
    date_step_beg: Mapped[datetime]
    date_step_end: Mapped[datetime]

    buy: Mapped["Buy"] = relationship(back_populates="steps")
    step: Mapped["Step"] = relationship(back_populates="buys")

    def __str__(self) -> str:
        return (
            f"step id: {self.step_id}, buy id: {self.buy_id}\n"
            f"date started: {self.date_step_beg}, date_ended: {self.date_step_end}"
        )


class Step(Base):
    __tablename__ = "step"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str] = mapped_column(String(50))

    buys: Mapped[list["BuyStep"]] = relationship(
        back_populates="step", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return self.name_step
