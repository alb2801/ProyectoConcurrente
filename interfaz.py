# interfaz.py

import streamlit as st
from DescargarIma import download_images

def main():
    st.title("Proyecto Concurrente")

    # Ingresar un tema
    tema = st.text_input("Ingrese el tema:")

    # Botón para ejecutar la descarga y duplicación de imágenes
    if st.button("Descargar imagenes"):
        download_images(tema)
        st.success("Descargas de imagenes completadas.")

    # Selección en lista desplegable para el tipo de paralelismo
    tipo_paralelismo = st.selectbox("Seleccione el tipo de paralelismo:",
                                    ["C", "OpenMP", "Multiprocessing", "MPI4PY"])

    # Configuración según el tipo de paralelismo
    if tipo_paralelismo == "C" or tipo_paralelismo == "OpenMP":
        # Cantidad de hilos (max 10)
        num_hilos = st.slider("Seleccione la cantidad de hilos:", 1, 10, 1)
    elif tipo_paralelismo == "Multiprocessing" or tipo_paralelismo == "MPI4PY":
        # Cantidad de procesos (max 10)
        num_procesos = st.slider("Seleccione la cantidad de procesos:", 1, 10, 1)

    # Lista desplegable con 10 items
    lista_items = st.selectbox("Seleccione un ítem de la lista:", ["Class 1","Class 2","Class 3",
                                                                   "Square 3x3","Edge 3x3","Square 5x5",
                                                                   "Edge 5x5","Sobel vertical y horizontalmente",
                                                                   "Laplace","Prewitt vertical y horizontal"])

    # Mostrar la configuración seleccionada
    st.text(f"Tipo de paralelismo: {tipo_paralelismo}")

    if tipo_paralelismo == "C" or tipo_paralelismo == "OpenMP":
        st.text(f"Cantidad de hilos: {num_hilos}")
    elif tipo_paralelismo == "Multiprocessing" or tipo_paralelismo == "MPI4PY":
        st.text(f"Cantidad de procesos: {num_procesos}")

    st.text(f"Ítem seleccionado: {lista_items}")


if __name__ == "__main__":
    main()
