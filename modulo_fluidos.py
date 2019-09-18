#-------------------------------------------------------------------------------
# Name:        modulo_fluidos
# Purpose:
#
# Author:      thmenendez
#
# Created:     05/06/2017
# Copyright:   (c) thmenendez 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def menu():

    ans = ''
    while ans not in ['A','R','N2','X']:
        ans = raw_input('Que quieres interpolar:\n* Aire (A)\n* R134a (R)\n* N2 (N2)\n* Salir (X)\n')

    if ans == 'A':
        aire()
    elif ans == 'R':
        R134a()
    elif ans == 'N2':
        N2()
    else:
        raw_input('Pulsa una tecla para salir')


def aire():

    ans = ''
    while ans not in ['T','h','Pr','u','Vr','S']:
        ans = raw_input('Que conoces:\n* Temperatura (T, K)\n* Entalpia (h, kJ/kg)\n* Presion relativa (Pr)\n* Energia interna (u, kJ/kg)\n* Volumen relativo (Vr)\n* Entropia (S, kJ/(kg*K)\n')

    if ans == 'T':
        indicador = 0
    elif ans == 'h':
        indicador = 1
    elif ans == 'Pr':
        indicador = 2
    elif ans == 'u':
        indicador = 3
    elif ans == 'Vr':
        indicador = 4
    else:
        indicador = 5

    propiedad_conocida = float(raw_input('Introduce el dato conocido: '))

    import modulo_datos_vapor, modulo_interpocalor_vapor
    tabla = modulo_datos_vapor.lee_datos('Aire')
    propiedades = modulo_interpocalor_vapor.calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador)

    if propiedades[len(propiedades)-1]==1:
        print 'EXTRAPOLACION'

     # Imprime el resultado
    for i in range(len(propiedades)):
        if i == 0:
            print 'Temperatura: %f K'%propiedades[i]
        elif i == 1:
            print 'Entalpia: %f kJ/kg'%propiedades[i]
        elif i == 2:
            print 'Presion relativa: %f'%propiedades[i]
        elif i == 3:
            print 'Energia interna: %f kJ/kg'%propiedades[i]
        elif i == 4:
            print 'Volumen relativo: %f'%propiedades[i]
        elif i == 5:
            print 'Entropia: %f kJ/(kg*K)'%propiedades[i]

    raw_input("Pulsa una tecla para volver al menu\n")

    menu()

def R134a():

    ans = ''
    while ans not in ['T','P']:
        ans = raw_input('Que conoces:\n* Temperatura (T)\n* Presion (P)\n')

    if ans == 'T':
        indicador = 0
    else:
        indicador = 1

    propiedad_conocida = float(raw_input('Introduce el dato conocido: '))

    import modulo_datos_vapor, modulo_interpocalor_vapor
    tabla = modulo_datos_vapor.lee_datos('R134a')
    propiedades = modulo_interpocalor_vapor.calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador)

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

    raw_input("Pulsa una tecla para volver al menu\n")

    menu()

def N2():

    ans = ''
    while ans not in ['T','h','u','S']:
        ans = raw_input('Que conoces:\n* Temperatura (T, K)\n* Entalpia (h, kJ/kg)\n* Energia interna (u, kJ/kg)\n* Entropia (kJ/(kg*K)\n')

    if ans == 'T':
        indicador = 0
    elif ans == 'h':
        indicador = 1
    elif ans == 'u':
        indicador = 2
    else:
        indicador = 3

    propiedad_conocida = float(raw_input('Introduce el dato conocido: '))

    import modulo_datos_vapor, modulo_interpocalor_vapor
    tabla = modulo_datos_vapor.lee_datos('N2')
    propiedades = modulo_interpocalor_vapor.calculo_interpocalor_vapor(tabla,propiedad_conocida,indicador)

    if propiedades[len(propiedades)-1]==1:
        print 'EXTRAPOLACION'

     # Imprime el resultado
    for i in range(len(propiedades)):
        if i == 0:
            print 'Temperatura: %f K'%propiedades[i]
        elif i == 1:
            print 'Entalpia: %f kJ/kg'%propiedades[i]
        elif i == 2:
            print 'Energia interna: %f kJ/kg'%propiedades[i]
        elif i == 3:
            print 'Entropia: %f kJ/(kg*K)'%propiedades[i]

    raw_input("Pulsa una tecla para volver al menu\n")

    menu()
