import numpy as np
import streamlit as st
from DescargarIma import download_images
from FiltradoMPI4PY import apply_filter
import os
import random
from PIL import Image

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
    lista_items = st.selectbox("Seleccione el filtro a aplicar:", ["Class 1", "Class 2", "Class 3",
                                                                   "Square 3x3", "Edge 3x3", "Square 5x5",
                                                                   "Edge 5x5", "Sobel", "Laplace", "Prewitt"])

    if st.button("Aplicar filtro"):
        random_images = select_random_images()
        for img_path in random_images:
            img = Image.open(img_path)

            # Crear dos columnas para mostrar las imágenes
            col1, col2 = st.columns(2)

            # Mostrar la imagen original a la izquierda
            col1.image(img, caption='Imagen Original', use_column_width=True)

            filtered_image = apply_filter(num_procesos, lista_items, img_path)

            # Mostrar estadísticas
            col2.write(f"Valor mínimo de los píxeles: {np.min(filtered_image)}")
            col2.write(f"Valor máximo de los píxeles: {np.max(filtered_image)}")
            col2.write(f"Valor medio de los píxeles: {np.mean(filtered_image)}")
            col2.write(f"Desviación estándar de los píxeles: {np.std(filtered_image)}")

            # Mostrar la imagen filtrada a la derecha
            col2.image(filtered_image, caption='Imagen Filtrada', use_column_width=True, channels='GRAY')

if __name__ == "__main__":
    main()
