# Parcial I - Algoritmos y Programación 2425-1

> Universidad Metropolitana \
> Facultad de Ingeniería \
> Departamento de Gestión de Proyectos y Sistemas \
> Algoritmos y Programación (BPTSP05) \

## Ejercicio 1 (7 puntos)

Dado un array de strings `words`, devuelve las palabras que se pueden escribir utilizando las letras del alfabeto que están en una sola fila del teclado estadounidense, como se muestra en la imagen a continuación.

![Teclado](https://www.daskeyboard.com/blog/wp-content/uploads/qwerty-windows-1024x338.jpg)

En el teclado estadounidense:

- La primera fila consiste en los caracteres "qwertyuiop",
- La segunda fila consiste en los caracteres "asdfghjkl", y
- La tercera fila consiste en los caracteres "zxcvbnm".

**Ejemplos:**

- Ejemplo 1:

  - Entrada: `words = ["Hello", "Alaska", "Dad", "Peace"]`
  - Salida: `["Alaska", "Dad"]`

- Ejemplo 2:

  - Entrada: `words = ["omk"]`
  - Salida: `[]`

- Ejemplo 3:

  - Entrada: `words = ["adsdf", "sfd"]`
  - Salida: `["adsdf", "sfd"]`

- Restricciones:

  - 1 <= words.length <= 20
  - 1 <= words[i].length <= 100
  - words[i] consiste en letras del alfabeto inglés (tanto minúsculas como mayúsculas).

## Ejercicio 2 (7 puntos)

Se te da un arreglo de enteros indexado desde 0 llamado mountain. Tu tarea es encontrar todos los picos en el arreglo de la montaña.

Devuelve un arreglo que consista en los índices de los picos en el arreglo dado en cualquier orden.

**Notas:**

- Un pico se define como un elemento que es estrictamente mayor que sus elementos vecinos.
- Los primeros y últimos elementos del arreglo no pueden ser un pico.

**Ejemplos:**

- Ejemplo 1:

  - Entrada: `mountain = [2,4,4]`
  - Salida: `[]`
  - Explicación: mountain[0] y mountain[2] no pueden ser picos porque son el primer y último elemento del arreglo. mountain[1] tampoco puede ser un pico porque no es estrictamente mayor que mountain[2]. Por lo tanto, la respuesta es [].

- Ejemplo 2:

  - Entrada: `mountain = [1,4,3,8,5]`
  - Salida: `[1,3]`
  - Explicación: mountain[0] y mountain[4] no pueden ser picos porque son el primer y último elemento del arreglo. mountain[2] tampoco puede ser un pico porque no es estrictamente mayor que mountain[3] y mountain[1]. Pero mountain[1] y mountain[3] son estrictamente mayores que sus elementos vecinos. Por lo tanto, la respuesta es [1,3].

- Restricciones:
  - 3 <= mountain.length <= 100
  - 1 <= mountain[i] <= 100

## Ejercicio 3 (8 puntos)

Dada una string `path`, donde `path[i]` puede ser 'N', 'S', 'E' o 'W', cada una representando un movimiento de una unidad hacia el norte, sur, este u oeste, respectivamente. Comienzas en el origen (0, 0) en un plano 2D y sigues el camino especificado por path.

Haz una función que devuelva `True` si el camino se cruza en algún punto, es decir, si en algún momento estás en una ubicación que ya has visitado previamente. Devuelve `False` en caso contrario.

**Ejemplos**:

- Ejemplo 1:

  - Entrada: `path = "NES"`
  - Salida: `False`
  - Explicación: Observa que el camino no cruza ningún punto más de una vez.

- Ejemplo 2:

  - Entrada: `path = "NESWW"`
  - Salida: `True`
  - Explicación: Observa que el camino visita el origen dos veces.

- Restricciones:

  - 1 <= path.length <= 10^4
