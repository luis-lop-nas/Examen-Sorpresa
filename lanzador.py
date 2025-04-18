from punto import Punto
from rectangulo import Rectangulo

def crear_puntos():
    # Pedir los valores por terminal
    x1, y1 = map(int, input("Ingrese las coordenadas de A (x y): ").split())
    x2, y2 = map(int, input("Ingrese las coordenadas de B (x y): ").split())
    x3, y3 = map(int, input("Ingrese las coordenadas de C (x y): ").split())
    x4, y4 = map(int, input("Ingrese las coordenadas de D (x y): ").split())
        
    # Crear los puntos
    A = Punto(x1, y1)
    B = Punto(x2, y2)
    C = Punto(x3, y3)
    D = Punto(x4, y4)
        
    return A, B, C, D



def imprimir_puntos(A, B, C, D):
    # Imprimir los puntos
    print("Punto A:", A)
    print("Punto B:", B)
    print("Punto C:", C)
    print("Punto D:", D)

def consultar_cuadrante(A, C, D):
    # Consultar y mostrar el cuadrante de los puntos
    print("El punto A pertenece al:", A.cuadrante())
    print("El punto C pertenece al:", C.cuadrante())
    print("El punto D pertenece al:", D.cuadrante())

def consultar_vectores(A, B):
    # Consultar y mostrar los vectores AB y BA
    print("El vector AB es:", A.vector(B))
    print("El vector BA es:", B.vector(A))

def consultar_distancias(A, B, C, D):
    # Calcular distancias al origen
    distancia_A = A.distancia(D)
    distancia_B = B.distancia(D)
    distancia_C = C.distancia(D)
    print(f"La distancia entre los puntos es: {distancia_A}")
    print(f"La distancia entre los puntos es: {distancia_B}")
    print(f"La distancia entre los puntos es: {distancia_C}")
    # Determinar el punto más lejano
    if distancia_A > distancia_B and distancia_A > distancia_C:
        print("El punto A es el más lejano al origen.")
    elif distancia_B > distancia_A and distancia_B > distancia_C:
        print("El punto B es el más lejano al origen.")
    elif distancia_C > distancia_A and distancia_C > distancia_B:
        print("El punto C es el más lejano al origen.")
    else:
        print("Hay puntos equidistantes del origen.")
def crear_rectangulo(A, B):
    
    rectangulo = Rectangulo(A, B)

    # Imprimir información del rectángulo
    print(rectangulo)
    print("Base del rectángulo:", rectangulo.calcular_base())
    print("Altura del rectángulo:", rectangulo.calcular_altura())
    print("Área del rectángulo:", rectangulo.calcular_area(rectangulo.calcular_base(), rectangulo.calcular_altura()))
    print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())



