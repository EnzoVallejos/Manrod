# Manrod

## Informacion: 
**Autor: Enzo Vallejos** 

**Lenguaje utilizado: Python**

**Version: 1.0.5(Es representada con 1.05 para abreviar)**

**Licencia: "GNU General Public License v3.0"**

**Descripcion de la libreria: Manrod es una librería de código abierto escrito en python que permite generar palabras, frases, ordenar listas, entre otras funciones, de forma aleatoria.**

## --Documentacion de la libreria "Manrod v1.03":--

### Importacion de la libreria
Para importar la libreria es muy facil, primera hay que tener intalado la libreria desde el pip de python. Se instala de la siguiente manera:

1. Tener instalado pip.
2. ingresar al cmd de windows y ingresar el siguiente comando
```
pip install Manrod
```
y listo tendremos instalado Manrod

Una vez esto ya este hecho para importar la libreria a nuestro codigo para utilizarlo se hace de la siguiente manera:
```
from Manrod import *
```
Debe ser de esta manera sino no importara el core de la libreria

### Indice:

#### Funciones de la libreria:
- random_lttr
- str_letters
- rSortingList
- rTake

#### Parametros que requieren las funciones:
- lttr_case
- final_range
- data_out_format
- range_of_letters

##### Funciones de la libreria:

- **"random_lttr":** La funcion "random_lttr" devuelve una letra elegida aleatoriamente. 
A dicha funcion se le debe pasar el parametro "lttr_case"(para mas informacion seguir leyendo la documentacion(**Doc\README.md**) o colocar **"help("lttr_case")"**.

Ejemplo en la consola de python:
```
>>>from Manrod import *
>>>random_lttr("lowercase")
a
```
Y con este formato pueden realizar con los otros valores que pide la funcion.

- **"str_letters":** La funcion "str_letters" a diferencia que "random_lttr" devuelve una cadena de letras aleatoria. A esta funcion se le pasa el parametro "lttr_case"(para mas informacion seguir leyendo la documentacion(**Doc\README.md**) o colocar **"help("lttr_case")"**, y opcionalmente le podemos pasar el parametro "range_of_letters" que con el definimos el largo que debera tener la cadena retornada(mas informacion seguir leyendo o colocar **"help("range_of_letters")"**). 

Ejemplo en la consola de python:

Con "lowercase":
```
>>>from Manrod import *
>>>str_letters("lowercase", range_of_letters=4)
ahgd
```

Con "any":
```
>>>str_letters("any", range_of_letters=6)
kJdSwO
```

Concadenacion con numeros con "&number":
```
>>>str_letters("any&number", range_of_letters=6)
fE3q5P
```

El range_of_letters puede colocarse o no. Mas informacion leer la documentacion o colocar "help("range_of_letters")".

- **"rSortingList":** La funcion "rSortingList" reordena de forma aleatoria una lista que se le sea suministrada o se le puede pasar un texto y devolvera una lista reordenada de forma aleatoria de ese texto. No se le puede pasar un numero, de ser ese el caso lanzara un error.

Ejemplo en la consola de python:
```
>>>from Manrod import *
>>> test = ["test1", "test2", "test3"]
>>> print(rSortingList(test))
["test3", "test1", "test2"]
```

Como veran devuelve una lista ordenada en un orden aleatorio diferente a la lista original. Para esta funcion no es necesario ingresar algun parametro.

- **"rTake":** La funcion "rTake" selecciona una letra o tambien un conjunto de letras de un texto o lista que le suministremos. Se le puede suministrar dos parametros a esta funcion "final_range" y "data_out_format".
Para mas informacion revise la documentacion en la parte de parametros o puede ver mas informacion con la funcion **"help("final_range")"** y **"help("data_out_format")"**.

Ejemplo en la consola de python:
```
>>>from Manrod import *
>>> print(rTake("test12345"))
1
```

Ejemplo con "final_range":
```
>>>from Manrod import *
>>> print(rTake("test12345", final_range=3))
est
```

Ejemplo con "data_out_format":
```
>>>from Manrod import *
>>> print(rTake("test12345", data_out_format="list"))
["e"]
```

Ejemplo con ambos parametros:
```
>>>from Manrod import *
>>> print(rTake("test12345", final_range=4, data_out_format="list"))
["t", "e", "s", "t"]
```

El "final_range" debe ser un numero entero y "data_out_format" se le debe pasar un valor valido, mas informacion de este parametro leer la documentacion o colocar **"help("data_out_format")"**.

#### Parametros que requieren las funciones:

- **"lttr_case":** El parametro "lttr_case" es requerido en las funciones "random_lttr" y "str_letters"; representa el tipo de letra que se utilizara para devolver el resultado final de la funcion. Los valores que se le pasan a este parametro son "lowercase", "uppercase" y "any", ademas de las concadenacion con numeros que se pueden hacer al resultado final en la funcion "str_letters" agregando a dichos parametros el "&number". Ej: lttr_case="uppercase&number. 

Al tipo de letra que hace referencia cada uno es:
**1. "lowercase":** Hace referencia a que el resultado retornado por la funcion va a ser en letras minusculas
**2. "uppercase":** Al igual que "lowercase", este devolvera el resultado en mayusculas.
**3. "any":** Este valor hace referencia a que el resultado sera cualquiera de los dos tipos de letras anteriores, el tipo de letra a usar sera elegido aleatoriamente.

- **"final_range":** El parametro "final_range" es requerido en la funcion "rTake", este parametro hace referencia al rango final de donde tomara las letras la funcion "rTake" , es decir, le damos un numero que representara hasta donde la funcion tomara letras para retornar el valor final. 
El valor que le demos a este parametro debe ser un numero, en caso que ingresemos un rango que sea mayor a la longitud del texto o lista que le suministramos a la funcion, dara un error.

- **"data_out_format":** El parametro "data_out_format" es requerido en la funcion "rTake", este parametro hace referencia a como queremos que sea el valor retornado por la funcion. 

A este se le da dos valores "text" y "list".
**1. "text":** Si se coloca como valor de "data_out_format" el valor retornado por la funcion sera un texto, independientemente si el el valor que ingresamos originalmente a la funcion es una lista o un texto.
**2. "list":** A diferencia de "text" el valor retornado sera en formato de una lista, sin importar el valor ingresado al principio en la funcion. Por defecto la funcion "rTake" retorna el valor en formato de texto.

- **"range_of_letters":** El parametro "range_of_letters" es requerido en la funcion  "str_letters" y  hace referencia a el largo de la cadena de texto retornado por la funcion. Este mismo debe ser un numero. 
Por defecto el range_of_letters es un numero aleatorio entre el 2 y el 10.
