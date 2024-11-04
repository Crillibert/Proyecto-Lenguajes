with open("cadena.txt", 'r') as cinta:
    linea1 = ''
    linea2 = ''
    lineaNueva = ''
    par = False
    alternador = True
    for linea in cinta.readlines():
        i = 0

        if alternador:
            linea1 = linea
        else:
            linea2 = linea
        alternador = not alternador

        if linea1 != '' and linea2 != '':
             if len(linea1) > len(linea2):
                 x = len(linea2)
             else:
                 x = len(linea1)
             while i < x:
                 
                lineaNueva += linea1[i]
                 
                lineaNueva += linea2[i]
                par = not(par)
                i += 1
             lineaNueva = lineaNueva + '\n'
             linea1 = ''
             linea2 = ''
    with open("nuevaCadena.txt", 'w') as dobleCinta:
        dobleCinta.write(lineaNueva)
        dobleCinta.close
    cinta.close()         
            