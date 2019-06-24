import googlemaps
import csv
from keys import google_API_key
gmaps = googlemaps.Client(key=google_API_key)
input_doc_name = 'addresses.csv'
output_doc_name = "result.csv"
text = 'adress,latitude,longitude\n'
def write_result(output_doc_name, text):
    with open(output_doc_name, "a") as file:
        file.write(text)
write_result(output_doc_name, text)
def geocode(input_doc_name):
    with open(input_doc_name) as f:
        reader = csv.reader(f)
        for row in reader:
            geocode_result = gmaps.geocode(row[0])
            print(row[0] + ',' + str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng']))
            with open(output_doc_name, "a") as file:
                output=(row[0] + ',' + str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng']) + '\n')
                write_result(output_doc_name, output)

def reverse_geocode(input_doc_name):
    with open(input_doc_name) as f:
        reader = csv.reader(f)
        for row in reader:
            reverse_geocode_result = gmaps.reverse_geocode((row[0], row[1]))
            print(reverse_geocode_result)

reverse_geocode('reverse.csv')