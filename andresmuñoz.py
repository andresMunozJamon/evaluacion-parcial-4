class SistemaReservas:
    def __init__(self):
        self.stock_total = 20  # Número total de pares disponibles
        self.reservas = {}  # Diccionario para almacenar las reservas

    def reservar_zapatillas(self):
        nombre = input("Nombre del comprador: ")
        palabra_clave = input("Digite la palabra secreta para confirmar la reserva: ")
        if palabra_clave == "EstoyEnListaDeReserva":
            if self.stock_total > 0:
                if nombre not in self.reservas:
                    self.reservas[nombre] = 1  # Reserva 1 par por defecto
                else:
                    self.reservas[nombre] += 1  # Si ya tiene reserva, aumenta la cantidad
                self.stock_total -= 1
                print(f"Reserva realizada exitosamente para {nombre}.")
            else:
                print("No hay pares disponibles para reservar.")
        else:
            print("Error: palabra clave incorrecta. Reserva no realizada.")

    def buscar_zapatillas_reservadas(self):
        nombre = input("Nombre del comprador a buscar: ")
        if nombre in self.reservas:
            cantidad = self.reservas[nombre]
            print(f"Reserva encontrada: {nombre} - {cantidad} par(es) (estándar).")
            desea_vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
            if desea_vip == 's':
                if self.stock_total > 0:
                    self.reservas[nombre] = 2  # Actualiza la reserva a VIP con 2 pares
                    self.stock_total -= 1
                    print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
                else:
                    print("no hay pares disponibles para VIP.")
        else:
            print("No se encontró ninguna reserva con ese nombre.")

    def ver_stock_reservas(self):
        pares_reservados = sum(self.reservas.values())
        pares_disponibles = self.stock_total
        print(f"Pares reservados: {pares_reservados}")
        print(f"Pares disponibles: {pares_disponibles}")

    def salir(self):
        print("Programa terminado")

def main():
    sistema = SistemaReservas()

    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Ver stock de reservas")
        print("4.- Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            sistema.reservar_zapatillas()
        elif opcion == "2":
            sistema.buscar_zapatillas_reservadas()
        elif opcion == "3":
            sistema.ver_stock_reservas()
        elif opcion == "4":
            sistema.salir()
            break
        else:
            print("Debe ingresar una opción válida ")

if __name__ == "__main__":
    main()
