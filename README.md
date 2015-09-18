# Aplicación para realizar operaciones con matrices.
## Tecnología: 
	Python 2.7.

## Descripción: 
Con esta aplicación se pueden realizar sumas, restas, multiplicaciones y divisiones de matrices, estas operaciones además de la potencia también se pueden realizar con escalares. Acepta fracciones las cuales siempre las simplifica a su mínima expresión. La matriz además puede determinar su transpuesta, determinante e inversa, aprovechando esta última (la inversa) tiene un complemento para poder resolver ecuaciones.

## Comandos:

### Matriz
#### Importar la clase matriz del archivo matriz
	>>> from matriz import matriz
#### Crear una matriz
	>>> matriz(valores_de_la_matriz)
	
*valores\_de\_la\_matriz tiene que ser un dato list o tuple*

**Ejemplo:**
Crear la matriz 

2 &nbsp;&nbsp;&nbsp;&nbsp; 4

3 &nbsp;&nbsp;&nbsp;&nbsp; 5

	>>> valores = [[2,4],[3,5]]
	>>> matriz\_1 = matriz(valores)

#### Visualizar la matriz con formato
	>>> print matriz


### Fracción
#### Importar la clase frac del archivo Fraccion
	>>> from Fraccion import frac
#### Crear una fracción
	>>> frac(numerador,denominador)
#### Visualizar la fracción con formato
	>>> print fraccion
#### Operaciones
Las operaciones que puede realizar son la suma(+), resta(-), multiplicación(\*), división(/) y potencia(\*\*).
Los tipos de datos compatibles son int, float, long e instancias de la clase matriz y del mismo frac.

**Ejemplo:**
Suma de la fracción 1/2 más el numero entero 2
	<pre><code>>>> print fraccion\_1 + 2<br/>5/2</code></pre>
	
Guardar el resultado de la operación anterior en la variable fraccion\_2
	<pre><code>>>> fraccion\_2 = fraccion\_1 + 2<br/>>>> print fraccion\_2<br/>5/2</code></pre>
