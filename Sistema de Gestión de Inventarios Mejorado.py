import os


class Producto:
    """
    Representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    """
    Gestiona el inventario de productos.
    """

    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde un archivo al iniciar el programa.
        """
        if not os.path.exists(self.archivo):
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            open(self.archivo, 'w').close()  # Crea un archivo vacío si no existe
            return

        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado exitosamente desde el archivo.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda los productos actuales en el archivo.
        """
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(
                        f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado exitosamente en el archivo.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return False
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado con éxito.")
        self.guardar_inventario()  # Guardar cambios en el archivo
        return True

    def eliminar_producto(self, id_producto):
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id_producto:
                del self.productos[i]
                print(f"Producto con ID {id_producto} eliminado con éxito.")
                self.guardar_inventario()  # Guardar cambios en el archivo
                return True
        print(f"Error: No se encontró ningún producto con ID {id_producto}.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado con éxito.")
                self.guardar_inventario()  # Guardar cambios en el archivo
                return True
        print(f"Error: No se encontró ningún producto con ID {id_producto}.")
        return False

    def buscar_producto(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(producto)


def menu(inventario):
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Error: Ingrese un valor válido para ID, cantidad y precio.")

        elif opcion == '2':
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == '3':
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (o deje en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio (o deje en blanco para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Ingrese un valor válido para ID, cantidad y precio.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    inventario = Inventario()
    menu(inventario)

