# interfaz.py

import streamlit as st
from DescargarIma import download_images
import os
import random
from PIL import Image

def select_random_images():
    image_folder = "imagenes"
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    random_images = random.sample(images, 10)
    return [Image.open(os.path.join(image_folder, img)) for img in random_images]

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

    # Configuración según el tipo de paralelismo
    if tipo_paralelismo == "C" or tipo_paralelismo == "OpenMP":
        # Cantidad de hilos (max 10)
        num_hilos = st.slider("Seleccione la cantidad de hilos:", 1, 10, 1)
    elif tipo_paralelismo == "Multiprocessing" or tipo_paralelismo == "MPI4PY":
        # Cantidad de procesos (max 10)
        num_procesos = st.slider("Seleccione la cantidad de procesos:", 1, 10, 1)

    # Lista desplegable con 10 items
    lista_items = st.selectbox("Seleccione el flitro a aplicar:", ["Class 1","Class 2","Class 3",
                                                                   "Square 3x3","Edge 3x3","Square 5x5",
                                                                   "Edge 5x5","Sobel vertical","Sobel horizontalmente"
                                                                   "Laplace","Prewitt vertical","Prewitt horizontal"])

    if st.button("Mostrar 10 imágenes aleatorias"):
        random_images = select_random_images()
        for img in random_images:
            st.image(img,  width=300) 

if __name__ == "__main__":
    main()
