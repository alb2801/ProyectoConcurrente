import numpy as np
import streamlit as st
from DescargarIma import download_images
from FiltradoMPI4PY import apply_filter
from FiltradoMultiprocessing import apply_filter_multi
from FiltradoSec import apply_filter_Sec
import os
import random
import time
from PIL import Image
import matplotlib.pyplot as plt

def select_random_images():
    image_folder = "imagenes"
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    random_images = random.sample(images, 10)
    return [os.path.join(image_folder, img) for img in random_images]

def main():
    st.title("Proyecto Concurrente")

    # Ingresar un tema
    tema = st.text_input("Ingrese el tema:")

    # Botón para ejecutar la descarga y duplicación de imágenes
    if st.button("Descargar imágenes"):
        download_images(tema)
        st.success("Descargas de imágenes completadas.")

    # Selección en lista desplegable para el tipo de paralelismo
    tipo_paralelismo = st.selectbox("Seleccione el tipo de paralelismo:",
                                    ["Multiprocessing", "MPI4PY"])

    if tipo_paralelismo == "Multiprocessing" or tipo_paralelismo == "MPI4PY":
        # Cantidad de procesos (max 10)
        num_procesos = st.slider("Seleccione la cantidad de procesos:", 1, 10, 1)

    # Lista desplegable con 10 items
    lista_filtros = st.selectbox("Seleccione el filtro a aplicar:", ["Class 1", "Class 2", "Class 3",
                                                                   "Square 3x3", "Edge 3x3", "Square 5x5",
                                                                   "Edge 5x5", "Sobel", "Laplace", "Prewitt"])

    if st.button("Aplicar filtro"):
        if tipo_paralelismo  == "MPI4PY":
            random_images = select_random_images()
            
            inicio_paralelo = time.time()

            for img_path in random_images:
                img = Image.open(img_path)

                # Crear dos columnas para mostrar las imágenes
                col1, col2 = st.columns(2)

                # Mostrar la imagen original a la izquierda
                col1.image(img, caption='Imagen Original', use_column_width=True)

                filtered_image = apply_filter(num_procesos, lista_filtros, img_path)

                # Mostrar la imagen filtrada a la derecha
                col2.image(filtered_image, caption='Imagen Filtrada', use_column_width=True, channels='GRAY')

                # Mostrar estadísticas
                col2.write(f"Valor mínimo de los píxeles: {np.min(filtered_image)}")
                col2.write(f"Valor máximo de los píxeles: {np.max(filtered_image)}")
                col2.write(f"Valor medio de los píxeles: {np.mean(filtered_image)}")
                col2.write(f"Desviación estándar de los píxeles: {np.std(filtered_image)}")

            fin_paralelo = time.time()

            inicio_secu = time.time()
            for img_path in random_images:
                img = Image.open(img_path)

                filtered_image = apply_filter_Sec(img_path, lista_filtros)

            fin_secu = time.time()

            # Calcular tiempos y aceleración
            duration_serial = fin_secu - inicio_secu
            duration_parallel = fin_paralelo - inicio_paralelo
            acceleration = duration_serial / duration_parallel if duration_parallel > 0 else 0

            col1, col2 = st.columns(2)
            # Mostrar resultados
            col1.write(f"Tiempo en serie: {duration_serial} segundos")
            col1.write(f"Tiempo en paralelo: {duration_parallel} segundos")
            col1.write(f"Aceleración: {acceleration}")

            # Crear gráfico de barras para comparar tiempos
            fig, ax = plt.subplots()
            ax.bar(['Serial', 'Paralelo'], [duration_serial, duration_parallel], color=['blue', 'orange'])
            ax.set_ylabel('Tiempo (segundos)')
            ax.set_title('Comparación de Tiempos en Serie y Paralelo')

            col2.pyplot(plt)

                
        elif tipo_paralelismo == "Multiprocessing":
            random_images = select_random_images()
            inicio_paralelo = time.time()
            for contador, img_path in enumerate(random_images, start=1):
                img = Image.open(img_path)

                col1, col2 = st.columns(2)
                col1.image(img, caption='Imagen Original', use_column_width=True)

                filtered_image_path = apply_filter_multi(num_procesos, lista_filtros, img_path, contador)
                filtered_image = Image.open(filtered_image_path)

                col2.image(filtered_image, caption='Imagen Filtrada', use_column_width=True, channels='GRAY')

                col2.write(f"Valor mínimo de los píxeles: {np.min(filtered_image)}")
                col2.write(f"Valor máximo de los píxeles: {np.max(filtered_image)}")
                col2.write(f"Valor medio de los píxeles: {np.mean(filtered_image)}")
                col2.write(f"Desviación estándar de los píxeles: {np.std(filtered_image)}")
            fin_paralelo = time.time()

            inicio_secu = time.time()
            for img_path in random_images:
                img = Image.open(img_path)

                filtered_image = apply_filter_Sec(img_path, lista_filtros)
            fin_secu = time.time()

            # Calcular tiempos y aceleración
            duration_serial = fin_secu - inicio_secu
            duration_parallel = fin_paralelo - inicio_paralelo
            acceleration = duration_serial / duration_parallel if duration_parallel > 0 else 0

            col1, col2 = st.columns(2)
            # Mostrar resultados
            col1.write(f"Tiempo en serie: {duration_serial} segundos")
            col1.write(f"Tiempo en paralelo: {duration_parallel} segundos")
            col1.write(f"Aceleración: {acceleration}")

            # Crear gráfico de barras para comparar tiempos
            fig, ax = plt.subplots()
            ax.bar(['Serial', 'Paralelo'], [duration_serial, duration_parallel], color=['blue', 'orange'])
            ax.set_ylabel('Tiempo (segundos)')
            ax.set_title('Comparación de Tiempos en Serie y Paralelo')

            col2.pyplot(plt)


if __name__ == "__main__":
    main()
