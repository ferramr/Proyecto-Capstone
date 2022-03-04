# Proyecto-Capstone
En este repositorio se encuentra la documentación y programas de desarrollo de un experimento de física consistente en el manejo de un plano inclinado con acceso remoto, como proyecto desarrollado para el Diplomado de IoT de Samsung Innovation Campus 2021/2022

RESUMEN
			
En este proyecto se propone la realización de un experimento de física básica: el plano inclinado sobre el cual se desliza una esfera de vidrio.

El experimento del plano inclinado podrá ser observado de forma remota mediante un servidor de video. El usuario podrá ajustar el ángulo de inclinación a través de una interfáz gráfica, en donde también se desplegarán los resultados del experimento mediante curvas de desplazamiento, velocidad y aceleración.

La detección del movimiento de la esfera sobre el plano se realizará con técnicas de visión por computadora sobre cada una de las tramas de video capturado con una cámara web.

El diagrama a bloques general del proyecto se muestra en la Figura 1.

![image](https://user-images.githubusercontent.com/87343531/156823978-4a4832ce-23f9-4245-bf09-b7114d566e71.png)
 
Figura 1. Diagrama a bloques general del proyecto

De acuerdo a este diagrama a bloques, el USUARIO puede acceder al LABORATORIO REMOTO a través de una estructura de comunicación por Internet mediante el concepto de la IoT, utilizando un bróker público mediante el protocolo MQTT.

La actividad del usuario se reduce a seleccionar un determinado ángulo de inclinación del plano inclinado y, presionando un botón, enviar este parámetro al laboratorio remoto a través del bróker público.

En el laboratorio remoto se encuentra el sistema formado por el plano inclinado, una esfera y una cámara web. El plano inclinado se coloca automáticamente con el ángulo de inclinación solicitado por el usuario, la esfera inicia su desplazamiento y una cámara web captura todo el proceso del experimento para, posteriormente, devolver al usuario los resultados de dicho experimento.

En la figura 2 se muestra el diagrama a bloques detallado del proyecto.

![image](https://user-images.githubusercontent.com/87343531/156824026-ae34a20f-3cbc-4a94-a78f-b2e1878d0ff1.png)

En la figura anterior se pueden observar los siguientes módulos:

1-USUARIO.- El usuario participa en las siguientes tres funciones:
a.	Controla de manera remota el ángulo de inclinación del plano inclinado
b.	Recibe visualmente la información sobre el estado del experimento
c.	Recibe visualmente los resultados del experimento.

2-DASHBOARD.- En este bloque se encuentra una computadora corriendo NODE-RED y presentando al USUARIO (1) un dashboard con la información visual necesaria para realizar las funciones de controlar la inclinación del plano inclinado y recibir los resultados del experimento realizado en el LABORATORIO REMOTO.

3-BROKER.- Este módulo se encarga de comunicar bidireccionalmente a los módulos  del 2-DASHBOARD (2) y del LABORATORIO REMOTO, a través del bloque COMPUTADORA (4), a través de un BROKER (3) público mediante el protocolo MQTT, dentro del contexto de la  IoT.

4-COMPUTADORA.- En la computadora se encuentra activo un programa en pyhton, el cual se encarga de realizar varias funciones como son: establecer la comunicación bidireccional con el BROKER (3) público, enviar la información necesaria al MICROCONTROLADOR (5) para llevar a cabo el experimento y procesar la información recibida a través de la CAMARA WEB (8).

5-MICROCONTROLADOR.- El programa residente en el microcontrolador se encarga de manejar un SERVOMOTOR (6) y un SOLENOIDE (7). Ambos dispositivos se encuentran acoplados a los extremos del plano inclinado.

6-SERVOMOTOR.- El servomotor se encarga de controlar la inclinación del plano inclinado.

7-SOLENOIDE.- El solenoide se encarga de capturar y liberar la esfera que se deslizará sobre el plano inclinado.

8-CAMARA WEB.- La cámara WEB se encarga de capturar los tramas de video de todo el experimento con el objetivo de que el programa residente en la computadora del laboratorio remoto, pueda procesar dichas imágenes.

