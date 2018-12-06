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
			raise TypeError('Ingrese un tipo de letra correcta("lowercase", "uppercase" or "any"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TypeLetter")')

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
			raise TypeError('Ingrese un tipo de letra correcta("lowercase", "uppercase" y "any". O sus concadenaciones con "&number"). \nPara mas informacion revise la documentacion o puede ver mas informacion con la funcion mr.help("TypeLetter")')

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
	#seguir trabajando en los demas, por si el usuario ingresa demas parametros
	def rTake(rValor, **kargs):
		#rangeIni, dOutput, rangeF
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

					#por si rangeIni es mayor que el rangeF
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
			
