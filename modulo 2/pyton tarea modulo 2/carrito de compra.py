class ListaCompras:
    def _init_(self):
        self.items = []
    
    def agregar_item(self, item, cantidad=1):
        """Añade un item a la lista de compras"""
        self.items.append({"item": item.lower(), "cantidad": cantidad})
        print(f"Añadido: {cantidad} x {item}")
    
    def eliminar_item(self, item):
        """Elimina un item de la lista"""
        item = item.lower()
        for i, producto in enumerate(self.items):
            if producto["item"] == item:
                del self.items[i]
                print(f"Eliminado: {producto['cantidad']} x {producto['item']}")
                return
        print(f"{item} no encontrado")
    
    def mostrar_lista(self):
        """Muestra todos los items"""
        if not self.items:
            print("Tu lista de compras está vacía.")
            return
        
        print("\nTu lista de compras:")
        for i, producto in enumerate(self.items, 1):
            print(f"{i}. {producto['cantidad']} x {producto['item'].capitalize()}")
    
    def editar_cantidad(self, item, nueva_cantidad):
        """Edita la cantidad de un item existente"""
        item = item.lower()
        for producto in self.items:
            if producto["item"] == item:
                producto["cantidad"] = nueva_cantidad
                print(f"Actualizado: {nueva_cantidad} x {item}")
                return
        print(f" {item} no encontrado en la lista")
    
    def guardar_lista(self, archivo="lista_compras.txt"):
        """Guarda la lista en un archivo de texto"""
        with open(archivo, "w") as f:
            for producto in self.items:
                f.write(f"{producto['item']},{producto['cantidad']}\n")
        print(f"Lista guardada{archivo}")
    
    def cargar_lista(self, archivo="lista_compras.txt"):
        """Carga la lista desde un archivo de texto"""
        try:
            with open(archivo, "r") as f:
                self.items = []
                for linea in f:
                    item, cantidad = linea.strip().split(",")
                    self.items.append({"item": item, "cantidad": int(cantidad)})
            print(f"Lista cargada desde {archivo}")
        except FileNotFoundError:
            print(" Archivo no encontrado, error")


def main():
    lista = ListaCompras()
    
    # Intenta cargar una lista existente al iniciar
    lista.cargar_lista()
    
    while True:
        print("\n" + "="*30)
        print("menu de la lista")
        print("1. Ver lista")
        print("2. Añadir item")
        print("3. Eliminar item")
        print("4. Editar cantidad")
        print("5. Guardar lista")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            lista.mostrar_lista()
        elif opcion == "2":
            item = input("Ingresa el nombre del producto: ")
            try:
                cantidad = int(input("Ingresa la cantidad: ") or 1)
                lista.agregar_item(item, cantidad)
            except ValueError:
                print(" La cantidad debe ser un número")
        elif opcion == "3":
            item = input("Ingresa el nombre del producto a eliminar: ")
            lista.eliminar_item(item)
        elif opcion == "4":
            item = input("Ingresa el nombre del producto a editar: ")
            try:
                nueva_cant = int(input("Ingresa la nueva cantidad: "))
                lista.editar_cantidad(item, nueva_cant)
            except ValueError:
                print(" La cantidad debe ser un número")
        elif opcion == "5":
            lista.guardar_lista()
        elif opcion == "6":
            print("adios")
            break
        else:
            print("Opción no válida. Por favor elige del 1 al 6.")


if __name__=="__main__":main()