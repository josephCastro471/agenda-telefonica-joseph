"""
Aplicación de Agenda Telefónica
Permite registrar, buscar, listar y eliminar contactos desde la consola
"""

from src.agenda import (
    registrar_contacto,
    buscar_contacto,
    listar_contactos,
    eliminar_contacto,
    limpiar_agenda,
    contactos
)


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 40)
    print("      📒 AGENDA TELEFÓNICA")
    print("=" * 40)
    print("1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Listar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Limpiar agenda (todos los contactos)")
    print("6. Salir")
    print("=" * 40)


def registrar():
    """Registra un nuevo contacto"""
    print("\n--- REGISTRAR CONTACTO ---")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono (10 dígitos): ").strip()

    exito, mensaje = registrar_contacto(nombre, telefono)
    if exito:
        print(f"✅ {mensaje}")
    else:
        print(f"❌ {mensaje}")


def buscar():
    """Busca un contacto por nombre"""
    print("\n--- BUSCAR CONTACTO ---")
    nombre = input("Nombre a buscar: ").strip()

    exito, mensaje, telefono = buscar_contacto(nombre)
    if exito:
        print(f"✅ {mensaje}")
        print(f"📞 Teléfono: {telefono}")
    else:
        print(f"❌ {mensaje}")


def listar():
    """Lista todos los contactos"""
    print("\n--- LISTA DE CONTACTOS ---")
    lista = listar_contactos()

    if not lista:
        print("📭 La agenda está vacía.")
    else:
        print(f"📋 Total de contactos: {len(lista)}")
        print("-" * 30)
        for nombre, telefono in lista.items():
            print(f"  👤 {nombre}")
            print(f"  📞 {telefono}")
            print("-" * 30)


def eliminar():
    """Elimina un contacto"""
    print("\n--- ELIMINAR CONTACTO ---")
    nombre = input("Nombre del contacto a eliminar: ").strip()

    exito, mensaje = eliminar_contacto(nombre)
    if exito:
        print(f"✅ {mensaje}")
    else:
        print(f"❌ {mensaje}")


def limpiar():
    """Limpia todos los contactos"""
    print("\n--- LIMPIAR AGENDA ---")
    confirmar = input("¿Seguro que quieres eliminar TODOS los contactos? (s/n): ").strip().lower()

    if confirmar == 's':
        limpiar_agenda()
        print("✅ Agenda limpiada correctamente.")
    else:
        print("❌ Operación cancelada.")


def main():
    """Función principal"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            registrar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            listar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            limpiar()
        elif opcion == "6":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()