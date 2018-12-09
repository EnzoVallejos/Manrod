#!/usr/bin/python3

#Manrod v1.01
#Copyright (C) 2018 Enzo Vallejos

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Enzo Vallejos. User Github: EnzoVallejos y Gitlab: Enzo Vallejos"
__copyright__ = "Copyright 2018, Enzo Vallejos"

__license__ = "GNU General Public License v3.0"
__version__ = "1.01"

from random import randint

_dict = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
		['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
		["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]

class mr:
	"""Core v1.01 llamado mr de la libreria Manrod"""
	def __init__(self):
		super().__init__()

	#Generacion de una letra aleatoria
	def randomLetter(typeL):
		if typeL == 'lowercase':
			lttrRandom = _dict[0][randint(0, len(_dict[0]) - 1)]

		elif typeL == 'uppercase':
			lttrRandom = _dict[1][randint(0, len(_dict[1]) - 1)]

		elif typeL == "any":
			listN = randint(0,1)
			lttrRandom = _dict[listN][randint(0, len(_dict[listN]) - 1)]

		else:
			raise TypeError('Ingrese un tipo de letra correcta("lowercase", "uppercase" or "any"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("typeL")')

		return lttrRandom

	#Generacion de cadenas de texto aleatorias
	def strOfLetters(typeL, **rangeL):
		#miro si hay ingresado un rango si no lo hay le asigno uno aleatorio
		strLetter = ""
		try:
			if rangeL == {}:
				i = randint(2, 10)
			else:
				i = int(rangeL['rangeL'])

		except ValueError:
			raise ValueError('Ingrese un numero como rango no un texto. \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("Range")')

		if typeL == 'lowercase':
			for makeStr in range(0,i):
				strLetter += _dict[0][randint(0, len(_dict[0]) - 1)]

		#concadenacion con numeros significa "&number"
		elif typeL == 'lowercase&number':
			for makeStr in range(0,i):
				#hago que elija aleatoriamente que elemento agregar si letra o numero
				listInd = (0, 2)
				randomList = listInd[randint(0,1)]

				strLetter += _dict[randomList][randint(0, len(_dict[randomList]) - 1)]
				
		elif typeL == 'uppercase':
			for makeStr in range(0,i):
				strLetter += _dict[1][randint(0, len(_dict[1]) - 1)]

		elif typeL == 'uppercase&number':
			for makeStr in range(0,i):
				#hago que elija aleatoriamente que elemento agregar si letra o numero
				listInd = (1, 2)
				randomList = listInd[randint(0,1)]

				strLetter += _dict[randomList][randint(0, len(_dict[randomList]) - 1)]

		elif typeL == 'any':
			for makeStr in range(0,i):
				listN = randint(0,1)
				strLetter += _dict[listN][randint(0, len(_dict[listN]) - 1)]

		elif typeL == 'any&number':
			for makeStr in range(0,i):
				#hago que elija aleatoriamente que elemento agregar si letra o numero
				listInd = (0, 1, 2)
				randomList = listInd[randint(0,2)]

				strLetter += _dict[randomList][randint(0, len(_dict[randomList]) - 1)]

		else:
			raise TypeError('Ingrese un tipo de letra correcta("lowercase", "uppercase" y "any". O sus concadenaciones con "&number"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("typeL")')

		return strLetter

	#reordenamiento de una lista aleatoriamente
	def rSortingList(lista):
			if  str(lista).isdigit():
				raise TypeError ('Ingrese un texto o una lista para su reordenamiento, no un numero. \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("rSortingList")')
			
			listFinal = []
			longList = len(lista)
			for i in lista:
				indexRand = randint(0, longList - 1)
				listFinal.insert(indexRand , i)

			return listFinal

	#obtencion de un valor de una lista o un texto
	def rTake(rValor, **kargs):
		rangeIni = randint(0, len(rValor) - 1)
		if kargs == {}:
			menF = rValor[rangeIni]
			return menF

		#por si el argumento pasado es 'dOutput' o 'rangeF'
		elif len(kargs) == 1:
			args = [i for i in kargs if i in ['dOutput', 'rangeF']] 

			if args == []:
				raise TypeError('Ingrese un parametro correcto("dOutput" o "rangeF"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')
			
			#si el argumento ingresado es 'dOutput' y el parametro es 'text' o 'list'
			if args[0] == 'dOutput' and kargs['dOutput'] in ['text', 'list']:
				if kargs['dOutput'] == 'text':
					rValor = str(rValor)
					menF = rValor[rangeIni]
				else:
					if kargs['dOutput'] == 'list':
						rValor = str(rValor)
						menlist = [k for k in rValor]
						menF = menlist[rangeIni: rangeIni + 1]
				return menF			

			else:
				if args[0] == 'rangeF':
					rangeF = kargs['rangeF']

					#filtro de comprobacion de errores par saber si el rangoF es valido
					if str(rangeF).isdigit() is not False:
						if rangeF > len(rValor):
							raise ValueError('El rango final ingresado es mas grande que la longitud de la cadena')
					else:
						raise ValueError('El rango final ingresado debe ser un numero no un texto.')

					if rangeIni > rangeF:
						rangeIniNew = rangeIni
						while rangeIniNew > rangeF:
							rangeIniNew = randint(0, len(rValor) - 1)
					else:
						rangeIniNew = rangeIni

					menF = rValor[rangeIniNew:rangeF]
					return menF

				else:
					raise ValueError('Ingrese un valor correcto para los parametros ("dOutput" o "rangeF"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')

		#si hay 2 argumentos ingresados
		elif len(kargs) == 2:
			args = [i for i in kargs if i in ['rangeF', 'dOutput']]
			
			if  len(args) < 2:
				raise TypeError('Ingrese parametros correctos ("dOutput" o "rangeF"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')
			else:
				if args[1] == 'rangeF':
					raise NameError('A ingresado los parametros de forma incorrecta. \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')

			if args[1] == 'dOutput' and kargs['dOutput'] in ['text', 'list']:
				rangeF = kargs['rangeF']
				dOutput = kargs['dOutput']
			else:
				raise ValueError('Ingrese un valor correcto para el parametro "dOutput". \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')

			if str(rangeF).isdigit() is not False:
				if rangeF > len(rValor):
					raise ValueError('El rango final ingresado es mas grande que la longitud de la cadena')
			else:
				raise ValueError('El rango final ingresado debe ser un numero no un texto.')

			#filtros de comprobaciones
			if rangeIni > rangeF:
				rangeIniNew = rangeIni
				while rangeIniNew > rangeF:
					rangeIniNew = randint(0, len(rValor) - 1)
			else:
				rangeIniNew = rangeIni

			menParcial = rValor[rangeIniNew:rangeF]

			if kargs['dOutput'] == 'text':
				menF = menParcial
			else:
				if kargs['dOutput'] == 'list':
					rValor = str(rValor)
					menlist = [k for k in menParcial]
					menF = menlist
			
			return menF

	def help(consulta):
		if consulta in ['?','randomLetter','strOfLetters','rSortingList','rTake','typeL','rangeF', 'rangeL','dOutput']:
			if consulta == '?':
				print('\n--help$all-- Las consultas que puede realizar aqui son: \n\nFunciones de la libreria:\n1."randomLetter"\n2."strOfLetters"\n3."rSortingList"\n4."rTake"\n\nParametros que requieren las funciones: \n5."typeL"\n6."rangoF"\n7."dOutput"\n8."rangeL"')

			#funciones de la libreria
			if consulta == 'randomLetter':
				print('\n--help$randomLetter-- La funcion "randomLetter" devuelve una letra elegida aleatoriamente. A dicha funcion se le debe pasar el parametro "typeL"(para mas informacion leer la documentacion o colocar "mr.help("typeL")").\n\nEjemplo en la consola de python:\n>>>from Manrod import mr\n>>>mr.randomLetter("lowercase")\na\n\nY con este formato pueden realizar con los otros valores que pide la funcion.')

			if consulta == 'strOfLetters':
				print('\n--help$strOfLetters-- La funcion "strOfLetters" a diferencia que "randomLetter" devuelve una cadena de letras aleatoria. A esta funcion se le pasa el parametro "typeL"(para mas informacion leer la documentacion o colocar "mr.help("typeL")") y opcionalmente el un rango de longitud que tendra la cadena, mas informacion ingrese "mr.help("rangeL")". Ejemplo en la consola de python:\n\nCon "lowercase":\n>>>from Manrod import mr\n>>>mr.strOfLetters("lowercase", rangeL=4)\nahgd\n\nCon "any":\n>>>mr.strOfLetters("any", rangeL=6)\nkJdSwO\n\nConcadenacion con numeros con "&number":\n>>>mr.strOfLetters("any&number", rangeL=6)\nfE3q5P\n\nEl rangeL puede colocarse o no. Mas informacion leer la documentacion o colocar "mr.help("rangeL")"')

			if consulta == 'rSortingList':
				print('\n--help$rSortingList-- La funcion "rSortingList" reordena de forma aleatoria una lista que se le sea suministrada o se le puede pasar un texto y devolvera una lista reordenada de forma aleatoria de ese texto. No se le puede pasar un numero, de ser ese el caso lanzara un error.\n\nEjemplo en la consola de python:\n\n>>>from Manrod import mr\n>>> test = ["test1", "test2", "test3"]\n>>> print(mr.rSortingList(test))\n["test3", "test1", "test2"]\n\nComo veran devuelve una lista ordenada en un orden aleatorio diferente a la lista original. Para esta funcion no es necesario ingresar algun parametro.')

			if consulta == "rTake":
				print('\n--help$rTake-- La funcion "rTake" selecciona una letra o tambien un conjunto de letras de un texto o lista que le suministremos. Se le puede suministrar dos parametros a esta funcion "rangeF" y "dOutput". \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion "mr.help("rangeF")" y "mr.help("dOutput")".\n\nEjemplo en la consola de python:\n\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345"))\n1\n\nEjemplo con "rangeF":\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345", rangeF=3))\nest\n\nEjemplo con "dOutput":\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345", dOutput="list"))\n["e"]\n\nEjemplo con ambos parametros:\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345", rangoF=4, dOutput="list"))\n["t", "e", "s", "t"]\n\nEl "rangeF" debe ser un numero entero y "dOutput" se le debe pasar un valor valido, mas informacion de este parametro leer la documentacion o colocar "mr.help("dOutput")"')

			#parametros de las funciones
			if consulta == 'typeL':
				print('\n--help$typeL-- El parametro "typeL" es requerido en las funciones "randomLetter" y "strOfLetters"; representa el tipo de letra que se utilizara para devolver el resultado final de la funcion.')
				print('\nLos valores que se le pasan a este parametro son "lowercase", "uppercase" y "any", ademas de las concadenacion con numeros que se pueden hacer al resultado final en la funcion "strOfLetters" agregando a dichos parametros el "&number". Ej: typeL="uppercase&number".')
				print('\n Al tipo de letra que hace referencia cada uno es:\n\n1."lowercase": Hace referencia a que el resultado retornado por la funcion va a ser en letras minusculas\n2."uppercase": Al igual que "lowercase", este devolvera el resultado en mayusculas.\n3."any": Este valor hace referencia a que el resultado sera cualquiera de los dos tipos de letras anteriores, el tipo de letra a usar sera elegido aleatoriamente.')

			if consulta == 'rangeF':
				print('\n--help$rangeF-- El parametro "rangeF" es requerido en la funcion "rTake", este parametro hace referencia al rango final de donde tomara las letras la funcion "rTake" , es decir, le damos un numero que representara hasta donde la funcion tomara letras para retornar el valor final.\n El valor que le demos a este parametro debe ser un numero, en caso que ingresemos un rango que sea mayor a la longitud del texto o lista que le suministramos a la funcion, dara un error.')

			if consulta == "dOutput":
				print('\n--help$dOutput-- El parametro "rangeF" es requerido en la funcion "rTake", este parametro hace referencia a como queremos que sea el valor retornado por la funcion. A este se le da dos valores "text" y "list".\n\n1."text": Si se coloca como valor de "dOutput" el valor retornado por la funcion sera un texto, independientemente si el el valor que ingresamos originalmente a la funcion es una lista o un texto.\n2."list": A diferencia de "text" el valor retornado sera en formato de una lista, sin importar el valor ingresado al principio en la funcion. Por defecto la funcion "rTake" retorna el valor en formato de texto.')

			if consulta == "rangeL":
				print('\n--help$rangeL-- El parametro "rangeL" es requerido en la funcion  "strOfLetters" y  hace referencia a el largo de la cadena de texto retornado por la funcion. Este mismo debe ser un numero. Por defecto el rangeL es un numero aleatorio entre el 2 y el 10.')

		else:
			raise ValueError('Debe ingresar un valor correcto a para recibir informacion. Para ver toda la informacion coloque un "?"')