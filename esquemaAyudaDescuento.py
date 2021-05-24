'''
    Creado por Jonathan Felipe Vargas Arias

'''
print('\n---------Bienvenido al sistema de porcentaje de ayuda de la Universidad Colombiana---------\n')
names= input('Ingrese su nombres -> ')
lastName = input('Ingrese apellidos -> ')
edad = int(input('Ingrese su edad en años el interesado debe tener como minimo 15 años -> '))
puntajePrueba = int(input('Ingrese el puntaje obtenido en el examen -> '))
numeroSalarios = int(input('Ingrese el número decimal de salarios mínimos mensuales que tiene de ingreso familiar \n ejemplo  1,2 salarios minimos -> '))
porcentajeApoyo = 0

#Se calcula el porcentaje dependiento de la edad que proporciona el usuario
def descuentoPorEdad (edad):
    if(edad>=15 and edad <= 18):
        return 25
    elif(edad>=19 and edad <= 21):
        return 15
    elif(edad>=22 and edad <= 25):
        return 10
    elif (edad >=26):
        return 0

#Se calcula el porcentaje dependiento de la salarios que proporciona el usuario
def descuentoPorIngreso (numeroSalarios):
    if(numeroSalarios <= 1):
        return 30
    elif(numeroSalarios >1 and numeroSalarios <=2):
        return 20
    elif(numeroSalarios >2 and numeroSalarios <=3):
        return 10
    elif(numeroSalarios >3 and numeroSalarios <=4):
        return 5
    else:
        return 0

#Se calcula el porcentaje dependiento de la puntaje prueba que proporciona el usuario
def descuentoPuntajePorExamen(puntajePrueba):
    if(puntajePrueba >=80 and puntajePrueba < 86):
        return 30
    elif(puntajePrueba >= 86 and puntajePrueba <91):
        return 35
    elif(puntajePrueba >= 91 and puntajePrueba < 96):
        return 40
    elif(puntajePrueba >= 96 and puntajePrueba<=100):
        return 45
    elif(puntajePrueba < 80):
        return 0

#Se calcula el porcentaje total de descuento
def calcularPorcentajeApoyo( edad, numeroSalarios,puntajePrueba):
    porcentajeApoyo = descuentoPorEdad(edad)
    porcentajeApoyo = porcentajeApoyo + descuentoPorIngreso(numeroSalarios)
    return porcentajeApoyo + descuentoPuntajePorExamen(puntajePrueba)

def ejecutarPrograma():
    print('\nUsuario : ',names,' ', lastName,'\n')
    print('El descuento recibido por edad = ',descuentoPorEdad(edad),'%\n')
    print('El descuento recibido por el ingreso familiar = ', descuentoPorIngreso(numeroSalarios),'%\n')
    print('El descuento recibido por el puntaje del examen = ', descuentoPuntajePorExamen(puntajePrueba),'%\n')
    print('El descuento total que recibirá sobre el valor de la matrícula = ', calcularPorcentajeApoyo(edad, numeroSalarios,puntajePrueba),'%\n')

ejecutarPrograma()
