import network   #import des fonction lier au wifi
import urequests #import des fonction lier au requetes http
import utime #import des fonction lier au temps
import ujson #import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Heloise'
password = 'petitpied'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://172.20.10.11:3000/dataled/"

maison = {
    "Gryffindor" : [255,0,0],
    "Slytherin" : [0,255,0],
    "Hufflepuff" : [200,200,0],
    "Ravenclaw" : [0,0,255]
}

led =[PWM(Pin(18,mode=Pin.OUT)), PWM(Pin(17,mode=Pin.OUT)),PWM(Pin(16,mode=Pin.OUT))]

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while True:
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        led[0].duty_u16(0)
        led[1].duty_u16(0)
        led[2].duty_u16(0)
        if (r.json()["house"]) == "Gryffindor":
            led[0].duty_u16(13000)
        if (r.json()["house"]) == "Slytherin":
            led[2].duty_u16(13000)
        if (r.json()["house"]) == "Hufflepuff":
            led[1].duty_u16(13000)
            led[0].duty_u16(13000)
        if (r.json()["house"]) == "Ravenclaw":
            led[1].duty_u16(13000)
        r.close() # ferme la demande
        utime.sleep(1)
    except Exception as e:
        print(e)