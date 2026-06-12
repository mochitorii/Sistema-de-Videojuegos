# Sistema-de-Videojuegos
El sistema presentado puede registrar y mostrar tanto videojuegos en venta como jugadores, el sistema está dirigido a tiendas digitales o administradores que requieran registrar videojuegos.
Conceptos utilizados:
  Encapsulamiento: Los atributos principales de las clases se encuentran privados mediante "__" y se accede a ellos utilizando métodos públicos.

  Herencia: Las clases JuegoAccion y JuegoAventura heredan de la clase Videojuego.

  Abstracción: La clase Videojuego es abstracta y obliga a implementar el método mostrar_detalle().

  Polimorfismo: El método mostrar_detalle() se implementa de forma diferente en JuegoAccion y JuegoAventura.

Criterios de aceptación:
  - Registrar videojuegos
  - Registrar jugadores.
  - Mostrar videojuegos.
  - Mostrar jugadores.
  - Comprar videojuegos.
  - Calcular total gastado.

Pruebas de usuario:
*Prueba 1*
  Acción: Registrar videojuego.
  Resultado esperado: Guardar videojuego.
  Resultado obtenido: Videojuego guardado correctamente.
  Cumple: Sí.

*Prueba 2*
  Acción: Registrar jugador.
  Resultado esperado: Guardar jugador.
  Resultado obtenido: Jugador guardado correctamente.
  Cumple: Sí.

*Prueba 3*
  Acción: Comprar videojuego.
  Resultado esperado: Agregar videojuego a biblioteca.
  Resultado obtenido: Compra realizada correctamente.
  Cumple: Sí.

*Prueba 4*
  Acción: Calcular dinero gastado.
  Resultado esperado: Mostrar suma total.
  Resultado obtenido: Total calculado correctamente.
  Cumple: Sí.

Aclaraciones: La base del sistema fue hecho por IA solo por requerimiento de una orientación, varias otras partes fueron extraidas de guías con revisiones de IA en pequeños errores.
