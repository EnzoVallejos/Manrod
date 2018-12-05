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
	"""Core v1.01 de la libreria Manrod"""
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