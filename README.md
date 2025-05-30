# GenBank_Api_Flask

📌 Requerimientos del Proyecto - GenBank

1️⃣ Requerimientos Funcionales
🔹 Gestión de Usuarios
✅ Un usuario debe poder registrarse con su cédula, nombres, apellidos, fecha de nacimiento, correo, número de teléfono, departamento, ciudad, dirección, detalles de la dirección y contraseña.
✅ Un usuario debe poder iniciar sesión utilizando su cédula y contraseña.
✅ Un usuario debe poder cerrar sesión de forma segura.
✅ El sistema debe validar que no haya cédulas, correos y teléfonos duplicados en el registro.

🔹 Gestión de Cuentas Bancarias
✅ Un usuario puede tener una o más cuentas bancarias (ejemplo: cuenta de ahorros y cuenta corriente).
✅ Cada cuenta debe tener un número único, un saldo inicial y un tipo (ahorros o corriente).
✅ Un usuario debe poder consultar el saldo de sus cuentas.
✅ Un usuario puede hacer un depósito a su propia cuenta.
✅ El sistema debe registrar cada depósito con los siguientes datos:
    - Cuenta destino
    - Monto depositado
    - Fecha y hora del depósito
    - Estado (exitoso, fallido)

🔹 Transferencias y Transacciones
✅ Un usuario debe poder transferir dinero a otra cuenta dentro del banco.
✅ El sistema debe validar que el usuario tenga saldo suficiente antes de realizar una transferencia.
✅ Cada transacción debe registrarse con los siguientes datos:
    - Cuenta origen y destino
    - Monto transferido
    - Estado (pendiente, completada, fallida)
    - Fecha de la transacción
✅ Un usuario debe poder ver su historial de transacciones (enviadas y recibidas).
✅ Si una transacción falla (saldo insuficiente, cuenta inexistente), el sistema debe notificar el error.

🔹 Seguridad y Autenticación
✅ Se debe usar hashing de contraseñas para almacenar las credenciales de los usuarios (bcrypt).
✅ Implementar tokens de sesión para mantener la autenticación activa.
✅ Un usuario debe ser desconectado automáticamente si su sesión expira.

🔹 Interfaz de Usuario (Frontend)
✅ Página de inicio con formulario de login y registro.
✅ Panel principal donde el usuario puede:
    - Ver sus cuentas y saldos
    - Hacer transferencias
    - Consultar historial de transacciones
✅ Alertas o notificaciones en caso de errores en las transferencias.

2️⃣ Requerimientos No Funcionales

🔹 Escalabilidad → El sistema debe permitir crecer en número de usuarios y transacciones sin afectar el rendimiento.
🔹 Seguridad → Todas las transacciones deben registrarse con auditoría para prevenir fraudes.
🔹 Rendimiento → Las consultas de saldo y transferencias deben ejecutarse en menos de 2 segundos.
🔹 Experiencia de Usuario → La interfaz debe ser rápida, sencilla y adaptable a dispositivos móviles.
🔹 Consistencia de Datos → Se debe garantizar que no haya transferencias duplicadas o inconsistencias en los saldos.
🔹 Disponibilidad → El sistema debe ser accesible 24/7.
