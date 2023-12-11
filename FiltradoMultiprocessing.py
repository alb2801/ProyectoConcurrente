import cv2
import numpy as np
from multiprocessing import Pool

# Función para aplicar el filtro en una sección de la imagen
def apply_filter(img_section, filter_type):
    if filter_type == 'class1':
        kernel = np.array([[0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, -1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
    elif filter_type == 'class2':
        kernel = np.array([[0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, -2, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0]])
    elif filter_type == 'class3':
        kernel = np.array([[0, 0, -1, 0, 0],
                           [0, 0, 3, 0, 0],
                           [0, 0, -3, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0]])
    elif filter_type == 'square3x3':
        kernel = np.array([[0, 0, 0, 0, 0],
                           [0, -1, 2, -1, 0],
                           [0, 2, -4, 2, 0],
                           [0, -1, 2, -1, 0],
                           [0, 0, 0, 0, 0]])
    elif filter_type == 'edge3x3':
        kernel = np.array([[0, 0, 0, 0, 0],
                           [0, -1, 2, -1, 0],
                           [0, 2, -4, 2, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
    elif filter_type == 'square5x5':
        kernel = np.array([[-1, 2, -2, 2, -1],
                           [2, -6, 8, -6, 2],
                           [-2, 8, -12, 8, -2],
                           [2, -6, 8, -6, 2],
                           [-1, 2, -2, 2, -1]])
    elif filter_type == 'edge5x5':
        kernel = np.array([[-1, 2, -2, 2, -1],
                           [2, -6, 8, -6, 2],
                           [-2, 8, -12, 8, -2],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
    elif filter_type == 'sobel_vertical':
        kernel = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
    elif filter_type == 'sobel_horizontal':
        kernel = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])
    elif filter_type == 'laplace':
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
    elif filter_type == 'prewitt_v':
        kernel = np.array([[-1, 0, 1],
                           [-1, 0, 1],
                           [-1, 0, 1]])
    elif filter_type == 'prewitt_h':
        kernel = np.array([[-1, -1, -1],
                              [0, 0, 0],
                              [1, 1, 1]])
    else:
        raise ValueError("Tipo de filtro no válido")

    filtered_section = cv2.filter2D(img_section, -1, kernel)
    return filtered_section

def main():
    # Cargar la imagen
    image_path = 'messi.jpg'  # Reemplaza con la ruta de tu imagen
    img = cv2.imread(image_path)

    # Verificar si la imagen se cargó correctamente
    if img is not None:
        # Dividir la imagen en secciones para el multiprocesamiento
        sections = np.array_split(img, 4)  # Dividir en 4 secciones, puedes ajustar esto según el número de núcleos de tu CPU

        # Iniciar el pool de procesos
        with Pool(2) as pool:
            # Aplicar el filtro en paralelo a cada sección de la imagen
            # Puedes cambiar el tipo de filtro aquí ('custom', 'sobel_vertical', 'sobel_horizontal')
            results = pool.starmap(apply_filter, [(section, 'laplace') for section in sections])

        # Combinar los resultados en una sola imagen
        filtered_img = np.vstack(results)

        # Descarga imagen filtrada
        cv2.imwrite('imagen_filtrada.jpg', filtered_img)

        # Mostrar la imagen original
        cv2.imshow('Imagen Original', img)

        # Mostrar la imagen filtrada
        cv2.imshow('Imagen Filtrada', filtered_img)
        cv2.waitKey(0)  # Esperar hasta que se presione una tecla
        cv2.destroyAllWindows()  # Cerrar las ventanas después de presionar una tecla

        # Mostrar las dimensiones de la imagen filtrada
        print(f"Dimensiones de la imagen filtrada: {filtered_img.shape}")

        # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
        min_val = np.min(filtered_img)
        max_val = np.max(filtered_img)
        mean_val = np.mean(filtered_img)
        std_dev = np.std(filtered_img)

        print(f"Valor mínimo de los píxeles: {min_val}")
        print(f"Valor máximo de los píxeles: {max_val}")
        print(f"Valor medio de los píxeles: {mean_val}")
        print(f"Desviación estándar de los píxeles: {std_dev}")

    else:
        print("No se pudo cargar la imagen. Verifica la ruta y el formato de la imagen.")

if __name__ == '__main__':
    main()
