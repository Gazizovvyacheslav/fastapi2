
from app.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column

class Task(Base):

    __tablename__ = "tasks"

    # описываем таблицу
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(primary_key=False)
    description: Mapped[str | None] = mapped_column(primary_key=False, nullable=True)
    is_done: Mapped[bool] = mapped_column(primary_key=False, default=False)

    