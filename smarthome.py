from philipstv import PhilipsTVRemote
from dotenv import load_dotenv
import time
import os

load_dotenv("Config.env")

IP = os.getenv("TV_IP")
CLIENT_ID = os.getenv("TV_CLIENT_ID")
TOKEN = os.getenv("TV_TOKEN")

active_Message = "in benutzung"
inactive_Message = "nicht in benutzung"

def pair_tv():
    try:
        # Erstellt Variable für den neuen TV
        tv = PhilipsTVRemote.new(IP)
            
        # 10 Sekunden warten
        #print("Pairing startet in 10 Sekunden")
        #time.sleep(10)

        # Versucht sich zu connecten
        credentials = tv.pair(pin)

        # print("Gespeichert:")
        print("ID:", credentials[0])
        print("TOKEN:", credentials[1])

    except Exception as e:
        print("Error:",e)


def pin():
    return input("PIN vom TV: ")


def connect_tv():
    try:
        # Verbindet sich via IP Client und Token
        return PhilipsTVRemote.new(IP,auth=(CLIENT_ID, TOKEN))
    except Exception as e:
        print(f"ERROR: ",e)


def power_off():
    try:
        tv = connect_tv()
        tv.set_power(False)
        print("TV ausgeschaltet")
    
    except Exception as e:
        print(f"Fehler: {e}")


def power_on():
    try:
        tv = connect_tv()
        tv.set_power(True)
        print("TV eingeschaltet")
    except Exception as e:
         print(f"Fehler: {e}")


def getCurrentPower():
    try: 
        tv = connect_tv()
        isInUse = tv.get_power()
        if isInUse:
            print(f"Status: {active_Message} (Info: {isInUse})")
        elif isInUse != True:
            print(f"Status: {inactive_Message} (Info: {isInUse})")

    except Exception as e:
        print("Fehler",e)


def switchPower():
    try: 
        tv = connect_tv()
        if tv.get_power() == True:
            tv.set_power(False)
            return
        tv.set_power(True)

    except Exception as e:
        print(f"Fehler",e)


getCurrentPower()