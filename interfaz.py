import streamlit as st

def main():
    st.title("Configuración de Paralelismo")

    # Ingresar un tema
    tema = st.text_input("Ingrese el tema:")

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
    lista_items = st.selectbox("Seleccione un ítem de la lista:", list(range(1, 11)))

    # Mostrar la configuración seleccionada
    st.text(f"Tema: {tema}")
    st.text(f"Tipo de paralelismo: {tipo_paralelismo}")

    if tipo_paralelismo == "C" or tipo_paralelismo == "OpenMP":
        st.text(f"Cantidad de hilos: {num_hilos}")
    elif tipo_paralelismo == "Multiprocessing" or tipo_paralelismo == "MPI4PY":
        st.text(f"Cantidad de procesos: {num_procesos}")

    st.text(f"Ítem seleccionado: {lista_items}")

if __name__ == "__main__":
    main()
