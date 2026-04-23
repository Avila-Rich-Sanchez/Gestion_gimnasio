# 🏋️ GymFlow - Sistema de Gestión de Membresías

Un asistente de escritorio desarrollado en **Python** para la gestión eficiente de clientes y control de asistencias en gimnasios pequeños o centros de entrenamiento. 

Este proyecto nació de la necesidad de digitalizar el control manual (cuadernos), evitando errores humanos en el conteo de días y facilitando el registro diario.

## 🚀 Características

- **Gestión de Base de Datos:** Uso de SQLite3 para un almacenamiento persistente y seguro de la información de los clientes.
- **Normalización de Datos:** Limpieza automática de nombres (formato Título y sin espacios extra).
- **Control de Membresía:** Sistema inteligente que impide descontar días si el cliente tiene saldo cero.
- **Persistencia Híbrida:** - **SQL:** Para datos críticos (Cédula, nombre, días restantes).
  - **Archivos Planos (.txt):** Registro de asistencias diarias que se mantiene incluso si el programa se cierra.
- **Interfaz de Consola Intuitiva:** Menús claros con validación de errores para evitar cierres inesperados (ValueErrors).

## 🛠️ Tecnologías Usadas

* **Lenguaje:** Python 3.10+
* **Base de Datos:** SQLite3
* **Librerías Estándar:** `os`, `time`, `sqlite3`

## 📋 Funcionalidades

1.  **Añadir Clientes:** Registro con Cédula (ID único), Nombre, Edad y Días válidos.
2.  **Descontar Días:** Búsqueda por Cédula para registrar la entrada del cliente.
3.  **Lista Diaria:** Visualización de todas las personas que asistieron durante la jornada actual.
4.  **Cierre de Jornada:** Opción de limpiar o conservar el registro de asistencia al salir.

## 🔧 Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/Avila-Rich-Sanchez/Gestion_gimnasio.git](https://github.com/Avila-Rich-Sanchez/Gestion_gimnasio.git)
