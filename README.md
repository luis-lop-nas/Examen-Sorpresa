# Examen-Sorpresa

https://github.com/luis-lop-nas/Examen-Sorpresa.git



Este proyecto implementa una serie de clases y funciones en Python para trabajar con puntos en un plano cartesiano y rectángulos definidos por dos puntos. A continuación, se detalla la funcionalidad del código.

---

## Clases

### Clase `Punto`
La clase `Punto` representa un punto en un plano cartesiano con coordenadas `x` e `y`. Incluye métodos para calcular el cuadrante, vectores, y distancias entre puntos.

#### Métodos:
1. **`__init__(self, x=0, y=0)`**:
   - Constructor que inicializa las coordenadas del punto.
   - Si no se proporcionan valores, las coordenadas por defecto son `(0, 0)`.

2. **`__str__(self)`**:
   - Devuelve una representación en texto del punto en el formato `(x, y)`.

3. **`cuadrante(self)`**:
   - Determina en qué cuadrante del plano cartesiano se encuentra el punto:
     - Primer cuadrante: `x > 0` y `y > 0`.
     - Segundo cuadrante: `x < 0` y `y > 0`.
     - Tercer cuadrante: `x < 0` y `y < 0`.
     - Cuarto cuadrante: `x > 0` y `y < 0`.
     - Sobre los ejes o en el origen.

4. **`vector(self, otro_punto)`**:
   - Calcula el vector entre el punto actual y otro punto.

5. **`distancia(self, otro_punto)`**:
   - Calcula la distancia euclidiana entre el punto actual y otro punto.

---

### Clase `Rectangulo`
La clase `Rectangulo` representa un rectángulo definido por dos puntos que forman su diagonal. Incluye métodos para calcular la base, altura, área y perímetro.

#### Métodos:
1. **`__init__(self, punto_inicial, punto_final)`**:
   - Constructor que inicializa el rectángulo con dos puntos (`punto_inicial` y `punto_final`).

2. **`calcular_base(self)`**:
   - Calcula la base del rectángulo como la diferencia absoluta entre las coordenadas `x` de los puntos.

3. **`calcular_altura(self)`**:
   - Calcula la altura del rectángulo como la diferencia absoluta entre las coordenadas `y` de los puntos.

4. **`calcular_area(self, base, altura)`**:
   - Calcula el área del rectángulo como `base * altura`.

5. **`calcular_perimetro(self)`**:
   - Calcula el perímetro del rectángulo como `2 * (base + altura)`.

6. **`__str__(self)`**:
   - Devuelve una representación en texto del rectángulo, indicando los puntos que lo definen.

---

## Funciones

### `crear_puntos()`
- Solicita al usuario las coordenadas de cuatro puntos (`A`, `B`, `C`, `D`) y los crea como instancias de la clase `Punto`.

### `imprimir_puntos(A, B, C, D)`
- Imprime las coordenadas de los puntos `A`, `B`, `C` y `D`.

### `consultar_cuadrante(A, C, D)`
- Determina y muestra en qué cuadrante se encuentran los puntos `A`, `C` y `D`.

### `consultar_vectores(A, B)`
- Calcula y muestra los vectores `AB` y `BA`.

### `consultar_distancias(A, B, C, D)`
- Calcula las distancias de los puntos `A`, `B` y `C` al punto `D`.
- Determina cuál de los puntos está más lejos del origen `(0, 0)`.

### `crear_rectangulo(A, B)`
- Crea un rectángulo utilizando los puntos `A` y `B` como la diagonal.
- Calcula y muestra la base, altura, área y perímetro del rectángulo.

---

## Ejecución del Código

1. **Crear puntos**:
   - Llama a la función `crear_puntos()` para ingresar las coordenadas de los puntos.

2. **Imprimir puntos**:
   - Usa la función `imprimir_puntos()` para mostrar las coordenadas de los puntos creados.

3. **Consultar cuadrantes**:
   - Llama a la función `consultar_cuadrante()` para determinar en qué cuadrante se encuentran los puntos.

4. **Consultar vectores**:
   - Usa la función `consultar_vectores()` para calcular los vectores entre dos puntos.

5. **Consultar distancias**:
   - Llama a la función `consultar_distancias()` para calcular las distancias entre los puntos y determinar cuál está más lejos del origen.

6. **Crear rectángulo**:
   - Usa la función `crear_rectangulo()` para crear un rectángulo con dos puntos y calcular sus propiedades.

---

## Ejemplo de Salida




