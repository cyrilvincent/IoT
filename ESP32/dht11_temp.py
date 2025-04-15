import machine
import time
import dht

capteur = dht.DHT11(machine.Pin(18))

while True:
    try:
        time.sleep(1)
        # Le DHT11 renvoie au maximum une mesure toute les 1s
        capteur.measure()
        # Récupère les mesures du capteur
        print(f"Temp: {capteur.temperature():.1f}")
        print(f"Humidity: {capteur.humidity():.1f}")
        # Transmet la température sur la console de l'ordinateur
    except Exception as e: # gestion des erreurs obligatoires car il peut être plus lent que 1s
        print('Echec reception', e)