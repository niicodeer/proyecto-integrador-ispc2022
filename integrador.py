import time
numeros = []

## Sección de funciones para trabajar los números ingresados
def sumar(numeros):
    suma= 0
    for num in numeros:
        suma = suma + num;
    print("-La suma de los números ingresados es: ", suma);

def promedio(numeros):
    suma= 0
    for num in numeros:
       suma = suma + num;
    promedio = suma / len(numeros);
    print("-El promedio de los números ingresados es: ", promedio);

def maximo(numeros):
     numMax = max(numeros);
     print("-De los números ingresados, el máximo es: ", numMax);

def minimo(numeros):
    numMin = min(numeros);
    print("-De los números ingresados, el mínimo es: ", numMin);


## Pido al usuario que indique la cantidad de números que quiere ingresar y luego que ingrese los números y los agrego a una lista.
name = input("¿Quién está ejecutando este código?: ")
time.sleep(0.5)
def pedirCantidad():
    contador = 0;
    print(f"Hola {name}! Te voy a pedir una cantidad de números y luego trabajaremos con ellos")
    time.sleep(1)
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar?: "))
        time.sleep(1)
        if(cantidad >0):
            while contador < cantidad:
                try:
                    numeros.append(float(input("Ingrese un número: ")));
                except:
                    print("Debes ingresar solamente números enteros!!!")
                    time.sleep(0.5)
                    numeros.append(float(input("Ingrese un número: ")));

                contador = contador + 1
        else:
            print("Debes ingresar un número entero mayor que cero!")
            time.sleep(1)
            pedirCantidad()
        print("")
    except:
        print("Debes ingresar un número entero mayor que cero!")
        time.sleep(0.5)
        pedirCantidad()

pedirCantidad()

time.sleep(1)
print("*** Los números que introdujiste son: ", numeros, " ***");
print("")
print("----------------------------------------");

opcion="";
while (opcion != "0"):
    time.sleep(1.5)
    print("")
    print("¿Qué operación desear hacer?:\n 1. Sumar los números.\n 2. Sacar el promedio de los números.\n 3. Saber el número máximo.\n 4. Saber el número mínimo.\n 0. Terminar")
    print("")

    opcion = (input("Selecciona una opción: "))
    time.sleep(1)
    if (opcion == "1"):
        sumar(numeros)
    elif (opcion == "2"):
        promedio(numeros)
    elif (opcion == "3"):
        maximo(numeros)
    elif (opcion == "4"):
        minimo(numeros)
    elif(opcion == "0"):
        print(f"Gracias {name}! :D")
    else:
        print('Ingrese sólo las opciones disponibles')
time.sleep(1)
print("Fin del programa")
print("----------------------------------------");



