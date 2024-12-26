from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.models.base import Base


class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str] = mapped_column(String(50))

    books: Mapped[list["Book"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return self.name_author
