from modelos import Equipo
from conexiones import Session

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


def crearEquipo(nombre,tipo,stock):
    if nombre.strip() =="":
        print("nombre obligatorio")
        return

    if tipo.strip() == "":
        print("nombre obligatorio")
        return

    if stock <= 0:
        print("el stock debe ser mayor a cero")
        return

    with Session.begin() as session:
        equipo_nuevo = Equipo(nombre = nombre, tipo = tipo , stock = stock)

        session.add(equipo_nuevo)

    print("nuevo equipo agregado")

def listarEquipo():
    with Session as session:
        equipo = session.scalars(select(Equipo).all)

    if len(equipo) == 0:
        print("no hay equipos disponibles")

    else:
            print("\n--- LISTA DE EQUIPOS ---")

            for equipo in equipo:
                print("----------------------")
                print("ID:", equipo.id)
                print("Nombre:", equipo.nombre)
                print("tipo:", equipo.tipo)
                print("stock disponible:", equipo.stock_disponibles)

def buscaridequipo():
    with Session as session:
        equipo = session.scalars(select(Equipo).all)

        if equipo is None:
            print(f"Error: no existe un equipo con ese ID.")
            return None
    
        print("\nequipo encontrado.")
        print(equipo)
        return equipo.id
    
def eliminarequipo(equipo_id):
    with Session() as session:
        try:
            equipo = session.get(equipo, equipo_id)

            if equipo is None:
                print(f"No existe un equipo con ese ID.")
                return False

            session.delete(equipo)
            session.commit()
            print(f"equipo eliminado correctamente.")
            return True

        except SQLAlchemyError as error:
            session.rollback()
            print(f"Error al eliminar equipo")
            return False
