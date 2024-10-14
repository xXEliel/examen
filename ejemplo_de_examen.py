#8
def bubblesort(matriz, lista_precios):
    valores_totales = [0] * len(provincias)
    sucursales = provincias[:]
    for i in range(len(provincias)):
        valor_total = 0
        for j in range(len(productos)):
            valor_total += matriz[i][j] * lista_precios[j]
        valores_totales[i] = valor_total   
    for i in range(len(valores_totales)):
        for j in range(0, len(valores_totales) -i -1):
            if valores_totales[j] > valores_totales[j+1]:
                    valores_totales[j], valores_totales[j+1] = valores_totales[j+1], valores_totales[j]
                    sucursales[j], sucursales[j+1] = sucursales[j+1], sucursales[j]
    
    print("los valores ordenados de menor a mayor:")
    for i in range(len(sucursales)):
        print(sucursales[i], valores_totales[i])
#8

#7
def calcular_porcentaje(matriz):
    for i in range(len(provincias)):
        acumulador_productos = 0
        for j in range(len(productos)):
            acumulador_productos += matriz[i][j]

        print(f"\nPorcentajes de la sucursal {provincias[i]}:")
        for j in range(len(productos)):
            if acumulador_productos > 0: 
                porcentaje = (matriz[i][j] / acumulador_productos) * 100
                print(f"{productos[j]}: {porcentaje}%")
            else:
                print(f"{productos[j]}: No hay productos en la sucursal {provincias[i]}.") 
#7

#6
def sucursales_con_mas_de_20000(matriz):
        for i in range (len(provincias)):
            suma = 0
            for j in range (len(matriz[i])):
                suma += matriz[i][j]
            if suma > 20000:
                print(f"\nsucursal {provincias[i]} tiene mas de 20000 unidades con un total de {suma} unidades")
#6

#5
def sucursal_mayor(matriz, lista_precios):
    max_valor = 0
    maxima_sucursal = ""
    
    
    for i in range(len(provincias)):
        valor_total = 0
        
        for j in range(len(productos)):
            valor_total += matriz[i][j] * lista_precios[j]
        
        if valor_total > max_valor:
            max_valor = valor_total
            maxima_sucursal = provincias[i]
    
    print(f"\nLa sucursal con mayor valor económico almacenado es {maxima_sucursal} con un valor total de {max_valor}.")
            
#5    

#4
def maxima_cantidad(matriz):
    for j in range(len(productos)):
        max_cantidad = matriz[0][j]
        max_provincia = provincias[0]

        for i in range(1, len(provincias)):
            if matriz[i][j] > max_cantidad:
                max_cantidad = matriz[i][j]
                max_provincia = provincias[i]


        print(f"\nLa sucursal {max_provincia} tiene la mayor cantidad de {productos[j]} con {max_cantidad} unidades.")
#4

#3
def reponer_productos(matriz):
    for i in range(len(productos)):
        for j in range(len(provincias)):
            if matriz[i][j] < 300:
                print(f"\n{provincias[i]}|{productos[j]}")
#3

#2
def suma_total(matriz):
    for i in range (len(provincias)):
        suma = 0
        for j in range (len(matriz[i])):
            suma += matriz[i][j]
        print(f"\nsucursal {provincias[i]} tiene un total de {suma} productos")
#2

#1
def ingresar_productos(matriz):
    for i in range(len(provincias)):
        print(f"Ingrese los procutos de la sucursal {provincias[i]}")
        for j in range(len(productos)):
            matriz[i][j] = int(input(f"\nIngrese la cantidad de los productos {productos[j]}: "))


def Inicializar_matriz(cantidad_productoss:int, cantidad_columnas:int, valor_inicial:any) -> list: 
    matriz = []
    for i in range (cantidad_productoss):
        productos = [valor_inicial] * cantidad_columnas

        matriz += [productos]
    
    return matriz


def Imprimir_tablero (matriz: list):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ")
        print()
#1       


provincias = ["Santa Fe", "Cordoba", "Buenos Aires", "Salta"]
productos = ["frutas", "verduras", "carnes", "bebidas", "lacteos"]
lista_precios = [30, 40, 50, 60, 80]
while True:
    menu= int(input("Elija las opciones del 1 al 10 para ver las existencias: "))
    match menu:
        case 1:
            mi_matriz = Inicializar_matriz(len(provincias), len(productos), 0)
            ingresar_productos(mi_matriz)
            Imprimir_tablero(mi_matriz)
            print(Imprimir_tablero)
        case 2:
            suma_total(mi_matriz)
        case 3:
            reponer_productos(mi_matriz)
        case 4:
            maxima_cantidad(mi_matriz)
        case 5:
            sucursal_mayor(mi_matriz, lista_precios)    
        case 6:
            sucursales_con_mas_de_20000(mi_matriz)
        case 7:
            calcular_porcentaje(mi_matriz)
        case 8:
            bubblesort(mi_matriz, lista_precios)
        case 9:
            pass
        case 10:
            print("saliste del sistema")
            break


          
