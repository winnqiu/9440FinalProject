import pandas as pd
import requests
import logging
import time
import csv 

API_KEY = 'AIzaSyAkcnNPhFjqJ4IXi2LuHfxVr4tO8kBhGv4'

output_filename = 'D:/Winn/Baruch College/2020Fall/CIS9440/GroupProject/data/Arrests/zipcoded.csv'

input_filename = "D:/Winn/Baruch College/2020Fall/CIS9440/GroupProject/data/Arrests/latlng.csv"

ColumnName='location'
# Return Full Google Results? If True, full JSON results from Google are included in output
RETURN_FULL_RESULTS = False



latlngs=[]
infile=open(input_filename,'r')
infile.readline()
for line in infile:
    latlngs.append(line)
infile.close()

def get_google_results(latlng, api_key=None, return_full_response=False):

    # Set up your Geocoding url
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={}".format(latlng)
    geocode_url = geocode_url + "&key={}".format(api_key)
    
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    results = results.json()
    # Results will be in JSON format - convert to dict using requests functionality
    if len(results['results']) == 0:
        output = '\n'
    else:    
        answer = results['results'][0]
        output = [x['long_name'] for x in answer.get('address_components') 
                                  if 'postal_code' in x.get('types')]
        sep='\n'
        output=sep.join(output)
    print(output)
    return output

outfile=open(output_filename,'w',newline='')
outfile.write('location\n')
for latlng in latlngs:
    geocode_result = get_google_results(latlng, API_KEY, return_full_response=RETURN_FULL_RESULTS)
    outfile.write(geocode_result+'\n')
            
outfile.close()







