import phonenumbers

from phonenumbers import timezone,geocoder,carrier,geodata
#numerotelefone = input('Digite seu numero:')
numero = phonenumbers.parse('+918978923094')
timezone = timezone.time_zones_for_number(numero)
carrier = carrier.name_for_number(numero, 'en')
regiao = geocoder.description_for_number(numero, 'en')

print(numero)
print(timezone)
print(carrier)
print(regiao)