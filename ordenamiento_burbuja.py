import random

def ordenamiento_burbuja(lista):
    n = len(lista) #Obtenemos la longitud de la lista

    for i in range(n):
        for j in range(0, n -i -1): #Siempre comenzamos desde 0 y cada iteracion recorremos un indice menos
                                    # O(n) * O(n) = O(n * n) = O(n**2) complejidad polinomial

            if lista[j] > lista[j +1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

def run():
    tamano_de_lista = int(input("De que tamaño sera la lista? "))
    

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

if __name__ == "__main__":
    run()