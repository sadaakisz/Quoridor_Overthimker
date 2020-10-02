Universidad Peruana de Ciencias Aplicadas
Ingeniería de Software
Complejidad Algorítmica
Ciclo: 2020-2
Profesor: Luis Martín Canaval Sánchez





Trabajo Parcial




Team Overthimker
Integrantes:
Juan Leyva            U201817709
Carlos Mazzarri        U201811947
Héctor Suzuki        U201810782

Contenidos

Introducción     3
Estado del arte  4
Metodología      5
Experimentos     8






Introducción
Este trabajo se está basando en el juego de mesa llamado “Quoridor”. Este es un juego creado oficialmente en Francia el año 1997, aunque se puede hablar de la evolución 
del este desde su primera fase en 1975 creada por Mirko Marchesi. Se puede jugar entre 2 o 4 jugadores y la meta del jugador es llegar al otro lado del tablero según la 
posición que estés (Si comienzas en el norte, debes ir al sur, si comienzas en la derecha debes ir en la izquierda, y viceversa). El tablero parece uno de ajedrez, 
aunque este usa un tablero 9x9. El tablero incluye los 4 peones y 20 “paredes”, las cuales son el truco del juego. 
Las paredes se dividen de 10 si juegan dos jugadores, y de 5 si juegan 4. En cada turno el jugador debe decidir si moverse o poner una pared en el tablero. El jugador
sólo puede moverse una casilla (izquierda, derecha, arriba, abajo), a no ser que se cumplan ciertas condiciones. Las paredes bloquean tanto al oponente como al jugador
que la puso. Finalmente una pared no puede encerrar al peón.
Este juego ha sido usado, como el ajedrez, como un ejemplo de juego de mesa que enseña la importancia de analizar todos los movimientos posibles tanto del jugador como
del contrincante. Debido a ello, varios algoritmos han sido propuestos para poder crear funciones para darle a un peón la habilidad de poder recorrer todos los 
movimientos posibles y elegir el más óptimo posible. Estos algoritmos pueden variar demasiado, tanto en nivel de complejidad como en funcionalidad. Algoritmos basados
desde Fuerza Bruta hasta analizar el tablero como un conjunto de grafos.
En este trabajo se analizará el uso de diferentes tipos de algoritmos para crear un bot que pueda jugar quoridor, en cual por ahora su meta simplemente será ganar 
llegando al otro lado, en el lenguaje de programación Python y con las enseñanzas del curso de Complejidad Algorítmica. Será un “bot” que evite las murallas puestas 
por el jugador y cumpla la misión de completar el juego, mientras analiza todas las opciones posibles mediante algoritmos.




Estado del arte
Al comenzar la investigación sobre Quoridor y la lógica empleada para jugar el juego, nos encontramos con diversos documentos en el internet relacionados al uso de la 
inteligencia artificial para simular seres humanos en los juegos en general. Se aprecia un mayor avance en las inteligencias artificiales enfocadas en los juegos que 
utilizan redes neuronales profundas, como es el caso de AlphaGo para jugar Go. Según Chang, el programa informático de inteligencia artificial logró derrotar al 
campeón regional europeo de Go, Fan Hui, con un margen sorprendente de 5-0. Los desarrolladores detrás de AlphaGo son Google Deepmind, situados en Londres y fundado 
en el 2010 por Demis Hassabis, Shane Legg y Mustafa Suleyman. 
Si nos enfocamos un poco más en los últimos avances tecnológicos centrados en Quoridor, tenemos el papel desarrollado llamado Quoridor agent, por Tsur y Segev de la 
Universidad Hebrea de Jerusalén, el cual describe la lógica básica del juego, como también técnicas para determinar la jugada óptima en un momento determinado. De la 
misma manera, la investigación realizada por ellos nos dan información correspondientes las jugadas de entrada (openings) más comunes para poder comenzar con la 
ventaja al jugar Quoridor. Quizás la parte más importante del documento es la sección de posibles algoritmos y herramientas de programación que se pueden utilizar 
para resolver el problema como minimax, random walker statistics, weighted evaluation features y genetic algorithms.
Estas herramientas se encuentran descritas en el documento mencionado, pero para motivos de la redacción de esta sección del estado del arte, procedo a resumir el 
algoritmo minimax desarrollado en el papel académico. Minimax es un método de decisión recursivo en los juegos de lógica, el cual tiene como objetivo minimizar la 
pérdida máxima esperada, asumiendo en todo momento que los movimientos que pueda realizar el oponente siempre son las más óptimas.
Otro documento relevante en el espacio de Quoridor y la inteligencia artificial empleada para jugarla es Mastering Quoridor, un papel académico realizado por 
Glendenning, el cual describe el juego, la representación del juego, los approaches a tomar en los turnos y el aprendizaje de la inteligencia artificial en los juegos.
De este documento podemos extrapolar información como la utilización del algoritmos Minimax y genéticos, como también pruebas y descubrimientos realizados a lo largo 
del desarrollo de la investigación. Lo más relevante para el presente trabajo son las representaciones mostradas del juego y las ilustraciones incluidas en el 
documento de Glendenning.



Metodología
Para la realización del trabajo estamos utilizando diversas herramientas. Inicialmente, adelantamos una parte del trabajo en un entorno llamado Cocalc, debido a que 
permite un trabajr online, de forma que todos podíamos editar y visualizar un mismo archivo. Posteriormente, tras recibir las pautas del trabajo, nos adaptamos a otro 
conjunto de herramientas, mencionadas a continuación. Usamos Visual Studio Code para el desarrollo del código, en lenguaje Python. Una gran ventaja de Python es la 
variedad de bibliotecas a las que podemos acceder, las cuales facilitan nuestro procedimiento. Un ejemplo de ellas es matplotlib, que usamos para graficar el tablero y 
los peones. El formato de archivos que estamos manejando es Notebooks de Jupyter (.ipynb), 
debido a que nos permiten organizar el código con facilidad, además de separarlo en celdas que pueden ejecutarse de forma individual. Esto nos permite probar el código 
con comodidad. Además, podemos crear Notebooks adicionales para probar ciertas funciones antes de agregarlas al archivo principal, para no cargar demasiado el documento. 
Es importante destacar que estamos trabajando con el paradigma de programación orientada a objetos (POO), creando clases para definir los objetos necesarios, agregando 
los atributos y métodos que consideramos más adecuados. Una vez que realizamos avances y confirmamos que el código funciona correctamente, hacemos nuestros respectivos 
commits a nuestro repositorio de Github, para gestionar de forma adecuada las versiones del proyecto.
El repositorio se encuentra la siguiente dirección: https://github.com/sadaakisz/Quoridor_Overthimker

Commits:
A continuación, se muestra el diagrama de clases referente al proyecto:





Algunas clases (human, player) aún no se encuentran definidas, pero las mantenemos en el diagrama porque han sido ideas en las que trabajaremos más adelante. Sin 
embargo, este diagrama está sujeto a cambios. El diagrama es una gran ayuda visual para orientarnos respecto a las clases que estamos manejando actualmente.
En cuanto a la resolución de problemas, una estrategia que tomamos fue la de programar una representación gráfica (a pesar de no ser un requerimiento fijo para esta 
entrega) debido a que esto facilita considerablemente la corrección de errores al momento de revisar el código. Por ejemplo, debajo se muestra parte de la 
visualización del tablero que revisamos para probar nuestra implementación de backtracking. De esta forma validamos que el movimiento del bot que controlará a uno de 
los peones funciona.

















Otra táctica con la que trabajamos al enfrentarnos a problemas fue la de cada uno programar soluciones diferentes, para ver cual funcionaba mejor y comparar nuestro 
razonamiento. Sin embargo, muchas veces también es útil que trabajemos juntos en un mismo bloque de código, notando detalles que a otro compañero le pueden haber 
pasado por alto, o consultando dudas sobre sintaxis, etc.




Experimentos
El trabajo ha pasado por varias fases por las cuales se ha experimentado tanto los algoritmos, como las validaciones del movimiento del peón siendo limitada por la 
existencia de las paredes en el tablero.




Referencia Bibliográfica:
Chang, H. S., Fu, M. C., Hu, J., & Marcus, S. I. (2016). Google Deep Mind's AlphaGo. OR/MS Today, 43(5), 24-29. Recuperado de: https://www.informs.org/ORMS-Today/Public-Articles/October-Volume-43-Number-5/Google-DeepMind-s-AlphaGo
Tsur, G., & Segev, Y. Quoridor agent. Recuperado de: http://www.cs.huji.ac.il/~ai/projects/2012/Quoridor/files/report.pdf 

Glendenning, L. (2005). Mastering quoridor. Bachelor Thesis, Department of Computer Science, The University of New Mexico. Recuperado de: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.100.5204&rep=rep1&type=pdf 
