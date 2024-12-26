from sqlalchemy import CheckConstraint, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id", ondelete="CASCADE"))
    price: Mapped[int] = mapped_column(
        CheckConstraint("price > 0", name="check_price_positive")
    )
    amount: Mapped[int] = mapped_column(
        CheckConstraint("amount > 0", name="check_amount_positive")
    )

    author: Mapped["Author"] = relationship(back_populates="author.id")
    genre: Mapped["Genre"] = relationship(back_populates="genre.id")

    buys: Mapped[list["BuyBook"]] = relationship(
        back_populates="book", cascade="all, delete-orphan"
    )
