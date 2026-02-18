#monitor.py
print("---Monitor de Sistema V1.0---")
reading=[]

while True:
    user_input=input("Ingresa valor del sensor o pulsa Q para salir: ")
    if user_input.lower()=='q':
        break
    #Convertir a Float y guardar
    try:
        value=float(user_input)
        reading.append(value)
    except ValueError:
        print("Error> Por favor ingresa un numero valido")
print(f"Datos capturados:{reading}")