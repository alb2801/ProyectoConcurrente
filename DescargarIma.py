import os
import threading
from google_images_search import GoogleImagesSearch
from urllib.parse import urlparse

# Configuración de la API de Google Images Search
google_search_cx = 'xxxxxx'  # Reemplaza 'tu_cx' con tu propio cx
google_search_api_key = 'xxxxxxxxxxx'  # Reemplaza 'tu_api_key' con tu propia clave API

# Configuración del tema de búsqueda
search_query = 'Bikes'

# Configuración del número total de imágenes y el número de hilos
total_images = 100
threads_count = 10

# Calcular el número de imágenes por hilo
images_per_thread = total_images // threads_count

# Directorio de destino para las imágenes descargadas
output_directory = 'imagenes'
os.makedirs(output_directory, exist_ok=True)

# Lock para evitar conflictos en el acceso al sistema de archivos
file_lock = threading.Lock()

def download_images(start_index, end_index):
    gis = GoogleImagesSearch(google_search_api_key, google_search_cx)

    for i in range(start_index, end_index):
        try:
            search_params = {
                'q': search_query,
                'num': images_per_thread,
                'start': i + 1
            }

            gis.search(search_params)
            results = gis.results()

            if results:
                image_url = results[0].url
                image_filename = f"imagen_{i + 1}.jpg"
                if urlparse(image_url).path:
                    image_filename = os.path.basename(urlparse(image_url).path)

                image_path = os.path.join(output_directory, image_filename)

                # Bloquear acceso al sistema de archivos antes de descargar
                with file_lock:
                    gis.download(image_url, path_to_dir=output_directory)

                # Renombrar después de la descarga
                new_image_path = os.path.join(output_directory, f"imagen_{i + 1}.jpg")

                # Bloquear acceso al sistema de archivos antes de renombrar
                with file_lock:
                    os.rename(image_path, new_image_path)

                print(f"Imagen {i + 1} descargada como {new_image_path}")
            else:
                print(f"No hay resultados para la búsqueda en la página {i + 1}")

        except Exception as e:
            print(f"Error al descargar la imagen {i + 1}: {str(e)}")

# Crear y ejecutar los hilos
threads = []
for i in range(threads_count):
    start_index = i * images_per_thread
    end_index = start_index + images_per_thread
    thread = threading.Thread(target=download_images, args=(start_index, end_index))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos finalicen
for thread in threads:
    thread.join()

print("Descarga de imágenes completada.")
