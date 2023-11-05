import cv2 #procesar imágenes y videos
import os #modulo para usar funciones dependientes del sistema operativo

def convertirVideoAImagen(carpetaSalida,video):  

    rutaVideo = os.path.join("video", video) #la ruta del video con el nombre del video a convertir
    captura = cv2.VideoCapture(rutaVideo) #captura el video por medio de la ruta dada
    
    if not captura.isOpened(): #si no se puede habrir o encontrar el video
        print("No se puede habrir el video o no existe")
        return #sale del programa
    else:
       print("si existe")

    os.makedirs(carpetaSalida, exist_ok=True) #Se crea una carpeta con el nombre que se trae en el metodo

    cont=0
    while True:

        bandera, frame=captura.read() #leer el video

        if not bandera: #si la bandera es falso es porque no hay mas frame ya que no se puede leer el video
            break

        nombreFrame=f"{carpetaSalida}/frame_{cont:04d}.jpg" #guarda la ruta y nombre de la imagen
        cv2.imwrite(nombreFrame, frame) #guarda la imagen donde sele indica la ruta

        cont+=1

    captura.release() #liberar los objetos que hay en captura (captura queda vacio)
   




archivos = os.listdir("video") #guardar todos los archivos de la carpeta video
print(archivos)

i=0
for archivo in archivos:
   if archivo.endswith(".mp4"): #si termina en .mp4
    print(archivo)
    nombreSinExtension, extension = os.path.splitext(archivo) #separe el nombre del archivo de la extension
    carpetaSalida=nombreSinExtension+"_"+str(i) #nombre de la carpeta donde se guardaran las imgs
    print(carpetaSalida)
    convertirVideoAImagen(carpetaSalida,archivo)
    i+=1
    