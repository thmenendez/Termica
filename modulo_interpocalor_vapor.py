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

def interpocalor_vapor():

    propiedad_conocida = float(raw_input('Introduce la temperatura (en C): '))

    indicador = 0 # indicador pasara a ser el de la propiedad a interpolar

    import modulo_datos_vapor
    tabla = modulo_datos_vapor.lee_datos_vapor_agua()
    propiedades = calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador)

    if propiedades[13]==1:
        print 'EXTRAPOLACION'

     # Imprime el resultado
    for i in range(len(propiedades)):
        if i == 0:
            print 'Temperatura: %f C'%propiedades[i]
        elif i == 1:
            print 'Presion: %f kPa\n'%propiedades[i]
        elif i == 2:
            print 'Volumen especifico del liquido: %f m3/kg'%propiedades[i]
        elif i == 3:
            print 'Volumen especifico del vapor: %f m3/kg\n'%propiedades[i]
        elif i == 4:
            print 'Energia interna del liquido: %f kJ/kg'%propiedades[i]
        elif i == 5:
            print 'Energia interna de evaporacion: %f kJ/kg'%propiedades[i]
        elif i == 6:
            print 'Energia interna del vapor: %f kJ/kg\n'%propiedades[i]
        elif i == 7:
            print 'Entalpia del liquido: %f kJ/kg'%propiedades[i]
        elif i == 8:
            print 'Entalpia de evaporacion: %f kJ/kg'%propiedades[i]
        elif i == 9:
            print 'Entalpia del vapor: %f kJ/kg\n'%propiedades[i]
        elif i == 10:
            print 'Entropia del liquido: %f kJ/(kg*K)'%propiedades[i]
        elif i == 11:
            print 'Entropia de evaporacion: %f kJ/(kg*K)'%propiedades[i]
        elif i == 12:
            print 'Entropia del vapor: %f kJ/(kg*K)\n'%propiedades[i]

    raw_input("Pulsa una tecla para finalizar\n")

def calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador):
    templista = []

    extrapola = 0

    nfilas = len(tabla)
    ncol = len(tabla[0])

    for i in range(nfilas):
            templista.append(tabla[i][0])

    # Calcula el factor de interpolacion
    i = 0
    while(propiedad_conocida>=templista[i]) and (i+1<nfilas):
        i = i + 1
    Fx = (propiedad_conocida-templista[i-1])/(templista[i]-templista[i-1])
    if propiedad_conocida>templista[i] or i==0: # Sobrepaso o me quedo corto y extrapolo
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
