from distutils.core import setup
import setuptools

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'Manrod',
  version = '1.1',
  description="Manrod es una librería de código abierto que le permite generar palabras, frases, ordenar listas, entre otras funciones, de forma aleatoria",
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Enzo Vallejos',
  author_email = 'shotkill791@gmail.com',
  license='GNU General Public License v3.0',
  url = 'https://github.com/EnzoVallejos/Manrod',
  keywords = ['python', 'random', 'string', 'letters'],
  classifiers = ['Programming Language :: Python :: 3.7'],
)
