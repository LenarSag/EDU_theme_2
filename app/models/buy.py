from sqlalchemy import CheckConstraint, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class BuyBook(Base):
    __tablename__ = "buy_book"
    id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.id", ondelete="CASCADE"))
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"))
    amount: Mapped[int] = mapped_column(
        CheckConstraint("amount > 0", name="check_amount_positive")
    )

    book: Mapped["Book"] = relationship(back_populates="buys")
    buy: Mapped["Buy"] = relationship(back_populates="books")

    def __str__(self) -> str:
        return (
            f"book id: {self.book_id}, buy id: {self.buy_id}\n" f"amount: {self.amount}"
        )


class Buy(Base):
    __tablename__ = "buy"

    id: Mapped[int] = mapped_column(primary_key=True)
    buy_description: Mapped[str] = mapped_column(Text())
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id", ondelete="CASCADE"))

    client: Mapped["Client"] = relationship(back_populates="client.id")

    books: Mapped[list["BuyBook"]] = relationship(
        back_populates="buy", cascade="all, delete-orphan"
    )
    steps: Mapped[list["BuyStep"]] = relationship(
        back_populates="step", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return self.buy_description
