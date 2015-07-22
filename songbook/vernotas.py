# -*- coding: utf-8 -*-
notas = (
    ' C ',' D ',' E ',' F ',' G ',' A ',
    ' C7 ',' D7 ',' E7 ',' F7 ',' G7 ',' A7 ',
    ' Cm ',' Dm ',' Em ',' Fm ',' Gm ',' Am ',
    ' C# ',' D# ',' E ',' F# ',' G# ',' A# ',
    ' C#m ',' D#m ',' E ',' F#m ',' G#m ',' A#m ',
    ' Do ',' Re ',' Mi ',' Fa ', ' Sol ',' La ', ' Si ',
    ' Do7 ',' Re7 ',' Mi7 ',' Fa7 ',' Sol7 ',' La7 ', ' Si7 ',
    ' Do# ',' Re# ',' Mi ',' Fa# ',' Sol# ',' La# ',' Si# ',
    ' Do#m ',' Re#m ',' Mim ',' Fa#m ',' Sol#m ',' La#m ',' Si#m ',
    )

texto = u"""
Re     Sol          Re
Dios espera en el altar
                  La7 
vamos todos hacia él
 Sol                   Re# 
llevemos nuestras sonrisas
                       La7 
la inquietud, nuestra hambre
           Re 
y nuestra sed.

           Sol       Re
Dios sobre todo es amor
                      La7 
quiere  nuestra salvación
 Sol              Re
que juntos nos salvemos
                La7       Re
para ir de la mano hacia Dios.

                Sol     Re
Al entrar a la casa de Dios
                           La7
libre de rencores he de entrar
 Sol                Re
llevar el alma tranquila
                  La7             Re
y pensar que al salir más he de amar

        La7            Re
ESE ES CRISTO, ESE ES DIOS
         La7   Sol      Re
ESE ES CRISTO, NUESTRO DIOS

"""
tonos = []
tonos_arriba = False

def containsAny(str, set):
    """Check whether'str' contains ANY of the chars in'set'"""
    return 1 in [c in str for c in set]
import re
lineas = texto.split('\n')
index = 0
es_letra = False
lineas_a_eliminar =  []
for linea in lineas:
    if containsAny(linea, notas):
        tonos_arriba = True    
        es_letra = False
        for nota in notas:
            posiciones = [m.start() for m in re.finditer(nota, linea)]
            if posiciones and posiciones != [0]:
                for posicion in posiciones:
                    tonos.append((posicion, nota))
    elif tonos_arriba:
        es_letra = True
        tonos = sorted(tonos,key=lambda x: x[0])
        notas_numero = 0
        caracteres_agregados = 0
        for tono in tonos:
            nota = tono[1]
            nota=nota[1:len(nota)-1]
            nota_str = '['+nota+']'
            posicion = tono[0] + caracteres_agregados+1
            if len(linea) < posicion:
                while len(linea) < posicion:
                    linea += ' '
            linea = linea[:posicion]+nota_str+linea[posicion:]
            notas_numero += 1
            caracteres_agregados += len(nota_str)
        lineas[index] = linea
        lineas_a_eliminar.append(index-1)
        tonos = []
        tonos_arriba = False

    index += 1

index = 0
for linea_eliminar  in lineas_a_eliminar:
    lineas.pop(linea_eliminar-index)
    index += 1
# print lineas

print '\n'.join(lineas)
    
    
    

