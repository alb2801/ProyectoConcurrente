import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_filter_Sec(pathImagen, filtro):
    imagen = cv2.imread(pathImagen, cv2.IMREAD_GRAYSCALE)
    if filtro == "Class 1":
        time.sleep(np.random.randint(1, 4))
        Class1(imagen)
    elif filtro == "Class 2":
        time.sleep(np.random.randint(1, 4))
        Class2(imagen)
    elif filtro == "Class 3":
        time.sleep(np.random.randint(1, 4))
        Class3(imagen)
    elif filtro == "Square 3x3":
        time.sleep(np.random.randint(1, 4))
        Square3x3(imagen)
    elif filtro == "Edge 3x3":
        time.sleep(np.random.randint(1, 4))
        Edge3x3(imagen)
    elif filtro == "Square 5x5":
        time.sleep(np.random.randint(1, 4))
        Square5x5(imagen)
    elif filtro == "Edge 5x5":
        time.sleep(np.random.randint(1, 4))
        Edge5x5(imagen)
    elif filtro == "Sobel":
        time.sleep(np.random.randint(1, 4))
        Sobel_x_y(imagen)
    elif filtro == "Laplace":
        time.sleep(np.random.randint(1, 4))
        Laplace(imagen)
    elif filtro == "Prewitt":
        time.sleep(np.random.randint(1, 4))
        Prewitt(imagen)
    else:
        raise ValueError("Tipo de filtro no válido")
    
def Sobel_x_y(imagen):
    # Definir los kernels de Sobel
    kernel_sobel_vertical = np.array([[0, 0, 0, 0, 0],
                                    [0, -1, 0, 1, 0],
                                    [0, -2, 0, 2, 0],
                                    [0, -1, 0, 1, 0],
                                    [0, 0, 0, 0, 0]])

    kernel_sobel_horizontal = np.array([[0, 0, 0, 0, 0],
                                        [0, -1, -2, -1, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 1, 2, 1, 0],
                                        [0, 0, 0, 0, 0]])

    # Aplicar los filtros
    filtro_vertical = cv2.filter2D(imagen, -1, kernel_sobel_vertical)
    filtro_horizontal = cv2.filter2D(imagen, -1, kernel_sobel_horizontal)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 3, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(filtro_vertical, cmap='gray')
    plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(filtro_horizontal, cmap='gray')
    plt.title('Sobel Horizontal'), plt.xticks([]), plt.yticks([])
    
    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_vertical.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_vertical)
    max_val = np.max(filtro_vertical)
    mean_val = np.mean(filtro_vertical)
    std_dev = np.std(filtro_vertical)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    print(f"Dimensiones de la imagen filtrada en horizontal: {filtro_horizontal.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val2 = np.min(filtro_horizontal)
    max_val2 = np.max(filtro_horizontal)
    mean_val2 = np.mean(filtro_horizontal)
    std_dev2 = np.std(filtro_horizontal)

    print(f"Valor mínimo de los píxeles: {min_val2}")
    print(f"Valor máximo de los píxeles: {max_val2}")
    print(f"Valor medio de los píxeles: {mean_val2}")
    print(f"Desviación estándar de los píxeles: {std_dev2}")

    plt.show()


def Class1(imagen):
    # Definir el kernel
    kernel = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, -1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Class1'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()


def Class2(imagen):
    # Definir el kernel
    kernel = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, -2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Class2'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Class3(imagen):
    # Definir el kernel
    kernel = np.array([[0, 0, -1, 0, 0],
                    [0, 0, 3, 0, 0],
                    [0, 0, -3, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Class3'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Square3x3(imagen):
    # Definir el kernel
    kernel = np.array([[0, 0, 0, 0, 0],
                    [0, -1, 2, -1, 0],
                    [0, 2, -4, 2, 0],
                    [0, -1, 2, -1, 0],
                    [0, 0, 0, 0, 0]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Square3x3'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Edge3x3(imagen):
    # Definir el kernel
    kernel = np.array([[0, 0, 0, 0, 0],
                    [0, -1, 2, -1, 0],
                    [0, 2, -4, 2, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Edge3x3'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Square5x5(imagen):
    # Definir el kernel (filtro Square5x5)
    kernel = np.array([[-1, 2, -2, 2, -1],
                    [2, -6, 8, -6, 2],
                    [-2, 8, -12, 8, -2],
                    [2, -6, 8, -6, 2],
                    [-1, 2, -2, 2, -1]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Square5x5'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Edge5x5(imagen):
    # Definir el kernel (filtro Edge5x5)
    kernel = np.array([[-1, 2, -2, 2, -1],
                    [2, -6, 8, -6, 2],
                    [-2, 8, -12, 8, -2],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Edge5x5'), plt.xticks([]), plt.yticks([])
    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Laplace(imagen):
    # Definir el kernel (filtro Laplace)
    kernel = np.array([[-1, -1, -1],
                    [-1,  8, -1],
                    [-1, -1, -1]])

    # Aplicar el filtro
    filtro_resultado = cv2.filter2D(imagen, -1, kernel)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(filtro_resultado, cmap='gray')
    plt.title('Filtro Laplace'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_resultado.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_resultado)
    max_val = np.max(filtro_resultado)
    mean_val = np.mean(filtro_resultado)
    std_dev = np.std(filtro_resultado)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    plt.show()

def Prewitt(imagen):
    # Definir los kernels de Prewitt
    kernel_prewitt_vertical = np.array([[-1, 0, 1],
                                        [-1, 0, 1],
                                        [-1, 0, 1]])

    kernel_prewitt_horizontal = np.array([[-1, -1, -1],
                                        [0, 0, 0],
                                        [1, 1, 1]])

    # Aplicar los filtros
    filtro_vertical = cv2.filter2D(imagen, -1, kernel_prewitt_vertical)
    filtro_horizontal = cv2.filter2D(imagen, -1, kernel_prewitt_horizontal)

    # Mostrar las imágenes resultantes
    plt.subplot(1, 3, 1), plt.imshow(imagen, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(filtro_vertical, cmap='gray')
    plt.title('Prewitt Vertical'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(filtro_horizontal, cmap='gray')
    plt.title('Prewitt Horizontal'), plt.xticks([]), plt.yticks([])

    print(f"Dimensiones de la imagen filtrada en vertical: {filtro_vertical.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtro_vertical)
    max_val = np.max(filtro_vertical)
    mean_val = np.mean(filtro_vertical)
    std_dev = np.std(filtro_vertical)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    print(f"Dimensiones de la imagen filtrada en horizontal: {filtro_horizontal.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val2 = np.min(filtro_horizontal)
    max_val2 = np.max(filtro_horizontal)
    mean_val2 = np.mean(filtro_horizontal)
    std_dev2 = np.std(filtro_horizontal)

    print(f"Valor mínimo de los píxeles: {min_val2}")
    print(f"Valor máximo de los píxeles: {max_val2}")
    print(f"Valor medio de los píxeles: {mean_val2}")
    print(f"Desviación estándar de los píxeles: {std_dev2}")

    plt.show()
