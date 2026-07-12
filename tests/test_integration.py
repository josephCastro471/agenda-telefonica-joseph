"""
Pruebas de Integración para la Agenda Telefónica
Verifican que varias funciones trabajan juntas correctamente
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


def test_integracion_registro_y_busqueda():
    """Registrar un contacto y luego buscarlo funciona correctamente"""
    limpiar_agenda()
    
    # 1. Registrar
    exito, mensaje = registrar_contacto("Carlos", "0987654321")
    assert exito is True
    
    # 2. Buscar (integración)
    exito2, mensaje2, telefono = buscar_contacto("Carlos")
    assert exito2 is True
    assert telefono == "0987654321"


def test_integracion_registro_y_lista():
    """Registrar varios contactos y listarlos funciona correctamente"""
    limpiar_agenda()
    
    registrar_contacto("Ana", "0987654321")
    registrar_contacto("Luis", "1234567890")
    
    lista = listar_contactos()
    assert len(lista) == 2
    assert "Ana" in lista
    assert "Luis" in lista


def test_integracion_registro_eliminar_y_buscar():
    """Registrar, eliminar y verificar que ya no existe"""
    limpiar_agenda()
    
    registrar_contacto("Pedro", "0987654321")
    assert "Pedro" in contactos
    
    exito, mensaje = eliminar_contacto("Pedro")
    assert exito is True
    
    exito2, mensaje2, telefono = buscar_contacto("Pedro")
    assert exito2 is False
    assert "No se encontró" in mensaje2


def test_integracion_registro_duplicado():
    """Intentar registrar duplicado y verificar que no se duplica"""
    limpiar_agenda()
    
    registrar_contacto("Juan", "0987654321")
    
    exito, mensaje = registrar_contacto("Juan", "0999999999")
    assert exito is False
    assert "ya existe" in mensaje
    
    lista = listar_contactos()
    assert len(lista) == 1
    assert contactos["Juan"] == "0987654321"


def test_integracion_busqueda_case_insensitive():
    """Búsqueda insensible a mayúsculas y minúsculas"""
    limpiar_agenda()
    
    registrar_contacto("Maria", "0987654321")
    
    exito, mensaje, telefono = buscar_contacto("maria")
    assert exito is True
    assert telefono == "0987654321"
    
    exito2, mensaje2, telefono2 = buscar_contacto("MaRiA")
    assert exito2 is True
    assert telefono2 == "0987654321"


def test_integracion_flujo_completo():
    """Flujo completo: registro → búsqueda → lista → eliminación"""
    limpiar_agenda()
    
    registrar_contacto("Maria", "0987654321")
    registrar_contacto("Jose", "1234567890")
    registrar_contacto("Ana", "1122334455")
    
    exito, mensaje, telefono = buscar_contacto("Maria")
    assert exito is True
    assert telefono == "0987654321"
    
    lista = listar_contactos()
    assert len(lista) == 3
    
    eliminar_contacto("Ana")
    assert "Ana" not in contactos
    assert len(contactos) == 2
    
    exito2, mensaje2, telefono2 = buscar_contacto("Ana")
    assert exito2 is False