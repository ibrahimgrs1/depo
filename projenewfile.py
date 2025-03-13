import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta

def get_user_location():
    locator = Nominatim(user_agent="deprem.uggulaması")

    name_of_city = input("Bulunduğunuz şehrin adını giriniz: ")

    # Türkçe karakterler ile ilgili sorun yaşamamak için şehir ismini düzgün şekilde encode edelim
    name_of_city = name_of_city.encode('utf-8').decode('utf-8')

    try:
        location = locator.geocode(name_of_city, timeout=10)

        if location:
            return location.latitude, location.longitude
        else:
            print("Konum bulunamadı")
            return None
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

def get_afad_earthquakes():
    base_url = "https://deprem.afad.gov.tr/apiv2/event/filter"

    # Bugünün tarihi ve 7 gün önceki tarih
    end_date = datetime.now().strftime("%Y-%m-%d")
