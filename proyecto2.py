# -*- coding: utf-8 -*-



import re
import time
import os.path

from datetime import datetime
from _markerlib.markers import var


def _banner():
    """Comment"""

    return """

##########################################################################

#

# Este es el script de búsqueda de patrones de palabras en un archivo txt

#

# Autor: Jesus Correas Velez

#

##########################################################################

"""
    # ----------------------------------------------------------------------

def main():
    """Comment"""

    print(_banner())

    patron = None
    archivo = open(os.path.join(os.path.dirname(__file__), "20krockyou.txt"), "rU", encoding="utf-8")
    cadena = archivo.read()

   # for x in archivo:
        #print(x)


    # ----------------------------------------------------------------------
    # ----------------------------FUNCIONES---------------------------------

    # Funcion pregunta 1
    def f1(x):
        global patron
        if x == 1:
            patron = re.compile('([\n\r\s]\w{1,6}[\n\r \s])')
        if x == 2:
            patron = re.compile('([\n\r\s]\w{6,10}[\n\r \s])')
        if x == 3:
            patron = re.compile('([\n\r\s]\w{10,}[\n\r \s])')
        return patron

    # Funcion pregunta 2
    def f2(x):
        global patron
        if x == 1:
            patron=re.compile('([\n\r\s][[qwertasdfgzxcvbQWERTASDFGZXCV]\w[\n\r \s])')
        if x == 2:
            patron=re.compile('([\n\r\s][yuiophjklñnmYUIOPHJKLÑNM]\w[\n\r \s])')
        return patron


    # Funcion pregunta 3
    def f3(x):
        global patron
        if x == 1:
            patron = re.compile('([\n\r\s]\d\w[\n\r \s])')
        if x == 2:
            patron = re.compile('([\n\r\s]\w\d[\n\r \s])')
        return patron
    #no hacer nada

    # Funcion pregunta 4
   # def funcion4(var4):
       # if var4 == 1:
        #    if var4 == 2:
         #   if var4 == 3:

    # Funcion pregunta 5

 #   def funcion5(var5):

    # Funcion pregunta 6
  #  def funcion6(var6):


# Funcion pregunta 7
# Funcion pregunta 8
# Funcion pregunta 1
# Funcion pregunta 1
# Funcion lee diccionarios dentro del directorio
# ----------------------------------------------------------------------
    # --------------------------------VARIABLES---------------------------

    pat=[] #variable para almacenar patrones
    var=[] #variable para almacenar lo que conocemos de la persona
    # --------------------------------PREGUNTAS---------------------------


    print('[*] Comienzo del cuestionario:')

    # -------------------Preguntas basadas en lo que vemos-----------------

    # Pregunta 1

    print('    -> 1ª Pregunta: ¿Podrías estimar la longitud de la contaseña? [1|2|3|4] ', end="")
    print("    -> Opciones: \n1-Entre 1 y 6\n2-Entre 6 y 10\n3-Mas de 10\n4-No lo sé ")
    var1=int(input())


    # Pregunta 2
    print('    -> 2ª Pregunta: ¿Con que mano empezó a teclear?  [1|2|3]: ', end="")
    print("    -> Opciones: \n1-Mano izquierda\n2-Mano derecha\n3-No estoy seguro ")
    var2=int(input())



    # Pregunta 3

    print('    -> 3ª Pregunta: ¿La contraseña contiene números?[1|2|3] : ', end="")
    print("    -> Opciones: \n1-Si, al principio\n2-Sí, al final\n3-No estoy seguro ")
    var3=int(input())


    # Pegunta 4
    #print('    -> 4ª Pregunta: ¿La contraseña contiene algún espacio?[1|2|3] : ', end="")
    #print("    -> Opciones: \n1-Si\n2-No\n3-No estoy seguro ")
    #var4 = int(input())
    #pat.append(funcion4(var4))
    
    # Pregunta 5
    #print('    -> 5ª Pregunta: ¿Sabes en que añó nació el usuario? (Introduce 0 si no lo sabes)  : ', end="")
    #var5 = int(input())

    #-----------------Preguntas basadas en lo que conocemos de la persona------------

    # Pregunta 6

    #print('    -> 6ª Pregunta: ¿Crees que la contraseña podría estar relacionada con el cine?  [1|2]  : ', end="")
    #print("    -> Opciones: \n1-Si, al usuario le gusta cine\n2-No, no lo creo. ")
    #var6 = int(input())
    #var.append(funcion6(var6))
    # Pregunta 7
    #print('    -> 7ª Pregunta: ¿Crees que la contraseña podría estar relacionada con la música?  [1|2]  : ', end="")
    #print("    -> Opciones: \n1-Si, al usuario le gusta la música\n2-No, no lo creo. ")
    #var7 = int(input())
    #   var.append(funcion(var7))

    #Opciones musicales si encuentro diccionarios

    # Pregunta 8

    #print('    -> 8ª Pregunta: ¿Crees que la contraseña podría estar relacionada con el deporte?  [1|2]  : ', end="")
   # print("    -> Opciones: \n1-Si, al usuario le gusta el deporte\n2-No, no lo creo. ")
    #var8 = int(input())
    #var.append(funcion8(var8))

    # Pregunta 9

   # print('    -> 9ª Pregunta: ¿Crees que la contraseña podría estar relacionada con el deporte?  [1|2]  : ', end="")
   # print("    -> Opciones: \n1-Si, al usuario le gusta cine\n2-No, no lo creo. ")
    #var9 = int(input())
    #var.append(funcion9(var9))

# Procesamiento

    print('[*] Procedemos a buscar las posibles coincidencias ...')

    pat.append(f1(var1))
    pat.append(f2(var2))
    pat.append(f3(var3))
    #pat.append(f4(var4))
    #pat.append(f5(var5))

   # patron=pat[0]
    for i in pat:
        patron=i
        if not patron:
            print("\n[!] No se ha elegido ningún patron válido!\n")
            exit(1)
        else:


            resultados = [x.lstrip() for x in patron.findall(cadena)]
            cadena="".join(resultados)
            #print(resultados)
            #print(cadena)
            time.sleep(1)
            _nombre_fichero_resultado= "matches_%s.txt" % int(datetime.timestamp(datetime.now()))
            print("[*] Encontradas %s coincidenias. Diccionario guardado en el fichero %s\n" % (len(resultados), _nombre_fichero_resultado))




            # Guardando

            with open(_nombre_fichero_resultado, "w") as f:

                 f.writelines(resultados)



        # Mostrando resultado y guardando info
     #
    #_nombre_fichero_resultado = "matches_%s.txt" % int(datetime.timestamp(datetime.now()))

        # Mostrando
    #print("[*] Encontradas %s coincidenias. Diccionario guardado en el fichero %s\n" % (len(resulados), _nombre_fichero_resultado))




    # Guardando
    #with open(_nombre_fichero_resultado, "w") as f:

        #f.writelines(resulados)




if __name__ == '__main__':

    main()
