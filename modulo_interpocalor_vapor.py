#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thmenendez
#
# Created:     03/06/2017
# Copyright:   (c) thmenendez 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador):

    proplista= []

    extrapola = 0

    nfilas = len(tabla)
    ncol = len(tabla[0])

    for i in range(nfilas):
        proplista.append(tabla[i][indicador])

    # Calcula el factor de interpolacion
    i = 0
    while(propiedad_conocida>=proplista[i]) and (i+1<nfilas):
        i = i + 1
    Fx = (propiedad_conocida-proplista[i-1])/(proplista[i]-proplista[i-1])
    if propiedad_conocida>proplista[i] or i==0: # Sobrepaso o me quedo corto y extrapolo
        extrapola = 1
    #del templista
    #del propiedad_conocida

    # Interpola para todas las variables
    sol = []
    for j in range(ncol):
        dato = tabla[i-1][j]+Fx*(tabla[i][j]-tabla[i-1][j])
        sol.append(dato)
    sol.append(extrapola)
    return sol
