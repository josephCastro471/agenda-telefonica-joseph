"""
Agenda Telefónica - Módulo principal
"""

contactos = {}

def validar_nombre(nombre):
    if not nombre or not isinstance(nombre, str):
        return False
    return all(c.isalpha() or c.isspace() for c in nombre)

def validar_telefono(telefono):
    if not telefono:
        return False
    telefono_str = str(telefono)
    return len(telefono_str) == 10 and telefono_str.isdigit()

def registrar_contacto(nombre, telefono):
    if not validar_nombre(nombre):
        return False, "Error: El nombre debe contener solo letras y espacios"
    if not validar_telefono(telefono):
        return False, "Error: El teléfono debe tener exactamente 10 dígitos numéricos"
    if nombre in contactos:
        return False, f"Error: El contacto '{nombre}' ya existe"
    contactos[nombre] = str(telefono)
    return True, f"Contacto '{nombre}' registrado con éxito"

def buscar_contacto(nombre):
    if not nombre or not isinstance(nombre, str):
        return False, "Error: Nombre inválido", None
    nombre_buscar = nombre.strip()
    for key in contactos:
        if key.lower() == nombre_buscar.lower():
            return True, f"Contacto encontrado", contactos[key]
    return False, f"No se encontró el contacto '{nombre}'", None

def listar_contactos():
    return contactos.copy()

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        return True, f"Contacto '{nombre}' eliminado"
    return False, f"No se encontró el contacto '{nombre}'"

def limpiar_agenda():
    contactos.clear()