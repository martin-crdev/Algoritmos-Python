

def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0: #Caso base para que la funcion recursiva no sea infinita
        return 0                     #Se detiene si se acaban los elementos o se acaba el tamaño del morral

    if pesos[n - 1] > tamano_morral: #Otro caso base si el peso es mayor al del morral 
        return morral(tamano_morral, pesos, valores, n - 1) #Verificamos el siguiente elemento

    # Debemos tomar una decision, meter o no meter al morral, lo voy a meter si es el valor maximo de si lo meto o no
    # si lo meto agarro la sumatoria de valores y vuelvo a ejecutar morral, haciendo mas chico el morral
    # ya que estoy metiendo el objeto al morral
    # si no lo meto simplemente checo el siguiente elemento
    return max(valores[n -1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n -1),
               morral(tamano_morral, pesos, valores, n -1))


def run():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 30
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)

if __name__ == "__main__":
    run()