#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""

Autor: Anderson Amaya Pulido

Libreria personal para encriptar.











"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#                                   importar complementos
#---------------------------------------------------------------------------------------

import hashlib

#---------------------------------------------------------------------------------------
#                                   Funciones para el emcriptado de datos
#---------------------------------------------------------------------------------------
#--- MD5

def MD5(Pal):

	return hashlib.md5(Pal).hexdigest()
