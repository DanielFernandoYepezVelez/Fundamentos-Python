# Para Crear  Y Manejar Directorios (Carpetas) Importamos La Libreria Os
import os

# Path Donde Se Crea La Carpeta Y La Extensión De Los Archivos
CARPETA = '14-Ejercicios/03-ProyectoFinal/contactos/'
EXTENSION = '.txt'

""" LA IDEA ES COMBINAR LO APRENDIDO POR ENDE, VAMOS A CREAR CLASE PARA CONTACTO """
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    crear_directorio()
    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = int(input('\nSeleccione Una Opción: \n'))

        # Ejecutar Las Opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            print('Buscar Contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar Contacto')
            preguntar = False
        else:
            print('La Opción Ingresada No Es Válida, Intente De Nuevo')

""" LISTANDO LOS ARCHIVOS DE CONTACTO """
def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    # En Una Base De Datos, Aqui Va La Consulta SQL 
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            # Imprime Un Separador Por Cada Archivo Del Contacto
            print('\n')

            for linea in contacto:
                # Imprime El Contenido Del Archivo
                print(linea.rstrip())

def editar_contacto():
    print('\nEscribe El Nombre Del Contacto A Editar')
    nombre_anterior = input('Nombre Del Contacto Que Desea Editar\n')

    # Revisar Si El Archivo Existe Antes De Editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        # Ubicación Del Archivo Donde Se Pretende Editar. Alias(archivo)
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Nuevo Nombre Contacto:\n')
            telefono_contacto = input('Nuevo Telefono Contacto:\n')
            categoria_contacto = input('Nuevo Categoria Contacto:\n')

            # Instanciar La Clase Contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write(f'Nombre: {contacto.nombre}\n')
            archivo.write(f'Telefono: {contacto.telefono}\n')
            archivo.write(f'Categoria: {contacto.categoria}\n')

            # Cerrar El Archivo
            archivo.close()

            # Renombrar El Archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + contacto.nombre + EXTENSION)
            print('\n***** Contacto Editado Correctamente *****\n')

    else:
        print('\n***** ¡¡¡OJO!!! Ese Contacto NO!!! Existe *****')

    # Reiniciar La App()
    app()

def agregar_contacto():
    print('\nEscribe Los Datos Para Agregar El Nuevo Contacto')
    nombre_contacto = input('Nombre Contacto:\n')

    # Revisar Si El Archivo Existe Antes De Crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
        # Ubicación Del Archivo Donde Se Pretende Escribir. Alias(archivo)
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            telefono_contacto = input('Telefono Contacto:\n')
            categoria_contacto = input('Categoria Contacto:\n')

            # Instancia De La Clase Contacto 
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write(f'Nombre: {contacto.nombre}\n')
            archivo.write(f'Telefono: {contacto.telefono}\n')
            archivo.write(f'Categoria: {contacto.categoria}\n')
            
            print('\n***** Contacto Creado Correctamente *****\n')
    else:
        print('\n***** ¡¡¡OJO!!! Ese Contacto Ya Existe *****')

    # Reiniciar La App()
    app()

def mostrar_menu():
    menu = '\nSeleccione Del Menú Lo Que Desea Hacer:\n'
    menu += '1) Agregar Nuevo Contacto\n'
    menu += '2) Editar Contacto\n'
    menu += '3) Ver Contactos\n'
    menu += '4) Buscar Contacto\n'
    menu += '5) Eliminar Contacto'
    print(menu)

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    # Revisar Si El Archivo Existe Antes De Crearlo
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()    