import cv2 #procesar imágenes y videos
import os #modulo para usar funciones dependientes del sistema operativo

rutaVideo = os.path.join("video", "video.mp4") #la ruta del video con el nombre del video a convertir
captura = cv2.VideoCapture(rutaVideo) #captura el video 

if not captura.isOpened(): #si no se puede habrir o encontrar el video
    print("No se puede habrir el video o no existe")
    exit() #sale del programa

carpetaSalida="Frame"
os.makedirs(carpetaSalida, exist_ok=True) #Se crea una carpeta

