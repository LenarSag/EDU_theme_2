from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_client: Mapped[str] = mapped_column(String(50))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id", ondelete="CASCADE"))

    buys: Mapped[list["Buy"]] = relationship(
        back_populates="client", cascade="all, delete-orphan"
    )
    city: Mapped["City"] = relationship(back_populates="clients")

    def __str__(self) -> str:
        return self.name_client
