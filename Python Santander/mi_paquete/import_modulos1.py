import mod_operaciones
import mod_funcionalidades


resultado = mod_operaciones.sumar(5, 3)
mod_funcionalidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = mod_funcionalidades.obtener_nombre_usuario()
mod_funcionalidades.imprimir_mensaje(f"Hola, {nombre}!")