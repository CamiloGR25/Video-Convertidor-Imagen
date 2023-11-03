import cv2 #procesar imágenes y videos
import os #modulo para usar funciones dependientes del sistema operativo

rutaVideo = os.path.join("video", "video.mp4") #la ruta del video con el nombre del video a convertir
captura = cv2.VideoCapture(rutaVideo) #captura el video 

if not captura.isOpened(): #si no se puede habrir o encontrar el video
    print("No se puede habrir el video o no existe")
    exit() #sale del programa

carpetaSalida="Frame"
os.makedirs(carpetaSalida, exist_ok=True) #Se crea una carpeta

cont=0
while True:

    bandera, frame=captura.read() #leer el video

    if not bandera: #si la bandera es falso es porque no hay mas frame ya que no se puede leer el video
        break

    nombreFrame=f"{carpetaSalida}/frame_{cont:04d}.jpg" #guarda la ruta y nombre de la imagen
    cv2.imwrite(nombreFrame, frame) #guarda la imagen donde sele indica la ruta

    cont+=1

