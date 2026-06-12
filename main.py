from abc import ABC, abstractmethod

class Videojuego(ABC):
    def __init__(self, nombre, precio, desarrollador):
        self.__nombre = nombre
        self.__precio = precio
        self.__desarrollador = desarrollador

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_desarrollador(self):
        return self.__desarrollador

    @abstractmethod
    def mostrar_detalle(self):
        pass

class JuegoAccion(Videojuego):
    def __init__(self, nombre, precio, desarrollador, dificultad):
        super().__init__(nombre, precio, desarrollador)
        self.__dificultad = dificultad

    def mostrar_detalle(self):
        return (
            f"[ACCIÓN] Nombre: {self.get_nombre()} | "
            f"Precio: ${self.get_precio()} | "
            f"Desarrollador: {self.get_desarrollador()} | "
            f"Dificultad: {self.__dificultad}"
)

class JuegoAventura(Videojuego):
    def __init__(self, nombre, precio, desarrollador, historia):
        super().__init__(nombre, precio, desarrollador)
        self.__historia = historia

    def mostrar_detalle(self):
        return (
            f"[AVENTURA] Nombre: {self.get_nombre()} | "
            f"Precio: ${self.get_precio()} | "
            f"Desarrollador: {self.get_desarrollador()} | "
            f"Historia: {self.__historia}"
)

class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__biblioteca = []

    def get_nombre(self):
        return self.__nombre

    def agregar_juego(self, juego):
        self.__biblioteca.append(juego)

    def mostrar_biblioteca(self):
        if len(self.__biblioteca) == 0:
            print("No posee videojuegos.")
        else:
            print(f"Biblioteca de {self.__nombre}")
            for juego in self.__biblioteca:
                print(juego.mostrar_detalle())

    def total_gastado(self):
        total = 0
        for juego in self.__biblioteca:
            total += juego.get_precio()
        return total

class TiendaVideojuegos:
    def __init__(self):
        self.__videojuegos = []
        self.__jugadores = []

    def registrar_videojuego(self, videojuego):
        self.__videojuegos.append(videojuego)

    def registrar_jugador(self, jugador):
        self.__jugadores.append(jugador)

    def mostrar_videojuegos(self):
        if len(self.__videojuegos) == 0:
            print("No existen videojuegos registrados.")
        else:
            print("___ VIDEOJUEGOS ___")
            for juego in self.__videojuegos:
                print(juego.mostrar_detalle())

    def mostrar_jugadores(self):
        if len(self.__jugadores) == 0:
            print("No existen jugadores registrados.")
        else:
            print("___ JUGADORES ___")
            for jugador in self.__jugadores:
                print(jugador.get_nombre())

    def buscar_videojuego(self, nombre):
        for juego in self.__videojuegos:
             if juego.get_nombre().lower() == nombre.lower():
                return juego
        return None

    def buscar_jugador(self, nombre):
        for jugador in self.__jugadores:
            if jugador.get_nombre().lower() == nombre.lower():
                return jugador
        return None

    def comprar_videojuego(self, nombre_jugador, nombre_juego):
        jugador = self.buscar_jugador(nombre_jugador)
        juego = self.buscar_videojuego(nombre_juego)

        if jugador and juego:
            jugador.agregar_juego(juego)
            print("Compra realizada correctamente.")
        else:
            print("Jugador o videojuego no encontrado.")

tienda = TiendaVideojuegos()

while True:

    print("________________________")
    print(" SISTEMA DE VIDEOJUEGOS ")
    print("________________________")
    print("1. Registrar información")
    print("2. Mostrar información")
    print("3. Ejecutar acción")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        print("1. Registrar videojuego")
        print("2. Registrar jugador")

        sub = input("Seleccione: ")

        if sub == "1":

            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            desarrollador = input("Desarrollador: ")

            print("Tipo:")
            print("1. Acción")
            print("2. Aventura")

            tipo = input("Seleccione: ")

            if tipo == "1":
                dificultad = input("Dificultad: ")

                juego = JuegoAccion(
                    nombre,
                    precio,
                    desarrollador,
                    dificultad
                )

            else:
                historia = input("Nivel de historia: ")

                juego = JuegoAventura(
                    nombre,
                    precio,
                    desarrollador,
                    historia
                )

            tienda.registrar_videojuego(juego)

            print("Videojuego registrado.")

        elif sub == "2":

            nombre = input("Nombre del jugador: ")

            jugador = Jugador(nombre)

            tienda.registrar_jugador(jugador)

            print("Jugador registrado.")

    elif opcion == "2":

        print("1. Mostrar videojuegos")
        print("2. Mostrar jugadores")
        print("3. Mostrar biblioteca jugador")

        sub = input("Seleccione: ")

        if sub == "1":
            tienda.mostrar_videojuegos()

        elif sub == "2":
            tienda.mostrar_jugadores()

        elif sub == "3":
            nombre = input("Nombre jugador: ")

            jugador = tienda.buscar_jugador(nombre)

            if jugador:
                jugador.mostrar_biblioteca()
            else:
                print("Jugador no encontrado.")

    elif opcion == "3":

        print("1. Comprar videojuego")
        print("2. Calcular dinero gastado")

        sub = input("Seleccione: ")

        if sub == "1":

            nombre = input("Nombre jugador: ")
            nombre_juego = input("Nombre videojuego: ")

            tienda.comprar_videojuego(
                nombre,
                nombre_juego
            )

        elif sub == "2":

            nombre = input("Nombre jugador: ")

            jugador = tienda.buscar_jugador(nombre)

            if jugador:
                print(
                    f"Total gastado: ${jugador.total_gastado()}"
                )
            else:
                print("Jugador no encontrado.")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")