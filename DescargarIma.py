import os
from google_images_search import GoogleImagesSearch
from urllib.parse import urlparse
import random
import time
from concurrent.futures import ThreadPoolExecutor

def download_and_duplicate_images(tema):
    # Configuración de la API de Google Images Search
    google_search_cx = '632f67be0671c4172'  # Reemplaza 'tu_cx' con tu propio cx
    google_search_api_key = 'AIzaSyBaISwCxV3YqJ3TFKeJopiqxzRt1uhrVmI'  # Reemplaza 'tu_api_key' con tu propia clave API

    # Configuración del tema de búsqueda
    search_query = tema

    # Configuración del número total de imágenes
    total_images = 100

    # Directorio de destino para las imágenes descargadas
    output_directory = 'imagenes'
    os.makedirs(output_directory, exist_ok=True)

    def download_image(index):
        gis = GoogleImagesSearch(google_search_api_key, google_search_cx)

        try:
            search_params = {
                'q': search_query,
                'num': 100,  # Intentaremos obtener 10 resultados y seleccionar uno aleatorio
                'start': index + 1
            }

            gis.search(search_params)
            results = gis.results()

            if results: # Seleccionar un resultado aleatorio
                random_result = random.choice(results) 
                image_url = random_result.url 
                image_filename = f"imagen_{index + 1}.jpg" 
                if urlparse(image_url).path: 
                    image_filename = os.path.basename(urlparse(image_url).path) 
                    image_path = os.path.join(output_directory, image_filename) 
                    gis.download(image_url, path_to_dir=output_directory) 
                    # Renombrar después de la descarga 
                    new_image_path = os.path.join(output_directory, f"imagen_{index + 1}.jpg") 
                    os.rename(image_path, new_image_path) 
                    print(f"Imagen {index + 1} descargada como {new_image_path}") 
            else:
                print(f"No hay resultados para la búsqueda en la página {index + 1}")
        except Exception as e:
            print(f"Error al descargar la imagen {index + 1}: {str(e)}")

    # Duplicar imágenes con 10 hilos
    def duplicate_images(image_path, index):
        for i in range(1, 101):
            duplicate_path = os.path.join(output_directory, f"imagen_{index + 100 * i}.jpg")
            os.system(f"copy {image_path} {duplicate_path}")
            print(f"Imagen duplicada: {duplicate_path}")

    # Descargar imágenes de manera secuencial
    for i in range(total_images):
        download_image(i)

    print("Descarga de imágenes completada.")

    # Duplicar imágenes con 10 hilos
    with ThreadPoolExecutor(max_workers=10) as executor:
        image_paths = [os.path.join(output_directory, f"imagen_{i + 1}.jpg") for i in range(total_images)]
        executor.map(duplicate_images, image_paths, range(total_images))

    print("Duplicación de imágenes completada.")
