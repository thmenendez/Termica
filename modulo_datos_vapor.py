    #-------------------------------------------------------------------------------
# Name:        modulo_datos_vapor
# Purpose:
#
# Author:      thmenendez
#
# Created:     16/06/2016
# Copyright:   (c) thmenendez 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def lee_datos_vapor_agua():
    """Recibe un indicador de temperatura (1) o presion (0) y devuelve la tabla completa en floats"""
    tabla = []
    f = open('R134a.txt','r')
    for linea in f:
        l = linea.strip()
        l = l.split(';')
        for i in range(len(l)):
            l[i]=float(l[i])
        tabla.append(l)
    f.close()
    #del f

    return tabla
