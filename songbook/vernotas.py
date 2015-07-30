# -*- coding: utf-8 -*-


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


def containsAny(str, set):
    """Check whether'str' contains ANY of the chars in'set'"""
    return 1 in [c in str for c in set]
    
lineas = texto.split('\n')

index = 0
es_letra = False

lineas_de_tono =  []
linea_notas = {
    'notas':[]
}

class LyricNotes(list):
    def __init__(self, texto):
        lineas = self.get_lineas_notas(texto)
        
        self.add_notes_to_letter(lineas)

    def add_notes_to_letter(self, lineas):
        """ Poner las notas en las posiciones indicadas. """

        for linea_nota in lineas['notas']:
            index = linea_nota['index']
            nueva_linea = lineas['letra'][index]
            caracteres_agregados = 0
            for nota in linea_nota['notas']:
                nota_str = '['+nota[1].lstrip().rstrip()+']'
                posicion_nota = nota[0]
                posicion = posicion_nota + caracteres_agregados+1
                            
                # Si la posicion de la nota es mayor al tamaño de la linea agregar espacios en blanco
                if len(nueva_linea) < posicion:
                    while len(nueva_linea) < posicion:
                        nueva_linea += ' '

                nueva_linea = nueva_linea[:posicion]+nota_str+nueva_linea[posicion:]
                caracteres_agregados += len(nota_str)

            lineas['letra'][index] = nueva_linea
        
        for linea in lineas:
            print linea['letra']
            # self.append(linea['letra'])


    def containsAny(str, set):
        """ Check whether'str' contains ANY of the chars in'set'"""

        return 1 in [c in str for c in set]
        
    def get_lineas_notas(self, texto): 
        """ Obtiene las lineas con notas musicales 
        y las devuelve como un lista con las notas y sus posiciones.

        """

        lineas = texto.split('\n')
        notas = (
            ' C ',' D ',' E ',' F ',' G ',' A ',
            ' C7 ',' D7 ',' E7 ',' F7 ',' G7 ',' A7 ',
            ' Cm ',' Dm ',' Em ',' Fm ',' Gm ',' Am ',
            ' C# ',' D# ',' E ',' F# ',' G# ',' A# ',
            ' C#m ',' D#m ',' E ',' F#m ',' G#m ',' A#m ',
            ' Do ',' Re ',' Mi ',' Fa ', ' Sol ',' La ', ' Si ',
            ' Do7 ',' Re7 ',' Mi7 ',' Fa7 ',' Sol7 ',' La7 ', 


            ' Si7 ',
            ' Do# ',' Re# ',' Mi ',' Fa# ',' Sol# ',' La# ',' Si# ',
            ' Do#m ',' Re#m ',' Mim ',' Fa#m ',' Sol#m ',' La#m ',' Si#m ',
        )

        import re
        lineas_notas = []
        for index, linea in enumerate(lineas):
            # Si la linea tiene notas
            if containsAny(linea, notas):
                linea_nota = {
                    'index': index+1,
                    'notas':[]
                }
                for nota in notas:
                    posiciones = [m.start() for m in re.finditer(nota, linea)]
                    if posiciones and posiciones != [0]:
                        for posicion in posiciones:
                            linea_nota['notas'].append((posicion,nota))    
                linea_nota['notas'] = sorted(linea_nota['notas'],key=lambda x: x[0])
                
                lineas_notas.append(linea_nota)
                lineas.pop(index)
        return {
            'letra': lineas,
            'notas': lineas_notas,
        }


texto_notas = LyricNotes(texto)
print texto_notas

# for linea in lineas:
#     # Si la linea tiene notas
#     if containsAny(linea, notas):
#         for nota in notas:
#             posiciones = [m.start() for m in re.finditer(nota, linea)]
#             if posiciones and posiciones != [0]:
#                 for posicion in posiciones:
#                     lineas_notas['notas'].append((posicion,nota))

#         # se ordenan las notas por posicion
#         linea_notas['notas'] = sorted(linea_notas['notas'],key=lambda x: x[0])
#         lineas_de_tono.append(index)
#     # Si hay una linea arriba con notas si enlaza con la linea
#     elif len(linea_notas['notas']) > 0:
        
#         caracteres_agregados = 0
#         # se recorren todas las notas para enlazarlas con la linea actual
#         for tono in linea_notas['notas']:
#             nota = tono[1].lstrip().rstrip()
#             nota_str = '['+nota+']'
#             posicion = tono[0] + caracteres_agregados+1
            
#             # Si la posicion de la nota es mayor al tamaño de la linea agregar espacios en blanco
#             if len(linea) < posicion:
#                 while len(linea) < posicion:
#                     linea += ' '

#             linea = linea[:posicion]+nota_str+linea[posicion:]
#             caracteres_agregados += len(nota_str)

#         # lineas[index] = linea
#         linea_notas = {
#             'notas':[]
#         }
    
#     index += 1

# index = 0
# print lineas_de_tono
# for linea_eliminar  in lineas_de_tono:
#     lineas.pop(linea_eliminar-index)
#     index += 1
# # print lineas

# print '\n'.join(lineas)
    
    
    

