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

# ==================== VALIDAR NOMBRE ====================
def test_validar_nombre_correcto():
    assert validar_nombre("Juan") is True
    assert validar_nombre("Maria Jose") is True

def test_validar_nombre_incorrecto():
    assert validar_nombre("Juan123") is False
    assert validar_nombre("") is False
    assert validar_nombre(123) is False

# ==================== VALIDAR TELÉFONO ====================
def test_validar_telefono_correcto():
    assert validar_telefono("0987654321") is True
    assert validar_telefono(1234567890) is True

def test_validar_telefono_incorrecto():
    assert validar_telefono("123456789") is False
    assert validar_telefono("12345678901") is False
    assert validar_telefono("") is False

# ==================== REGISTRAR CONTACTO ====================
def test_registrar_contacto_exitoso():
    limpiar_agenda()
    exito, mensaje = registrar_contacto("Juan", "0987654321")
    assert exito is True
    assert "registrado" in mensaje
    assert "Juan" in contactos

def test_registrar_contacto_nombre_invalido():
    limpiar_agenda()
    exito, mensaje = registrar_contacto("Juan123", "0987654321")
    assert exito is False
    assert "letras" in mensaje

def test_registrar_contacto_telefono_invalido():
    limpiar_agenda()
    exito, mensaje = registrar_contacto("Juan", "123456789")
    assert exito is False
    assert "10 dígitos" in mensaje

def test_registrar_contacto_duplicado():
    limpiar_agenda()
    registrar_contacto("Juan", "0987654321")
    exito, mensaje = registrar_contacto("Juan", "0999999999")
    assert exito is False
    assert "ya existe" in mensaje

# ==================== BUSCAR CONTACTO ====================
def test_buscar_contacto_exitoso():
    limpiar_agenda()
    registrar_contacto("Maria", "0987654321")
    exito, mensaje, telefono = buscar_contacto("Maria")
    assert exito is True
    assert telefono == "0987654321"

def test_buscar_contacto_no_existente():
    limpiar_agenda()
    exito, mensaje, telefono = buscar_contacto("Pedro")
    assert exito is False
    assert "No se encontró" in mensaje

def test_buscar_contacto_case_insensitive():
    limpiar_agenda()
    registrar_contacto("Maria", "0987654321")
    exito, mensaje, telefono = buscar_contacto("maria")
    assert exito is True

def test_buscar_contacto_nombre_invalido():
    limpiar_agenda()
    exito, mensaje, telefono = buscar_contacto("")
    assert exito is False

# ==================== LISTAR CONTACTOS ====================
def test_listar_contactos_vacio():
    limpiar_agenda()
    resultado = listar_contactos()
    assert len(resultado) == 0

def test_listar_contactos_con_datos():
    limpiar_agenda()
    registrar_contacto("Juan", "0987654321")
    registrar_contacto("Maria", "1234567890")
    resultado = listar_contactos()
    assert len(resultado) == 2

# ==================== ELIMINAR CONTACTO ====================
def test_eliminar_contacto_exitoso():
    limpiar_agenda()
    registrar_contacto("Juan", "0987654321")
    exito, mensaje = eliminar_contacto("Juan")
    assert exito is True
    assert "Juan" not in contactos

def test_eliminar_contacto_no_existente():
    limpiar_agenda()
    exito, mensaje = eliminar_contacto("Pedro")
    assert exito is False

# ==================== FLUJO COMPLETO ====================
def test_flujo_completo():
    limpiar_agenda()
    registrar_contacto("Ana", "0987654321")
    registrar_contacto("Luis", "1234567890")
    exito, mensaje, telefono = buscar_contacto("Ana")
    assert exito is True
    assert len(listar_contactos()) == 2
    eliminar_contacto("Ana")
    assert len(listar_contactos()) == 1