import requests
import threading
import os
import gzip
from random import randint

def download_image(query, index):
    # Genera un número aleatorio entre 1 y 100
    random_number = randint(1, 100)

    # Crea la URL de la imagen
    url = f"https://www.google.com/search?q={query}&tbm=isch&hl=es&tbs=isz:l,itp:photo&start={random_number}"

    # Descarga la imagen
    response = requests.get(url)

    # Obtiene el nombre de la imagen
    filename = f"image_{index}.jpg"

    # Guarda la imagen en el disco
    with open(filename, "wb") as file:
        file.write(response.content)


def main():
    # Define el tema de las imágenes
    query = "paisajes"

    # Crea los hilos
    threads = []
    for i in range(10):
        thread = threading.Thread(target=download_image, args=(query, i))
        threads.append(thread)

    # Inicia los hilos
    for thread in threads:
        thread.start()

    # Espera a que terminen los hilos
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
