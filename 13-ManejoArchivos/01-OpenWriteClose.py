def app():
    archivo = open('13-ManejoArchivos/archivo.txt', 'w'); # w Es Escritura, Si No Existe Lo Creara

    # Generar Un Rango De Némeros En El Archivo
    for i in range(0, 20):
        archivo.write('Esta Es La Linea ' + str(i) + '\n')

    # Cerrar El Archivo
    archivo.close()    

app()