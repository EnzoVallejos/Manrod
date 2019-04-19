#!/usr/bin/python3

#Manrod v1.1
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
__version__ = "1.1"

from random import randint

_dict = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
		['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
		["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]

"""Libreria de generacion de string, etc; de forma aleatoria"""	
def random_lttr(lttr_case):
	"""#Generacion de una letra aleatoria"""
	if lttr_case == 'lowercase':
		lttr_random = _dict[0][randint(0, len(_dict[0]) - 1)]

	elif lttr_case == 'uppercase':
		lttr_random = _dict[1][randint(0, len(_dict[1]) - 1)]

	elif lttr_case == "any":
		listN = randint(0,1)
		lttr_random = _dict[listN][randint(0, len(_dict[listN]) - 1)]

	else:
		raise TypeError('Ingrese un tipo de letra correcta("lowercase", "uppercase" or "any"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("lttr_case")')

	return lttr_random

def str_letters(lttr_case, **range_of_letters):
	"""#Generacion de cadenas de texto aleatorias"""
	str_letter = ""
	try:
		if range_of_letters == {}:
			i = randint(2, 10)
		else:
			i = int(range_of_letters['range_of_letters'])

	except ValueError:
		raise ValueError('Ingrese un numero como rango no un texto. \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("Range")')

	if lttr_case == 'lowercase':
		for makeStr in range(0,i):
			str_letter += _dict[0][randint(0, len(_dict[0]) - 1)]

	#concadenacion con numeros significa "&number"
	elif lttr_case == 'lowercase&number':
		for makeStr in range(0,i):
			#hago que elija aleatoriamente que elemento agregar si letra o numero
			list_index = (0, 2)
			random_list = list_index[randint(0,1)]

			str_letter += _dict[random_list][randint(0, len(_dict[random_list]) - 1)]
				
	elif lttr_case == 'uppercase':
		for makeStr in range(0,i):
			str_letter += _dict[1][randint(0, len(_dict[1]) - 1)]

	elif lttr_case == 'uppercase&number':
		for makeStr in range(0,i):
			#hago que elija aleatoriamente que elemento agregar si letra o numero
			list_index = (1, 2)
			random_list = list_index[randint(0,1)]

			str_letter += _dict[random_list][randint(0, len(_dict[random_list]) - 1)]

	elif lttr_case == 'any':
		for makeStr in range(0,i):
			listN = randint(0,1)
			str_letter += _dict[listN][randint(0, len(_dict[listN]) - 1)]

	elif lttr_case == 'any&number':
		for makeStr in range(0,i):
			list_index = (0, 1, 2)
			random_list = list_index[randint(0,2)]

			str_letter += _dict[random_list][randint(0, len(_dict[random_list]) - 1)]

	else:
		raise TypeError('Ingrese un tipo de letra correcta("lowercase", "uppercase" y "any". O sus concadenaciones con "&number"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("lttr_case")')

	return str_letter

def rSortingList(lista):
	"""#reordenamiento de una lista aleatoriamente"""
	if  str(lista).isdigit():
		raise TypeError ('Ingrese un texto o una lista para su reordenamiento, no un numero. \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("rSortingList")')
			
	final_list = []
	long_list = len(lista)
	for i in lista:
			indexRand = randint(0, long_list - 1)
			final_list.insert(indexRand , i)

	return final_list

def rTake(range_valor, **kargs):
	"""#obtencion de un valor de una lista o un texto"""
	range_init = randint(0, len(range_valor) - 1)
	if kargs == {}:
		menF = range_valor[range_init]
		return menF

	#por si el argumento pasado es 'data_out_format' o 'final_range'
	elif len(kargs) == 1:
		args = [i for i in kargs if i in ['data_out_format', 'final_range']] 

		if args == []:
			raise TypeError('Ingrese un parametro correcto("data_out_format" o "final_range"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')
			
		#si el argumento ingresado es 'data_out_format' y el parametro es 'text' o 'list'
		if args[0] == 'data_out_format' and kargs['data_out_format'] in ['text', 'list']:
			if kargs['data_out_format'] == 'text':
				range_valor = str(range_valor)
				menF = range_valor[range_init]
			else:
				if kargs['data_out_format'] == 'list':
					range_valor = str(range_valor)
					menlist = [k for k in range_valor]
					menF = menlist[range_init: range_init + 1]
			return menF			

		else:
			if args[0] == 'final_range':
				final_range = kargs['final_range']

				#filtro de comprobacion de errores par saber si el rangoF es valido
				if str(final_range).isdigit() is not False:
					if final_range > len(range_valor):
						raise ValueError('El rango final ingresado es mas grande que la longitud de la cadena')
				else:
					raise ValueError('El rango final ingresado debe ser un numero no un texto.')

				if range_init > final_range:
					range_init_new = range_init
					while range_init_new > final_range:
							range_init_new = randint(0, len(range_valor) - 1)
				else:
					range_init_new = range_init

				menF = range_valor[range_init_new:final_range]
				return menF

			else:
				raise ValueError('Ingrese un valor correcto para los parametros ("data_out_format" o "final_range"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')

	#si hay 2 argumentos ingresados
	elif len(kargs) == 2:
		args = [i for i in kargs if i in ['final_range', 'data_out_format']]
			
		if  len(args) < 2:
			raise TypeError('Ingrese parametros correctos ("data_out_format" o "final_range"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')
		else:
			if args[1] == 'final_range':
				raise NameError('A ingresado los parametros de forma incorrecta. \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')

		if args[1] == 'data_out_format' and kargs['data_out_format'] in ['text', 'list']:
			final_range = kargs['final_range']
			data_out_format = kargs['data_out_format']
		else:
			raise ValueError('Ingrese un valor correcto para el parametro "data_out_format". \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TakeParams")')

		if str(final_range).isdigit() is not False:
			if final_range > len(range_valor):
				raise ValueError('El rango final ingresado es mas grande que la longitud de la cadena')
		else:
			raise ValueError('El rango final ingresado debe ser un numero no un texto.')

		#filtros de comprobaciones
		if range_init > final_range:
			range_init_new = range_init
			while range_init_new > final_range:
				range_init_new = randint(0, len(range_valor) - 1)
		else:
			range_init_new = range_init

		menParcial = range_valor[range_init_new:final_range]

		if kargs['data_out_format'] == 'text':
			menF = menParcial
		else:
			if kargs['data_out_format'] == 'list':
				range_valor = str(range_valor)
				menlist = [k for k in menParcial]
				menF = menlist
			
		return menF

def array_random(lttr_case, row, column):
	try:
		import numpy as np
	except:
		raise ImportError("para usar esta opcion debe tener instalado numpy")


	if lttr_case in ["lowercase", "lowercase&number", "uppercase", "uppercase&number", "any", "any&number"]:
		column_generated = []
		array_final = []

		if lttr_case == "lowercase":
			for columna in range(column):
				for fila in range(row):
					column_generated.append(_dict[0][randint(0,len(_dict[0]) - 1)])

				array_final.append(column_generated)
				column_generated = []

		elif lttr_case == "uppercase":
			for columna in range(column):
				for fila in range(row):
					column_generated.append(_dict[1][randint(0,len(_dict[1]) - 1)])

				array_final.append(column_generated)
				column_generated = []

		elif lttr_case == "any":
			for columna in range(column):
				for fila in range(row):
					column_generated.append(_dict[randint(0,1)][randint(0,len(_dict[randint(0,1)]) - 1)])

				array_final.append(column_generated)
				column_generated = []

		elif lttr_case == "lowercase&number":
			for columna in range(column):
				list_index = (0,2)
				list_index_choice = list_index[randint(0,1)]
				
				for fila in range(row):
					column_generated.append(_dict[list_index_choice][randint(0,len(_dict[list_index_choice]) - 1)])

				array_final.append(column_generated)
				column_generated = []

		elif lttr_case == "uppercase&number":
			for columna in range(column):
				list_index = (1,2)
				list_index_choice = list_index[randint(0,1)]
				
				for fila in range(row):
					column_generated.append(_dict[list_index_choice][randint(0,len(_dict[list_index_choice]) - 1)])

				array_final.append(column_generated)
				column_generated = []

		elif lttr_case == "any&number":
			for columna in range(column):
				list_index = [0,1,2]
				list_index_choice = list_index[randint(0,2)]
				
				for fila in range(row):
					column_generated.append(_dict[list_index_choice][randint(0,len(_dict[list_index_choice]) - 1)])

				array_final.append(column_generated)
				column_generated = []

		return np.array(array_final)

	else:
		raise ValueError('Ingrese un tipo de letra correcta("lowercase", "uppercase" y "any". O sus concadenaciones con "&number"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("lttr_case")')

def help(consulta):
	"""#funcion para que el usuario pueda obtener informacion"""
	if consulta in ['?','random_lttr','str_letters','rSortingList','rTake','lttr_case','final_range', 'range_of_letters','data_out_format']:
		if consulta == '?':
			print('\n--help$all-- Las consultas que puede realizar aqui son: \n\nFunciones de la libreria:\n1."random_lttr"\n2."str_letters"\n3."rSortingList"\n4."rTake"\n\nParametros que requieren las funciones: \n5."lttr_case"\n6."final_range"\n7."data_out_format"\n8."range_of_letters"')

		#funciones de la libreria
		if consulta == 'random_lttr':
			print('\n--help$random_lttr-- La funcion "random_lttr" devuelve una letra elegida aleatoriamente. A dicha funcion se le debe pasar el parametro "lttr_case"(para mas informacion leer la documentacion o colocar "mr.help("lttr_case")").\n\nEjemplo en la consola de python:\n>>>from Manrod import mr\n>>>mr.random_lttr("lowercase")\na\n\nY con este formato pueden realizar con los otros valores que pide la funcion.')

		if consulta == 'str_letters':
			print('\n--help$str_letters-- La funcion "str_letters" a diferencia que "random_lttr" devuelve una cadena de letras aleatoria. A esta funcion se le pasa el parametro "lttr_case"(para mas informacion leer la documentacion o colocar "mr.help("lttr_case")") y opcionalmente el un rango de longitud que tendra la cadena, mas informacion ingrese "mr.help("range_of_letters")". Ejemplo en la consola de python:\n\nCon "lowercase":\n>>>from Manrod import mr\n>>>mr.str_letters("lowercase", range_of_letters=4)\nahgd\n\nCon "any":\n>>>mr.str_letters("any", range_of_letters=6)\nkJdSwO\n\nConcadenacion con numeros con "&number":\n>>>mr.str_letters("any&number", range_of_letters=6)\nfE3q5P\n\nEl range_of_letters puede colocarse o no. Mas informacion leer la documentacion o colocar "mr.help("range_of_letters")"')

		if consulta == 'rSortingList':
			print('\n--help$rSortingList-- La funcion "rSortingList" reordena de forma aleatoria una lista que se le sea suministrada o se le puede pasar un texto y devolvera una lista reordenada de forma aleatoria de ese texto. No se le puede pasar un numero, de ser ese el caso lanzara un error.\n\nEjemplo en la consola de python:\n\n>>>from Manrod import mr\n>>> test = ["test1", "test2", "test3"]\n>>> print(mr.rSortingList(test))\n["test3", "test1", "test2"]\n\nComo veran devuelve una lista ordenada en un orden aleatorio diferente a la lista original. Para esta funcion no es necesario ingresar algun parametro.')

		if consulta == "rTake":
			print('\n--help$rTake-- La funcion "rTake" selecciona una letra o tambien un conjunto de letras de un texto o lista que le suministremos. Se le puede suministrar dos parametros a esta funcion "final_range" y "data_out_format". \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion "mr.help("final_range")" y "mr.help("data_out_format")".\n\nEjemplo en la consola de python:\n\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345"))\n1\n\nEjemplo con "final_range":\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345", final_range=3))\nest\n\nEjemplo con "data_out_format":\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345", data_out_format="list"))\n["e"]\n\nEjemplo con ambos parametros:\n>>>from Manrod import mr\n>>> print(mr.rTake("test12345", rangoF=4, data_out_format="list"))\n["t", "e", "s", "t"]\n\nEl "final_range" debe ser un numero entero y "data_out_format" se le debe pasar un valor valido, mas informacion de este parametro leer la documentacion o colocar "mr.help("data_out_format")"')

		#parametros de las funciones
		if consulta == 'lttr_case':
			print('\n--help$lttr_case-- El parametro "lttr_case" es requerido en las funciones "random_lttr" y "str_letters"; representa el tipo de letra que se utilizara para devolver el resultado final de la funcion.')
			print('\nLos valores que se le pasan a este parametro son "lowercase", "uppercase" y "any", ademas de las concadenacion con numeros que se pueden hacer al resultado final en la funcion "str_letters" agregando a dichos parametros el "&number". Ej: lttr_case="uppercase&number".')
			print('\n Al tipo de letra que hace referencia cada uno es:\n\n1."lowercase": Hace referencia a que el resultado retornado por la funcion va a ser en letras minusculas\n2."uppercase": Al igual que "lowercase", este devolvera el resultado en mayusculas.\n3."any": Este valor hace referencia a que el resultado sera cualquiera de los dos tipos de letras anteriores, el tipo de letra a usar sera elegido aleatoriamente.')

		if consulta == 'final_range':
			print('\n--help$final_range-- El parametro "final_range" es requerido en la funcion "rTake", este parametro hace referencia al rango final de donde tomara las letras la funcion "rTake" , es decir, le damos un numero que representara hasta donde la funcion tomara letras para retornar el valor final.\n El valor que le demos a este parametro debe ser un numero, en caso que ingresemos un rango que sea mayor a la longitud del texto o lista que le suministramos a la funcion, dara un error.')

		if consulta == "data_out_format":
			print('\n--help$data_out_format-- El parametro "data_out_format" es requerido en la funcion "rTake", este parametro hace referencia a como queremos que sea el valor retornado por la funcion. A este se le da dos valores "text" y "list".\n\n1."text": Si se coloca como valor de "data_out_format" el valor retornado por la funcion sera un texto, independientemente si el el valor que ingresamos originalmente a la funcion es una lista o un texto.\n2."list": A diferencia de "text" el valor retornado sera en formato de una lista, sin importar el valor ingresado al principio en la funcion. Por defecto la funcion "rTake" retorna el valor en formato de texto.')

		if consulta == "range_of_letters":
			print('\n--help$range_of_letters-- El parametro "range_of_letters" es requerido en la funcion  "str_letters" y  hace referencia a el largo de la cadena de texto retornado por la funcion. Este mismo debe ser un numero. Por defecto el range_of_letters es un numero aleatorio entre el 2 y el 10.')

	else:
		raise ValueError('Debe ingresar un valor correcto a para recibir informacion. Para ver toda la informacion coloque un "?"')
