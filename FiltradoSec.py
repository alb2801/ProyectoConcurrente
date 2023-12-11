import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('cebra.jpg', cv2.IMREAD_GRAYSCALE)

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

    plt.show()


Class1(imagen)
