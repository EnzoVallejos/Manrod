from distutils.core import setup

with open('README.md') as file:
  long_description = file.read()

setup(
  name = 'Manrod',
  packages = ['Manrod'],
  version = '1.01-stable',
  long_description=long_description,
  description = 'Manrod es una librería de código abierto que le permite generar palabras, frases, ordenar listas, entre otras funciones, de forma aleatoria.',
  author = 'Enzo Vallejos',
  author_email = 'shotkill791@gmail.com',
  license='GNU General Public License v3.0',
  url = 'https://github.com/EnzoVallejos/Manrod',
  download_url = 'https://github.com/EnzoVallejos/Manrod/tarball/v1.01-stable',
  keywords = ['python', 'random', 'string', 'letters'],
  classifiers = ['Programming Language :: Python :: 3.7'],
)