import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta

def get_user_location():
    locator = Nominatim(user_agent="deprem.uggulaması")

    name_of_city = input("Bulunduğunuz şehrin adını giriniz: ")

    # Türkçe karakterler ile ilgili sorun yaşamamak için şehir ismini düzgün şekilde encode edelim
    name_of_city = name_of_city.encode('utf-8').decode('utf-8')

    location = locator.geocode(name_of_city, timeout=10)

    if location:
        return location.latitude, location.longitude
    else:
        print("Konum bulunamadı")
        return None

def get_afad_earthquakes():
    base_url = "https://deprem.afad.gov.tr/apiv2/event/filter"

    # Bugünün tarihi ve 7 gün önceki tarih
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    params = {
        "start": start_date,  # Başlangıç tarihi
        "end": end_date,      # Bitiş tarihi
        "limit": 100          # En fazla 100 deprem al
    }

    response = requests.get(base_url, params=params)

    print("HTTP Yanıt Kodu:", response.status_code)
    print("Yanıt İçeriği (İlk 500 karakter):", response.text[:500])

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except requests.exceptions.JSONDecodeError:
            print("JSON formatına çevrilemedi! API yanıtı beklenen formatta değil.")
            return None
    else:
        print("AFAD'dan veri alınamadı.")
        return None

# Kullanıcıdan şehir bilgisi al
latitude, longitude = get_user_location()
if latitude and longitude:
    print("Latitude:", latitude, "Longitude:", longitude)

    # AFAD'dan deprem verilerini al
    earthquake_data = get_afad_earthquakes()

    if earthquake_data:
        print("Son 5 deprem:")
        for quake in earthquake_data["result"][:5]:  # İlk 5 depremi yazdır
            print(quake)
    else:
        print("Deprem verisi bulunamadı.")
