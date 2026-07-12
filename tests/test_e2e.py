"""
Pruebas End-to-End (E2E) para la Agenda Telefónica
Simulan el flujo completo como lo haría un usuario real
"""

import pytest
from src.agenda import (
    registrar_contacto,
    buscar_contacto,
    listar_contactos,
    eliminar_contacto,
    limpiar_agenda,
    contactos
)


def test_e2e_flujo_usuario_completo():
    """Simula un usuario usando la agenda de principio a fin"""
    limpiar_agenda()
    
    print("\n=== FLUJO DE USUARIO E2E ===")
    
    # 1. Usuario registra un contacto
    print("1. Registrando contacto...")
    exito, mensaje = registrar_contacto("Juan Perez", "0987654321")
    assert exito is True
    print(f"   ✅ {mensaje}")
    
    # 2. Usuario registra otro contacto
    print("2. Registrando otro contacto...")
    exito, mensaje = registrar_contacto("Maria Gomez", "1234567890")
    assert exito is True
    print(f"   ✅ {mensaje}")
    
    # 3. Usuario busca un contacto
    print("3. Buscando contacto...")
    exito, mensaje, telefono = buscar_contacto("Juan Perez")
    assert exito is True
    print(f"   ✅ Contacto encontrado: {telefono}")
    
    # 4. Usuario lista todos los contactos
    print("4. Listando todos los contactos...")
    lista = listar_contactos()
    assert len(lista) == 2
    print(f"   ✅ Contactos: {lista}")
    
    # 5. Usuario elimina un contacto
    print("5. Eliminando contacto...")
    exito, mensaje = eliminar_contacto("Maria Gomez")
    assert exito is True
    print(f"   ✅ {mensaje}")
    
    # 6. Usuario verifica que el contacto fue eliminado
    print("6. Verificando eliminación...")
    exito, mensaje, telefono = buscar_contacto("Maria Gomez")
    assert exito is False
    print(f"   ✅ Contacto eliminado correctamente")
    
    print("=== FLUJO COMPLETO EXITOSO ===")


def test_e2e_escenario_registro_duplicado():
    """Simula que el usuario intenta registrar un contacto duplicado"""
    limpiar_agenda()
    
    registrar_contacto("Carlos", "0987654321")
    
    exito, mensaje = registrar_contacto("Carlos", "0999999999")
    assert exito is False
    assert "ya existe" in mensaje
    
    exito2, mensaje2, telefono = buscar_contacto("Carlos")
    assert telefono == "0987654321"


def test_e2e_escenario_busqueda_insensible():
    """Simula que el usuario busca sin importar mayúsculas/minúsculas"""
    limpiar_agenda()
    
    registrar_contacto("JOSE", "0987654321")
    
    exito, mensaje, telefono = buscar_contacto("jose")
    assert exito is True
    assert telefono == "0987654321"
    
    exito2, mensaje2, telefono2 = buscar_contacto("JoSe")
    assert exito2 is True
    assert telefono2 == "0987654321"


def test_e2e_escenario_agenda_vacia():
    """Simula que el usuario interactúa con una agenda vacía"""
    limpiar_agenda()
    
    lista = listar_contactos()
    assert len(lista) == 0
    
    exito, mensaje, telefono = buscar_contacto("Algo")
    assert exito is False
    assert "No se encontró" in mensaje
    
    exito2, mensaje2 = eliminar_contacto("Algo")
    assert exito2 is False
    assert "No se encontró" in mensaje2


def test_e2e_escenario_multiples_operaciones():
    """Simula un usuario realizando múltiples operaciones"""
    limpiar_agenda()
    
    contactos_prueba = [
        ("Ana", "0987654321"),
        ("Luis", "1234567890"),
        ("Carlos", "1122334455"),
        ("Maria", "5566778899"),
    ]
    
    for nombre, telefono in contactos_prueba:
        exito, mensaje = registrar_contacto(nombre, telefono)
        assert exito is True
    
    lista = listar_contactos()
    assert len(lista) == 4
    
    exito, mensaje, telefono = buscar_contacto("Luis")
    assert exito is True
    assert telefono == "1234567890"
    
    eliminar_contacto("Carlos")
    assert "Carlos" not in contactos
    
    exito2, mensaje2, telefono2 = buscar_contacto("Carlos")
    assert exito2 is False
    
    lista2 = listar_contactos()
    assert len(lista2) == 3