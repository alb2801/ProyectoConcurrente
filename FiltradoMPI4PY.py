import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

filter_type='laplace'
# Inicializar MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Cargar la imagen desde la web (reemplaza 'URL_de_tu_imagen.jpg' con la URL de tu imagen)
image_url = 'messi.jpg'
image = cv2.imread(image_url)

# Dividir la imagen en partes iguales entre los procesos
rows_per_process = image.shape[0] // size
start_row = rank * rows_per_process
end_row = (rank + 1) * rows_per_process if rank != size - 1 else image.shape[0]

# Seleccionar la porción de la imagen para este proceso
local_image = image[start_row:end_row, :]

#Definir el kernel
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

# Convertir la porción de la imagen a escala de grises
local_gray_image = cv2.cvtColor(local_image, cv2.COLOR_BGR2GRAY)

# Aplicar el filtro convolucional localmente
local_filtered_image = cv2.filter2D(local_gray_image, -1, kernel)

# Recopilar todas las porciones filtradas
filtered_images = comm.gather(local_filtered_image, root=0)

# El proceso 0 muestra las imágenes
if rank == 0:
    # Combinar las imágenes filtradas
    filtered_image = np.vstack(filtered_images)

    # Mostrar las dimensiones de la imagen filtrada
    print(f"Dimensiones de la imagen filtrada: {filtered_image.shape}")

    # Obtener valor mínimo, máximo, medio y desviación estándar de los píxeles
    min_val = np.min(filtered_image)
    max_val = np.max(filtered_image)
    mean_val = np.mean(filtered_image)
    std_dev = np.std(filtered_image)

    print(f"Valor mínimo de los píxeles: {min_val}")
    print(f"Valor máximo de los píxeles: {max_val}")
    print(f"Valor medio de los píxeles: {mean_val}")
    print(f"Desviación estándar de los píxeles: {std_dev}")

    # Mostrar la imagen original y la imagen filtrada
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Imagen Original')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Imagen Filtrada')
    plt.imshow(filtered_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
