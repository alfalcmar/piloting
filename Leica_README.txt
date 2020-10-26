Pasos uso Leica:

1.	Enroscar la Leica al trípode
2.	Encenderla y quitarle el tapón a la cámara
3.	Calibrar la burbuja usando las ruedas negras laterales
4.	Pulsar F1 n veces hasta que salga Crear nuevo trabajo o Ir a trabajar
5.	Entrar en el trabajo creado: PILOTING
6.	Pulsar I para terminar de ajustar bien el centrado de la burbuja
7.	Pulsar en Ir a trabajar -> estacionar -> orientar (antes pulsar en medir sin reflector)
8.	Poner ID espalda = origen y coincidir los ejes con el Norte (esto último solo en caso de cerrar el bucle de control con la Leica)
9.	Comprobar en Instrumento -> Conexiones -> Todas las conexiones que está puesto TS RS232
10.	Conectar cable Leica con PC
11.	Apuntar al prisma usando la mirilla (usar rueda derecha para zoom)
12.	Activar lock para que la Leica detecte el prisma
13.	En el PC: lanzar ./tools/leica_control/leica_control 
14.	Poner parámetros 1 (comunicación UDP) y 8000
15.	Lanzar tsbridge para obtener topic de la pose del prisma
