with open("cadena.txt", 'r') as cinta:
    linea1 = ''
    linea2 = ''
    lineaNueva = ''
    par = False
    
    for linea in cinta.readlines():
        i = 0
        if linea1 == '':
            linea1 = linea
        elif linea2 == '':
            linea2 = linea
        else:
             if len(linea1) > len(linea2):
                 x = len(linea2)
             else:
                 x = len(linea1)
             while i < x:
                 if par:
                     lineaNueva += linea1[i]
                 else:
                      lineaNueva += linea2[i]
                 par = not(par)
                 i += 1

                 
            