from sqlalchemy import String,  Integer, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Equipo(Base):
    __tablename__ = "equipo"
    __table_args__ = (
        CheckConstraint("stock_disponible >=0",name="ck_stock")
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(30), nullable=False)
    tipo: Mapped[str] = mapped_column(String(30), nullable=False)
    stock_disponible: Mapped[int] = mapped_column(Integer,nullable=False)

class Estudiante(Base):
    __tablename__ = "estudiante"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(30), nullable=False)
    correo: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)


class Prestamo(Base):
    __tablename__ = "prestamo"
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="ck_cantidad")
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    equipo_id: Mapped[int] = mapped_column(ForeignKey("equipo.id"), nullable=False)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiante.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    cantidad: Mapped[int] = mapped_column (nullable=False)
    estado: Mapped[int] = mapped_column(nullable=False)