# Manrod version 1.1

## Cambios version 1.1:
- Renombramiento de variables y funciones: se renombro una gran parte de las variables e funciones para mejor legibilidad.
- Cambio de la forma de importar la libreria: antes de esta version la forma de importar la libreria era de esta forma
```
from Manrod.Manrod import mr
```
Esto se debia a que el core de la libreria era tratado como un objeto, al volver a leer el codigo note que no daba ninguna utilidad esto asi que cambie la estructura de la  misma, convirtiendola en funciones separadas e independientes que pueden ser importadas de forma individual o todas de una ves.
Para importar apartir de esta version es de la siguiente forma
```
from Manrod import *
```
