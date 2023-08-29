#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
def insertar_arbol_trinario(root, value):
    if not root:
        return [value, [], [], []]

    if value < root[0]:
        root[1] = insertar_arbol_trinario(root[1], value)
    elif value == root[0]:
        root[2] = insertar_arbol_trinario(root[2], value)
    else:
        root[3] = insertar_arbol_trinario(root[3], value)

    return root


def construir_arbol_trinario(numbers):
    root = None
    for num in numbers:
        root = insertar_arbol_trinario(root, num)
    return root


def main():
    t = input()
    numeros = list(map(int, t.split()))

    trinario_tree = construir_arbol_trinario(numeros)

    print(trinario_tree)


if __name__ == '__main__':
    main()
