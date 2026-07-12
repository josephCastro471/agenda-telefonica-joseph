"""
Pruebas unitarias para la Agenda Telefónica
"""

import pytest
from src.agenda import (
    validar_nombre,
    validar_telefono,
    registrar_contacto,
    buscar_contacto,
    listar_contactos,
    eliminar_contacto,
    limpiar_agenda,
    contactos
)


# ============================================================
# PRUEBAS: validar_nombre()
# ============================================================
def test_validar_nombre_correcto():
    """Nombres válidos deben retornar True"""
    assert validar_nombre("Juan") is True
    assert validar_nombre("Maria Jose") is True
    assert validar_nombre("Ana") is True


def test_validar_nombre_incorrecto():
    """Nombres inválidos deben retornar False"""
    assert validar_nombre("Juan123") is False   # Números
    assert validar_nombre("Maria!") is False    # Símbolos
    assert validar_nombre("") is False          # Vacío
    assert validar_nombre(123) is False         # Número


# ============================================================
# PRUEBAS: validar_telefono()
# ============================================================
def test_validar_telefono_correcto():
    """Teléfonos válidos (10 dígitos) deben retornar True"""
    assert validar_telefono("0987654321") is True
    assert validar_telefono("1234567890") is True
    assert validar_telefono(1234567890) is True  # Como número


def test_validar_telefono_incorrecto():
    """Teléfonos inválidos deben retornar False"""
    assert validar_telefono("123456789") is False      # 9 dígitos
    assert validar_telefono("12345678901") is False    # 11 dígitos
    assert validar_telefono("1234abc123") is False     # Letras
    assert validar_telefono("") is False               # Vacío
    assert validar_telefono("123456789a") is False     # Letra al final


# ============================================================
# PRUEBAS: registrar_contacto()
# ============================================================
def test_registrar_contacto_exitoso():
    """Registro exitoso de un contacto"""
    limpiar_agenda()
    exito, mensaje = registrar_contacto("Juan", "0987654321")
    assert exito is True
    assert "registrado con éxito" in mensaje
    assert "Juan" in contactos
    assert contactos["Juan"] == "0987654321"


def test_registrar_contacto_nombre_invalido():
    """Registro falla cuando el nombre es inválido"""
    limpiar_agenda()
    exito, mensaje = registrar_contacto("Juan123", "0987654321")
    assert exito is False
    assert "nombre debe contener solo letras" in mensaje


def test_registrar_contacto_telefono_invalido():
    """Registro falla cuando el teléfono es inválido"""
    limpiar_agenda()
    exito, mensaje = registrar_contacto("Juan", "123456789")
    assert exito is False
    assert "10 dígitos" in mensaje


def test_registrar_contacto_duplicado():
    """No se pueden registrar contactos duplicados"""
    limpiar_agenda()
    registrar_contacto("Juan", "0987654321")
    exito, mensaje = registrar_contacto("Juan", "0999999999")
    assert exito is False
    assert "ya existe" in mensaje


# ============================================================
# PRUEBAS: buscar_contacto()
# ============================================================
def test_buscar_contacto_exitoso():
    """Búsqueda exitosa de un contacto existente"""
    limpiar_agenda()
    registrar_contacto("Maria", "0987654321")
    exito, mensaje, telefono = buscar_contacto("Maria")
    assert exito is True
    assert "encontrado" in mensaje
    assert telefono == "0987654321"


def test_buscar_contacto_no_existente():
    """Búsqueda falla cuando el contacto no existe"""
    limpiar_agenda()
    exito, mensaje, telefono = buscar_contacto("Pedro")
    assert exito is False
    assert "No se encontró" in mensaje
    assert telefono is None


def test_buscar_contacto_case_insensitive():
    """Búsqueda es insensible a mayúsculas/minúsculas"""
    limpiar_agenda()
    registrar_contacto("Maria", "0987654321")
    exito, mensaje, telefono = buscar_contacto("maria")
    assert exito is True
    assert telefono == "0987654321"


def test_buscar_contacto_nombre_invalido():
    """Búsqueda falla con nombre inválido"""
    limpiar_agenda()
    exito, mensaje, telefono = buscar_contacto("")
    assert exito is False
    assert "inválido" in mensaje


# ============================================================
# PRUEBAS: listar_contactos()
# ============================================================
def test_listar_contactos_vacio():
    """Listar contactos cuando no hay ninguno"""
    limpiar_agenda()
    resultado = listar_contactos()
    assert isinstance(resultado, dict)
    assert len(resultado) == 0


def test_listar_contactos_con_datos():
    """Listar contactos con datos existentes"""
    limpiar_agenda()
    registrar_contacto("Juan", "0987654321")
    registrar_contacto("Maria", "1234567890")
    resultado = listar_contactos()
    assert len(resultado) == 2
    assert "Juan" in resultado
    assert "Maria" in resultado


# ============================================================
# PRUEBAS: eliminar_contacto()
# ============================================================
def test_eliminar_contacto_exitoso():
    """Eliminar un contacto existente"""
    limpiar_agenda()
    registrar_contacto("Juan", "0987654321")
    exito, mensaje = eliminar_contacto("Juan")
    assert exito is True
    assert "eliminado" in mensaje
    assert "Juan" not in contactos


def test_eliminar_contacto_no_existente():
    """Eliminar falla cuando el contacto no existe"""
    limpiar_agenda()
    exito, mensaje = eliminar_contacto("Pedro")
    assert exito is False
    assert "No se encontró" in mensaje


# ============================================================
# PRUEBAS DE INTEGRACIÓN
# ============================================================
def test_flujo_completo():
    """Flujo completo de registro y búsqueda"""
    limpiar_agenda()

    # Registrar varios contactos
    registrar_contacto("Ana", "0987654321")
    registrar_contacto("Luis", "1234567890")

    # Buscar
    exito, mensaje, telefono = buscar_contacto("Ana")
    assert exito is True
    assert telefono == "0987654321"

    # Listar
    lista = listar_contactos()
    assert len(lista) == 2

    # Eliminar
    eliminar_contacto("Ana")
    assert "Ana" not in contactos
    assert len(contactos) == 1