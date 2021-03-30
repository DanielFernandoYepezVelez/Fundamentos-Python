""" FUNCIONES PARA TAREAS PEQUEÑAS Y REPETITIVAS 
Y todo SU CONTENIDO ES UNA LINEA DE CÓDIGO """

""" El Return Se Utiliza Principalmente Para Procesar La
Información Y Luego Retornar Dicha Información, Pero Procesada """

""" Recibe un anio y retorna un string, 
con el producto del año por 3 """

def anio(parametro): return f'Año final es {parametro * 3}'

def hola(parameter_list): return print(f'hola {parameter_list}')

def informacion(nombre): return nombre

print(anio(2003))

hola('Mundo')

empleado = informacion('Daniel Fernando Yepez Vélez')
print(empleado)