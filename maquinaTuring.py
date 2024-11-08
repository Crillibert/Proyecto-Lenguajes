
import re
from graphviz import Digraph

# Genera tabla de frecuencia para imprimir
def generarTabla(mensaje):
    pilaErrores = []
    estado = '0'
    tabla = [['|||'],['|0|'],['|1|'],['|2|'],['|3|'],['|4|']]
    pasarG4 = False
    #Evalua el estado y actua de acuerdo al caracter leido y el estado
    for i in mensaje:
        i = "|" + i + "|"
        if estado == "0":
            tabla[0].append(i)
            if i == "|a|":
                tabla[1].append("|1|")
                estado = '1'
            else:
                tabla[1].append("|0|")

                # Generar pilas errores 
                pilaErrores.append(i)
        
        elif estado == "1":
            tabla[0].append(i)
            if i == "|b|":
                tabla[2].append("|2|")
                estado = '2'
            else:
                tabla[2].append("|1|")

                pilaErrores.append(i)


        elif estado == "2":

            tabla[0].append(i)
            estado = "3"
            

           
            tabla[3].append("|3|")
            

        elif estado == "3":
            tabla[0].append(i)
            if i == "|b|":
                tabla[4].append("|1|")
                estado = "1"
            elif i == "|a|":
                tabla[4].append("|3|")
                estado = "3"
            elif i == "|*|":
                tabla[4].append("|4|")
                estado = "4"
            

        elif estado == "4":
            tabla[0].append(i)
            if i == "|#|":
                tabla[5].append("|4|")
                estado = "4"
            elif i == "|a|":
                tabla[5].append("|1|")
                estado = "1"
            elif i == "|b|":
                tabla[5].append("|2|")
                estado = "2"
            
        for z in range (len(tabla)):
            if len(tabla[z]) < len(tabla[0]):
                tabla[z].append("|-|")
    
    for r in tabla:
        print(' '.join(map(str,r)))
    print('\nPila de errores\n')
    for z in pilaErrores:
        print(z)

    return(pilaErrores)

    
# Función para obtener el siguiente estado según la tabla de transición
def obtener_siguiente_estado(estado_actual, caracter):
    tabla_transicion = {
        '0': {'a': '1'},
        '1': {'b': '2'},
        '2': {'a': '3'},
        '3': {'a': '3', 'b': '1', '*': '4'},
        '4': {'a': '3', 'b': '1', '#': '4'}
    }
    
    if estado_actual in tabla_transicion and caracter in tabla_transicion[estado_actual]:  # Verifica si el estado actual y el caracter están en la tabla de transición.
        return tabla_transicion[estado_actual][caracter] # Retorna el siguiente estado.
    else:
        return '4'  # Estado de error

# Función para generar el árbol de derivación
def generar_arbol_derivacion(cadena, numero):  # Crea un nuevo gráfico para el árbol de derivación
    dot = Digraph(comment=f'Árbol de Derivación - Cadena {numero}')
    dot.attr(rankdir='TB')  # Establece la dirección del gráfico de arriba hacia abajo (Top To Bottom)

    estado_actual = '0' # Comienza en el estado inicial
    for i, caracter in enumerate(cadena): # Itera sobre cada caracter de la cadena
        estado_siguiente = obtener_siguiente_estado(estado_actual, caracter) # Obtiene el siguiente estado

        # Se usa el mismo nodo si apunta a sí mismo
        if estado_siguiente == estado_actual:
            dot.node(f"{estado_actual}", estado_actual)  # Solo crea un nodo para el estado
            dot.edge(f"{estado_actual}", f"{estado_siguiente}", label=caracter)  # Muestra la transición
        else:
            dot.node(f"{estado_actual}", estado_actual)  # Crea un nodo para el estado actual
            dot.node(f"{estado_siguiente}", estado_siguiente)  # Crea un nodo para el siguiente estado
            dot.edge(f"{estado_actual}", f"{estado_siguiente}", label=caracter)  # Muestra la transición
        
        estado_actual = estado_siguiente # Actualiza el estado actual al siguiente estado.

    # Añadir colores a los nodos finales para el estado de aceptación
    if estado_actual == '4' and cadena[-1] == '#':
        dot.node(f"{estado_actual}", estado_actual, color='green', style='filled') #verde si se llega al estado de aceptación
    else:
        dot.node(f"{estado_actual}", estado_actual, color='red', style='filled') #Rojo si no se llega al estado de aceptación

    #  # Genera el archivo del árbol de derivación en formato PNG y limpia los archivos temporales que cera grapviz para renderizar la imagen.
    dot.render(f'arbol_derivacion_cadena_{numero}', format='png', cleanup=True)

patron = re.compile("(.*a)(.*b)(a)(b\2|a*\*)(#+|a\2|b\3)")
print("\nValidación de cadenas:")
simbolos = ['a', 'b', '*', '#', '.']
print("Se mueve de izquierda a derecha ambas cintas")
print(simbolos)
try:
    with open("nuevaCadena.txt", 'r') as reader:
        for numero, line in enumerate(reader.readlines(), 1):
            cadena = line.strip()
            cintaInpar = ""
            cintaPar = ""
            par = False
            for z in cadena:
                if par:
                    cintaPar += z
                else: 
                    cintaInpar += z
                par = not par
                
                #generar_arbol_derivacion(cadena, numero)  # Generar árbol


            if re.fullmatch(patron, cintaPar):
                cinta1 = []
                print(f"Cadena Cinta 1: {numero}: {cintaPar}")
                print('---Es válido---')
                print('Tabla de transiciones:\n')
                pila = generarTabla(cintaPar)
                for s in cintaPar:
                    cinta1.append(s)
                generar_arbol_derivacion(cinta1, numero)  # Generar árbol

            if re.fullmatch(patron, cintaInpar):
                cinta2 = []
                print(f"Cadena Cinta 2: {numero}: {cintaInpar}")
                print('---Es válido---')
                print('Tabla de transiciones:\n')
                pila = generarTabla(cintaInpar)
                for s in cintaInpar:
                    cinta2.append(s)
                generar_arbol_derivacion(cinta2, numero)  # Generar árbol

            if not re.fullmatch(patron, cintaPar):
                print(f"Cadena Cinta 1 {numero}: {cintaPar}")
                print('---No es válido---\n')
                #generar_arbol_derivacion(cadena, numero)  # Generar árbol   
            if not re.fullmatch(patron, cintaInpar):
                print(f"Cadena Cinta 2 {numero}: {cintaInpar}")
                print('---No es válido---\n')
                #generar_arbol_derivacion(cadena, numero)  # Generar árbol   
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo 'cadena.txt'.")
except IOError:
    print("Error: Hubo un problema al leer el archivo 'cadena.txt'.")


