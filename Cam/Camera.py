import picamera
import time

class Camera:

    def __init__(self, data_collector, dir_to_store_images: str):
        if dir_to_store_images[-1] == "/":   
            self.__dir_to_store = dir_to_store_images[:-1]
        else:
            self.__dir_to_store = dir_to_store_images

    def get_store_path(self):
        return self.__dir_to_store

    def __get_img_name(self) -> str:
        '''
        not implemented yet
        '''
        pass

    def take_photo(self):
        with picamera.PiCamera() as picam:
            picam.start_preview()
            time.sleep(5) #Esperamos 5 segundos para que la camara este disponible
            #(Seguramente se puede mejorar)
            picam.capture(self.__dir_to_store + "/" + self.__get_img_name())

    def real_time_preview(self):
        print("Real time preview started, press q to finish")
        char = ""
        with picamera.PiCamera() as picam:
            picam.start_preview()
            while char != "q":
                char = input()
            picam.stop_preview()
            picam.close() #Creo que esto no es necesario ya que el with ejecuta esta funcion al terminar su bloque
