

<h1>Complejidad Algorítmica</h1>


<h3>Trabajo Final</h3>

<h3>“Informe del Trabajo Final”</h3>

<h3>Docente:</h3>
Reyes Silva, Patricia Daniela

<h3>Integrantes:</h3>

<br>Nuñez Melgarejo, Mauricio Oscar
<br>Diaz Quilia, Marc Alexander
<br>Gómez Timoteo, Clinder
<br>Chumpitaz Paredes, Alessandro Paris


<h3>Índice</h3>


1.	Introducción
2.	Objetivos
3.	Área de la ciudad
o	Descripción de la ciudad elegida
o	Imagen estática de la ciudad o porción de ciudad elegida
4.	Descripción del conjunto de datos
o	Datos consignados por calle
o	Datos consignados por intersección
5.	Grafo de la Ciudad
(Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices).
6.	Diseño del Sistema de Tráfico
o	Cómo se incorpora tráfico por horas en calles o segmentos de calles
o	Cómo se calcula el peso de arista en base a su longitud y factor de tráfico
o	Cómo se actualiza el peso de la arista en función de la hora del día.
o	Algoritmos utilizados para calcular la ruta más corta y dos rutas alternativas
o	Implementación de visual del mapa y las rutas a partir del grafo y algoritmo seleccionado
o	Interfaz gráfica
o	Enlaces: a repositorio de GitHub / a video de presentación.
7.	Conclusiones 

<h2>Introducción</h2>




<br>Los aplicativos móviles son diseñados para la resolución de problemas que puede encontrar un usuario frecuentemente. En especial, son populares aquellas aplicaciones que logran determinar la mejor ruta a recorrer para un conductor que requiere llegar a cierta ubicación desde otro punto. Por ello, el uso de aplicaciones como Waze, una aplicación social de tránsito automotor en tiempo real y navegación asistida por GPS,  u otras del mismo estilo resultan ser una gran herramienta que facilita una respuesta óptima a este problema. 

<br>El problema de encontrar el mejor camino entre dos puntos de una ciudad es realmente complejo de resolver, pues la gran cantidad de calles genera una mayor cantidad de posibles rutas que resuelvan este dilema. Por lo tanto, los algoritmos diseñados para la resolución de este problema que son implementados en las distintas aplicaciones son buenos ejemplos para el entendimiento de la complejidad algorítmica.

<br>En este proyecto se presenta un programa especialmente diseñado para la resolución del tema abordado: un sistema que nos permita encontrar la ruta más corta entre 2 puntos en una ciudad. Para ello, el programa tiene implementado el algoritmo a-estrella (A*) y hace uso de los datos de las calles de Lima para poner a prueba esta aplicación. 












<h2>Objetivos</h2>


Como objetivo de este proyecto, se busca desarrollar un programa en Python que logre determinar la ruta más óptima para llegar desde una determinada locación a otra. Para ello, se usarán datos de las calles de Lima con la ubicación geográfica de cada intersección. Además, para la búsqueda de la mejor ruta se hará uso del algoritmo A* (A - star) en la que los nodos representan los cruces entre calles y las aristas representan la distancia entre dos intersecciones.





<h2>Área de la ciudad</h2>
<br>●	Descripción de la ciudad elegida
Elegimos la ciudad de Lima, la capital del Perú, debido a que es la ciudad más urbanizada del Perú. Su alto nivel de tránsito y su compleja distribución de calles nos representa un gran desafío a superar y poner a prueba el programa desarrollado.
<br>●	Imagen estática de la ciudad o porción de ciudad elegida

![img]( https://prnt.sc/v3PKxgONllqM)









<h2>Descripción del conjunto de datos</h2>

Contamos con dos archivos de los datos que usaremos en formato de valores separados por comas

●	Datos consignados por calle

1.	Cada calle tiene un punto origen (inicio), punto destino (final) y un valor de distancia de dicha calle. 
2.	El punto de inicio representa el primer punto x1 (latitud), y1 (longitud) marcado en el mapa y el punto final representa donde termina la calle x2, y2. 
3.	Con respecto a la distancia, esta es la diferencia en kilómetros con respecto al punto de inicio y el punto final. 

Del archivo Lima-calles.csv

1.	Id de la calle
2.	Nombre de la calle
3.	Cantidad de intersecciones












●	Datos consignados por intersección

1.	Un punto de intersección se puede representar por medio de un punto X, Y, porque X representa la latitud y la longitud. 
2.	Además, una calle se puede representar por medio de una recta, entonces, en base a esa lógica, podemos afirmar que tendremos una intersección de calles o una esquina cuando dos o más rectas se encuentren.  

Del archivo Lima-intersecciones.csv

1.	Ítem (correlativo)
2.	Id de la calle
3.	Nombre de la calle
4.	Id calle origen (con la que intercepta)
5.	Id calle final (con la que intercepta)
6.	Id origen de la intersección
7.	Id destino de la intersección
8.	Distancia en Km entre Id origen de la intersección / Id destino de la intersección
9.	La velocidad en Km/h entre Id origen de la intersección / Id destino de la intersección (es la velocidad permitida en ese tramo)
10.	Costo1 (deben calcular algún tipo de costo o ponderación de transitar en 8) 
11.	Costo2 (deben calcular algún tipo de costo o ponderación según la latitud/longitud)
12.	Latitud de 6
13.	Longitud de 6
14.	Latitud de 7
15.	Longitud de 7







<h2>Grafo de la Ciudad</h2>

<br>Para la creación del mapa se tomó como base conceptual la teoría de grafos.
<br>Esta consiste en un conjunto de nodos que se relacionan unas con otras mediante aristas.
<br>Así mismo, cada intersección dada como parte de nuestros datos para la elaboración del mapa está representado como un nodo o vértice en un grafo y cada calle, o sección de esta, como una arista.
<br>El costo de una arista que une dos nodos indica la distancia obtenida entre dos intersecciones a partir de las coordenadas proporcionadas en los datos.
<br>Además, cada nodo puede estar enlazada a muchos otros por lo que es crucial disponer de una matriz de adyacencia en la cual se ubiquen los nodos directamente enlazados para cada nodo.
<br>Esta matriz representa a cada intersección seguida de una lista de todas aquellas a las cuales, según los datos disponibles, sea posible llegar recorriendo una sola calle sin pasar por ningún otro cruce.











