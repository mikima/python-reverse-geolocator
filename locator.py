from geopy.geocoders import Nominatim
import json, csv

print('pronto')

geolocator = Nominatim()
location = geolocator.reverse("48.8588443, 2.2943506")
#
print(location.raw['address'])

#load csvstate

with open('data/airbnb-places.txt') as csvfile:
	readCSV = csv.reader(csvfile, delimiter='\t')
	for row in readCSV:
		try:
			loc = geolocator.reverse(row[1]+","+ row[2], timeout=1000, language='en')
			country = loc.raw['address']['country']
			region = loc.raw['address']['state']
			print("\t".join([row[1], row[2], country, region]))
		except Exception as e:
			print(row[1], row[2], 'error')
