#-------------------------------------------------------------------------------
# Name:        modulo_fluidos
# Purpose:
#
# Author:      thmenendez
#
# Created:     07/06/2017
# Copyright:   (c) thmenendez 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def menu():

    ans = ''
    while ans not in ['A','R','N2','X']:
        ans = raw_input('Que quieres interpolar:\n* Aire (A)\n* R134a (R)\n* N2 (N2)\n* Salir (X)\n')

    if ans == 'A':
        fluido('Aire')
    elif ans == 'R':
        fluido('R134a')
    elif ans == 'N2':
        fluido('N2')
    else:
        raw_input('Pulsa una tecla para salir')


def fluido(ruta):

    import modulo_datos_vapor, modulo_interpocalor_vapor
    tabla = modulo_datos_vapor.lee_datos(ruta)
    propiedades = tabla[1]
    tabla = tabla[0]

    siglas = []
    prompt = 'Que conoces:\n'
    for i in range(len(propiedades)):
        prompt += '* '
        prompt += propiedades[i][0] + ' (' +propiedades[i][1] + ', ' +propiedades[i][2] + ')\n'
        siglas.append(propiedades[i][1])

    ans = ''
    while ans not in siglas:
        ans = raw_input(prompt)

    for i in range(len(siglas)):
        if ans == siglas[i]:
            indicador = i

    propiedad_conocida = float(raw_input('Introduce el dato conocido: '))
    datos_inter = modulo_interpocalor_vapor.calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador)

    if datos_inter[len(datos_inter)-1]==1:
        print 'EXTRAPOLACION'

    print
     # Imprime el resultado
    for i in range(len(datos_inter)-1):
        print '%s: %f %s'%(propiedades[i][0],datos_inter[i],propiedades[i][2])

    raw_input("\nPulsa una tecla para volver al menu\n")

    menu()