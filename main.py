def calcular_medidas(horizontal: float, vertical: float) -> tuple[str, float, float]:
    """
    Devuelve una tupla con el área y el perímetro, en ese orden. El área es el producto de la base por la altura; el perímetro es el doble de la suma de ambas.
    Devuelve "cuadrado" si ambas medidas son iguales, "horizontal" si la base es mayor que la altura y "vertical" en el caso restante.
    :param: horizontal
    :param: vertical
    :return: forma
    :return: area
    :return: perimetro
    """

    if horizontal > vertical:
        forma = "horizontal"
    elif vertical > horizontal:
        forma = "vertical"
    else:
        forma = "cuadrado"

    area = horizontal * vertical

    perimetro = (horizontal + vertical)*2

    return forma, area, perimetro

def main():

    print("Entrada:")
    horizontal_entrada = float(input("horizontal: "))
    vertical_entrada = float(input("vertical: "))
    salida = calcular_medidas(horizontal_entrada, vertical_entrada)
    print("Salida:")
    print("Forma: ", salida[0])
    print("Área: ", salida[1], "cm²")
    print("Perímetro: ", salida[2], "cm")

if __name__ == "__main__":
    main()

