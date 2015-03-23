# Arquitectura Cliente-Servidor

Ejemplos de diferentes implementaciones de un servidor en Python.

### [Simple tests packets](https://github.com/hcosta/arquitectura-cliente-servidor/tree/master/Python/0_simple_test_packets)

Ejemplo muy sencillo de un servidor implementado en Python capaz de manejar varios clientes. 

* Se guardan los clientes en una lista para saber la cantidad de clientes conectados.
* A cada cliente se le otorga un identificador para diferenciarlo de los demás.
* La gestión del socket de cada cliente se realiza en un hilo específico.
* Cuando un cliente no responde un envío del servidor se cierra su socket.

[![Imagen](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img1.png
)](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img1.png)

### [Simple math server](https://github.com/hcosta/arquitectura-cliente-servidor/tree/master/Python/1_simple_math_server)

Ejemplo simple donde se crea un servidor capaz de solucionar varias operaciones matemáticas como la suma, la resta, la multiplicación y la división. Los clientes le enviarán un paquete con la operación que desean hacer y dos números, en este caso enteros.

* Se guardan los clientes en una lista para saber la cantidad de clientes conectados.
* A cada cliente se le otorga un identificador para diferenciarlo de los demás.
* La gestión del socket de cada cliente se realiza en un hilo específico.
* Cuando un cliente no responde o hay un error se cierra su socket.
* Los paquetes gestionan gracias a la librería **struct** y sus funciones para empaquetar y desempaquetar conjuntos de datos utilizando los formatos descritos en la [documentación](https://docs.python.org/2/library/struct.html#format-characters) de la librería.
* El paquete que envía el cliente está formado por varias variables empaquetadas:
	* Longitud del comando: Un entero con signo que ocupa 4 bytes.
	* El primer valor: Un short que ocupa 2 bytes.
	* El segundo valor: Un short que ocupa 2 bytes.
* Al final del paquete (pero fuera del buffer del struct) se adjunta **el comando**, una string de tamaño indeterminado indicando SUMA, RESTA, MULTIPLICACION o DIVISION. 
* Es muy interesante ver como se envía la cadena de carecteres fuera de un buffer de bytes, cuando se lee a partir del byte 8 (int signed + 2 * short = 8 bytes) hasta la longitud que ocupa.
* Al leer el buffer del cliente el servidor desempaqueta los diferentes datos.
* Una vez los tiene ejecuta la función para saber el resultado de la operación y la envía al cliente.
* Se ha automatizado el sistema para que cada 10 segundos el cliente genere dos valores aleatorios y un comando y los envie al servidor.

[![Imagen](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img2.png
)](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img2.png)

### [Simple positional broadcasting](https://github.com/hcosta/arquitectura-cliente-servidor/tree/master/Python/2_simple_broadcast_test)

Ejemplo en el que los clientes envían al servidor una coordenada (x,y) cada ciertos segundos con una nueva posición. El servidor entonces hace un broadcast de la coordenada de cada cliente en todos los clientes. Es una idea a como podría funcionar una futura implementación de posicionamiento en un simple juego online.

* Se guardan los clientes en una lista para saber la cantidad de clientes conectados.
* A cada cliente se le otorga un identificador para diferenciarlo de los demás.
* La gestión del socket de cada cliente se realiza en un hilo específico.
* Cuando un cliente no responde o hay un error se cierra su socket.
* Desde el cliente se envía una coordenada en dos valores de tipo **short**, cada uno de 2bytes empaquetados con la librería struct. Se hace desde un hilo individual que ejecuta una función recursiva que altera las posiciones x e y -1,0,+1 aleatoriamente cada vez que se envía.
* El resto del cliente queda en espera de ir leyendo el buffer local (con el broadcast).
* Para gestionar el broadcast el servidor envía el paquete a todos los clientes utilizando un loop, y si alguno no funciona le cierra el socket.

[![Imagen](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img3.png
)](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img3.png)
