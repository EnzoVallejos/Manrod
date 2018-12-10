# Manrod

## Informacion: 
**Autor: Enzo Vallejos** 

**Lenguaje utilizado: Python**

**Version: 1.01**

**Licencia: "GNU General Public License v3.0"**

**Descripcion de la libreria: Manrod es una librería de código abierto escrito en python que permite generar palabras, frases, ordenar listas, entre otras funciones, de forma aleatoria.**

## --Documentacion de la libreria "Manrod v1.01":--

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
#Terminar cuando este subido a PyPi
```

### Indice:

#### Funciones de la libreria:
- randomLetter
- strOfLetters
- rSortingList
- rTake

#### Parametros que requieren las funciones:
- typeL
- rangoF
- dOutput
- rangeL

##### Funciones de la libreria:

- **"randomLetter":** La funcion "randomLetter" devuelve una letra elegida aleatoriamente. 
A dicha funcion se le debe pasar el parametro "typeL"(para mas informacion seguir leyendo la documentacion(**Doc\README.md**) o colocar **"mr.help("typeL")"**.

Ejemplo en la consola de python:
```
>>>from Manrod import mr
>>>mr.randomLetter("lowercase")
a
```
Y con este formato pueden realizar con los otros valores que pide la funcion.

- **"strOfLetters":** La funcion "strOfLetters" a diferencia que "randomLetter" devuelve una cadena de letras aleatoria. A esta funcion se le pasa el parametro "typeL"(para mas informacion seguir leyendo la documentacion(**Doc\README.md**) o colocar **"mr.help("typeL")"**, y opcionalmente le podemos pasar el parametro "rangeL" que con el definimos el largo que debera tener la cadena retornada(mas informacion seguir leyendo o colocar **"mr.help("rangeL")"**). 

Ejemplo en la consola de python:

Con "lowercase":
```
>>>from Manrod import mr
>>>mr.strOfLetters("lowercase", rangeL=4)
ahgd
```

Con "any":
```
>>>mr.strOfLetters("any", rangeL=6)
kJdSwO
```

Concadenacion con numeros con "&number":
```
>>>mr.strOfLetters("any&number", rangeL=6)
fE3q5P
```

El rangeL puede colocarse o no. Mas informacion leer la documentacion o colocar "mr.help("rangeL")".

- **"rSortingList":** La funcion "rSortingList" reordena de forma aleatoria una lista que se le sea suministrada o se le puede pasar un texto y devolvera una lista reordenada de forma aleatoria de ese texto. No se le puede pasar un numero, de ser ese el caso lanzara un error.

Ejemplo en la consola de python:
```
>>>from Manrod import mr
>>> test = ["test1", "test2", "test3"]
>>> print(mr.rSortingList(test))
["test3", "test1", "test2"]
```

Como veran devuelve una lista ordenada en un orden aleatorio diferente a la lista original. Para esta funcion no es necesario ingresar algun parametro.

- **"rTake":** La funcion "rTake" selecciona una letra o tambien un conjunto de letras de un texto o lista que le suministremos. Se le puede suministrar dos parametros a esta funcion "rangeF" y "dOutput".
Para mas informacion revise la documentacion en la parte de parametros o puede ver mas informacion con la funcion **"mr.help("rangeF")"** y **"mr.help("dOutput")"**.

Ejemplo en la consola de python:
```
>>>from Manrod import mr
>>> print(mr.rTake("test12345"))
1
```

Ejemplo con "rangeF":
```
>>>from Manrod import mr
>>> print(mr.rTake("test12345", rangeF=3))
est
```

Ejemplo con "dOutput":
```
>>>from Manrod import mr
>>> print(mr.rTake("test12345", dOutput="list"))
["e"]
```

Ejemplo con ambos parametros:
```
>>>from Manrod import mr
>>> print(mr.rTake("test12345", rangoF=4, dOutput="list"))
["t", "e", "s", "t"]
```

El "rangeF" debe ser un numero entero y "dOutput" se le debe pasar un valor valido, mas informacion de este parametro leer la documentacion o colocar **"mr.help("dOutput")"**.

#### Parametros que requieren las funciones:

- **"typeL":** El parametro "typeL" es requerido en las funciones "randomLetter" y "strOfLetters"; representa el tipo de letra que se utilizara para devolver el resultado final de la funcion. Los valores que se le pasan a este parametro son "lowercase", "uppercase" y "any", ademas de las concadenacion con numeros que se pueden hacer al resultado final en la funcion "strOfLetters" agregando a dichos parametros el "&number". Ej: typeL="uppercase&number. 

Al tipo de letra que hace referencia cada uno es:
**1. "lowercase":** Hace referencia a que el resultado retornado por la funcion va a ser en letras minusculas
**2. "uppercase":** Al igual que "lowercase", este devolvera el resultado en mayusculas.
**3. "any":** Este valor hace referencia a que el resultado sera cualquiera de los dos tipos de letras anteriores, el tipo de letra a usar sera elegido aleatoriamente.

- **"rangoF":** El parametro "rangeF" es requerido en la funcion "rTake", este parametro hace referencia al rango final de donde tomara las letras la funcion "rTake" , es decir, le damos un numero que representara hasta donde la funcion tomara letras para retornar el valor final. 
El valor que le demos a este parametro debe ser un numero, en caso que ingresemos un rango que sea mayor a la longitud del texto o lista que le suministramos a la funcion, dara un error.

- **"dOutput":** El parametro "dOutput" es requerido en la funcion "rTake", este parametro hace referencia a como queremos que sea el valor retornado por la funcion. 

A este se le da dos valores "text" y "list".
**1. "text":** Si se coloca como valor de "dOutput" el valor retornado por la funcion sera un texto, independientemente si el el valor que ingresamos originalmente a la funcion es una lista o un texto.
**2. "list":** A diferencia de "text" el valor retornado sera en formato de una lista, sin importar el valor ingresado al principio en la funcion. Por defecto la funcion "rTake" retorna el valor en formato de texto.

- **"rangeL":** El parametro "rangeL" es requerido en la funcion  "strOfLetters" y  hace referencia a el largo de la cadena de texto retornado por la funcion. Este mismo debe ser un numero. 
Por defecto el rangeL es un numero aleatorio entre el 2 y el 10.
