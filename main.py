from lanzador import crear_puntos, imprimir_puntos, consultar_cuadrante, consultar_vectores, consultar_distancias, crear_rectangulo, determinar_punto_mas_lejano

if __name__ == "__main__":
    A, B, C, D = crear_puntos()
    imprimir_puntos(A, B, C, D)
    consultar_cuadrante(A, C, D)
    consultar_vectores(A, B)
    consultar_distancias(A, B, C, D)
    determinar_punto_mas_lejano(A.distancia(D), B.distancia(D), C.distancia(D))
    crear_rectangulo(A, B)
        