Manrod v1.1
Copyright (C) 2018 Enzo Vallejos

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Razon por la que cree esta libreria

Desarrolle esta libreria por que queria darle una solucion rapida y facil a los desarrolladores para hace operaciones o iteraciones con letras o una cadena de letras, entre otras funciones que tiene la libreria, generadas aleatoriamente.

# ¿Por que usar Manrod?

Por que es facil de obtener un resultado que tenga que ver con una letras o una cadena de letras generadas de forma aleatoria, con esta libreria. basicamente es importar la libreria, llamar a la funcion que desea ejecutar y pasarle un parametro o mas si desea un resultado mas concreto(esto esta descrito en la documentacion **README.md**) y listo.

Un ejemplo de lo facil que es obtener un resultado con esta libreria es el siguiente:
```
print(strOfLetters(lttr_case="any"))
```
Esto nos devolvera el siguiente resultado, el para metro que le pase a la funcion llamado "lttr_case" hace referencia al tipo de letra que devolvera, pueden ver mas de esto en la documentacion.
```
aUIldH
```
Para ser mas especificos podemos pasarle otro parametro a esta funcion que es "range_of_letters" que dice que tan larga sera la cadena que retornara la funcion, es de la siguiente manera:
```
print(strOfLetters(lttr_case="any", range_of_letters=6))
```
El resultado de esto seria una cadena de 6 letras
```
DqPkNd
```

Asi de facil es obtener una cadena de letras totalmente aleatoria hasta podemos a hacer concadenaciones con numeros agregando a el valor que pasemos en "lttr_case" un "&number". Todo esto esta es la documentacion.

# ¿Por que se llama Manrod?

Manrod es la palabra "Random" pero en ordenada en forma aleatoria. Esto es asi por que esta generado por unas de las funciones que proporcionara la libreria que reordena las palabras de un texto o lista que le suministremos.
