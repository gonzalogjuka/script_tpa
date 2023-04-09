url_way = ''  # Inicializar la variable url_way con una cadena vacía


while True:
    print('----- MENÚ -----')
    print('1: Seleccionar número de pos de waystation')
    print('2: Ingresar IP de pos a analizar')
    print('0: Salir')
    opcion = input('Ingrese una opción: ')



    if opcion == '1':
        pos_number = input('Ingrese número de pos: ')
        url_way = r"D:\newpos61\POSFILES\LOGS\tlog\POS00" + pos_number
        print('El número de pos es el siguiente: ' + url_way)

    try:
        with open(url_way, 'r') as archivo:
            contenido = archivo.read()
            if '997110761301310013' in contenido:
                print('Se encontró cierre de TPA.')
            else:
                print('No se encontró encontró cierre de TPA.')
    except FileNotFoundError:
        print('El archivo no pudo ser encontrado. Verifica la ruta y el número de pos ingresados.')

        elif opcion == '2':        
        ip_pos = input('Ingrese IP completa de pos: ')
        url_pos = "\\" + ip_pos + r"\e$\newpos61\posfile\logs"
        print('La IP elegida es: ' + ip_pos)
        elif opcion == '0':
        print('Saliendo...')
        break
    else:
        print('Opción no válida. Por favor, ingrese una opción válida.')

# una vez que toma la info correcta analizar tpa y anotar evt contarlos y mostrarlos (dar una preview de los eventos)
# hacer seccion de resultados de los test (si tiene o no el resultado obtenido) y poner ok o fail
# hacer la secuncia de la toma de datos y de lectura para un posterior resultado