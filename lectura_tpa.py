""""
import os
url_way = ''  # Inicializar la variable url_way con una cadena vacía

while True:
    print('----- MENÚ -----')
    print('1: Seleccionar número de pos de waystation')
    print('2: Ingresar IP de pos a analizar')
    print('0: Salir')
    opcion = input('Ingrese una opción: ')

    
    if opcion == '1':
        pos_number = input('Ingrese número de pos: ')
        fecha_tpa = input('Ingrese una fecha en formato YYYYMMDD: ')
        url_way = r"D:\newpos61\POSFILES\LOGS\tlog\POS00" + pos_number
        tpa_way = url_way + "\\" + "nptrx_POS00" + pos_number + "_" + fecha_tpa + ".tpa"
        confirmacion = input('Este es el .tpa para analizar: ' + tpa_way + '. ¿Desea continuar? (si/no): ')
        intentos = 0
        while intentos < 3:           
            if confirmacion.lower() == "si":
                try:
                    with open(tpa_way, 'r') as archivo:
                        contenido = archivo.read()
                    if '997110761301310013' in contenido:
                        print('Se encontró cierre de TPA.')
                        input('Presione una tecla para volver al menu')
                        break
                    else:
                        print('No se encontró cierre de TPA.')
                        input('Presione una tecla para volver al menu')
                        break
                except FileNotFoundError:
                    print('El archivo no pudo ser encontrado. Verifica la ruta y el número de pos ingresados.')
                    input('Presione una tecla para volver al menu')
                    break

            elif confirmacion.lower() == "no":               
                pos_number = input('Ingrese número de pos: ')
                fecha_tpa = input('Ingrese una fecha en formato YYYYMMDD: ')
                url_way = r"D:\newpos61\POSFILES\LOGS\tlog\POS00" + pos_number
                tpa_way = url_way + "\\" + "nptrx_POS00" + pos_number + "_" + fecha_tpa + ".tpa"
                confirmacion = input('Este es el .tpa para analizar: ' + tpa_way + '. ¿Desea continuar? (si/no): ')
                intentos += 1
                if intentos >= 3:
                    print('Se alcanzó el máximo de intentos permitidos. El programa se cerrará.')
                    input('Presione una tecla para volver al menu')
            elif confirmacion.lower() !="no":
                print('Por favor, volver a ingresar los datos nuevamente')
                input('Presione una tecla para volver al menu')
                break

    elif opcion == '2':
        ip_pos = input('Ingrese IP completa de pos: ')
        url_pos = "\\"+"\\" + ip_pos + "\\e$\\newpos61\\posfile\\logs"
        url_clean = url_pos.replace('\\', '\\')
        confirmacion = input('Este es el .tpa para analizar: ' + url_clean + '. ¿Desea continuar? (si/no): ')
        intentos = 0
        while intentos < 3:           
            if confirmacion.lower() == "si":
                try:
                    os.chdir(url_clean)
                    print('Acceso exitoso a la carpeta: ' + url_clean)    
                    if '997110761301310013' in contenido:
                        print('Se encontró cierre de TPA.')
                        input('Presione una tecla para volver al menu')
                        break
                    else:
                        print('No se encontró cierre de TPA.')
                        input('Presione una tecla para volver al menu')
                        break
                except OSError as e:
                    print('Error al acceder a la carpeta: ' + str(e))
                    input('Presione una tecla para volver al menu')
                    break

            elif confirmacion.lower() == "no":               
                ip_pos = input('Ingrese IP completa de pos: ')
                url_pos = "\\"+"\\" + ip_pos + "\\e$\\newpos61\\posfile\\logs"
                url_clean = url_pos.replace('\\', '\\')
                confirmacion = input('Este es el .tpa para analizar: ' + url_clean + '. ¿Desea continuar? (si/no): ')
                intentos += 1
                if intentos >= 3:
                    print('Se alcanzó el máximo de intentos permitidos. El programa se cerrará.')
                    input('Presione una tecla para volver al menu')
            elif confirmacion.lower() !="no":
                print('Por favor, volver a ingresar los datos nuevamente')
                input('Presione una tecla para volver al menu')
                break

    elif opcion == '0':
        print('Saliendo')
        break

    else:
        print('Opción no válida. Por favor, ingrese una opción válida.')



# una vez que toma la info correcta analizar tpa y anotar evt contarlos y mostrarlos (dar una preview de los eventos)
# hacer seccion de resultados de los test (si tiene o no el resultado obtenido) y poner ok o fail
# hacer la secuncia de la toma de datos y de lectura para un posterior resultado

"""