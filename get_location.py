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
with open(input_doc_name) as f:
    reader = csv.reader(f)
    for row in reader:
        geocode_result = gmaps.geocode(row[0])
        print(row[0] + ',' + str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng']))
        with open(output_doc_name, "a") as file:
            output=(row[0] + ',' + str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng']) + '\n')
            write_result(output_doc_name, output)
