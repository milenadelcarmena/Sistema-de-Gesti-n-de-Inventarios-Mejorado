# Sistema-de-Gesti-n-de-Inventarios-Mejorado
(Semana 10) Tarea: Manipulación de archivos y manejo de excepciones


Explicación de las Modificaciones Realizadas


1. Carga del Inventario
Se agregó un método cargar_inventario que se llama al inicializar la clase Inventario. Este método intenta leer desde un archivo inventario.txt y carga los productos existentes.


2. Guardado del Inventario
Se incorporó un método guardar_inventario que guarda todos los productos actuales en inventario.txt. Este método es llamado cada vez que se agrega, actualiza o elimina un producto.


3. Manejo de Excepciones
Se implementaron bloques try-except para manejar errores como FileNotFoundError y PermissionError, asegurando que los problemas durante la lectura o escritura sean informados al usuario.


4. Interfaz de Usuario
Se incluyeron mensajes informativos sobre la carga y guardado exitoso del inventario.

