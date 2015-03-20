# Arquitectura Cliente-Servidor

Ejemplos de diferentes implementaciones en diferentes lenguajes aplicando principios comunes.

## Python

### [Simple tests packets](https://github.com/hcosta/arquitectura-cliente-servidor/tree/master/Python/0_simple_test_packets)

Ejemplo muy sencillo de un servidor implementado en Python capaz de manejar varios clientes. 

* Se guardan los clientes en una lista para saber la cantidad de clientes conectados.
* A cada cliente se le otorga un identificador para diferenciarlo de los demás.
* La gestión del socket de cada cliente se realiza en un hilo específico.
* Cuando un cliente no responde un envío del servidor se cierra su socket.

[![Imagen](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img1.png
)](https://github.com/hcosta/arquitectura-cliente-servidor/raw/master/Python/Screens/img1.png)