import os
import threading
from google_images_search import GoogleImagesSearch

# Configuración de la API de Google Images Search
google_search_cx = '632f67be0671c4172'  # Reemplaza 'tu_cx' con tu propio cx
google_search_api_key = 'AIzaSyASm9RMn1jLDEStl3FpZasPMySVj7yf0XY'  # Reemplaza 'tu_api_key' con tu propia clave API

# Configuración del tema de búsqueda
search_query = 'Car'

# Configuración del número total de imágenes y el número de hilos
total_images = 100
threads_count = 10

# Calcular el número de imágenes por hilo
images_per_thread = total_images // threads_count

# Directorio de destino para las imágenes descargadas
output_directory = 'imagenes'
os.makedirs(output_directory, exist_ok=True)

def download_images(start_index, end_index):
  gis = GoogleImagesSearch(google_search_api_key, google_search_cx)

  for i in range(start_index, end_index):
    try:
      search_params = {
        'q': search_query,
        'num': images_per_thread,  # Descarga múltiples imágenes por hilo
        'start': i + 1  # Índice de inicio de la página de resultados
      }

      gis.search(search_params)

      # Descarga y guarda la imagen
      image_url = gis.results()[i].url
      gis.download(image_url, path_to_dir=output_directory)
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
