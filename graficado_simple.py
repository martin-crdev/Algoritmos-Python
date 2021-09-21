from bokeh.plotting import figure, output_file, show
#Figure es la ventana en donde vamos a graficar, outpu_file determina el nombre del archivo como output

if __name__ == "__main__":
    output_file("graficado_simple.html")#Asignamos el nombre del archivo como html para visualizar
    fig = figure() #Generamos la figura donde generamos nuestros graficos

    total_vals = int(input("Cuantos valores quieres graficar?"))
    x_vals = list(range(total_vals)) #Generamos valores para el eje x
    y_vals = [] #El usuario nos dara los valores del eje y

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width = 2) #Agregamos a nuestra figura los valores del eje X y Y para graficar
    show(fig) #Genera un servidor que se prende y que nos muestra el archivo html