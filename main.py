import requests
import time
import datetime
import json
import csv
from math import radians, cos, sin, asin, sqrt
from src.jetList import *

airportcodes = open("src/AirportCodes.txt", "r")

with open('src/idtomodel.txt', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}


def idtomodel(icao):
    for each, val in dict_from_csv.items():
        model = "UFO"
        if each == icao:
            model = val
            return model
    return model


def fuel(model):
    for each in data:
        try:
            if model in each['Name']:
                return each["Fuel Burn (Hour)"]
            else:
                pass
        except:
            NoneType


def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    r = 6372.8  # Radius of earth in kilometers. Use 3959.87433 for miles.
    
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a)
    return c * r


def longlat(icao, firstSeen):
    if firstSeen is not None:
        r = requests.get(
            f'https://opensky-network.org/api/tracks/all?icao24={icao}&time={firstSeen}')
        print(f"{icao}, {firstSeen}, {type(firstSeen)}")
        print(r.text)
        flightrecord = json.loads(r.text)
        departureLong = flightrecord['path'][0][1]
        departureLat = flightrecord['path'][0][2]

        destinationlong = flightrecord['path'][-1][1]
        destinationlat = flightrecord['path'][-1][2]
        departure = f"{departureLong},{departureLat}"
        destination = f"{destinationlong},{destinationlat}"
        return haversine(departureLong, departureLat, destinationlong, destinationlat)
    else:
        print('Is not an integer')


def main():
    arrived = []
    CarbonEmissions = 0
    # Epoch time for start->end of yesterday
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    start_of_yesterday = int(time.mktime(yesterday.timetuple()))
    end_of_yesterday = int(time.mktime(today.timetuple()))

    # Retrieve flight arrival data from every airport ICAO code in AirportCodes.txt, combining the API response into arrived list
    for codes in airportcodes.readlines():
        stripped_line = codes.rstrip()
        r = requests.get(
            f'https://opensky-network.org/api/flights/arrival?airport={stripped_line}&begin={start_of_yesterday}&end={end_of_yesterday}')
        arrived.extend(r.json())
        print(
            f"Number of Flights from {stripped_line} airport: {len(r.json())}")
    print(f"Total flights : {len(arrived)}")

    # Process each flight if firstSeen and lastSeen are not None
    for flight in arrived:

        if flight['firstSeen'] and flight['lastSeen'] != None:
            firstSeen = flight['firstSeen']
            lastSeen = flight['lastSeen']
            icao = flight['icao24']
            model = idtomodel(flight['icao24'])
            fuelburn = fuel(model)

            # Further process if fuelburn and model are not None
            if fuelburn != None and model != None:
                # distance = longlat(icao, firstSeen)
                flighttime = (lastSeen - firstSeen) / 360
                gallons = float(flighttime) * float(fuelburn)
                CO2 = (gallons * 21.1) / 2000
                CarbonEmissions += CO2
                for x, vars in enumerate(stats):
                    stats[x] = round(vars, 2)
                print(
                    f"Model: {model}, Time (Hours): {stats[0]:,}, Fuel Burn Gallons(Hour): {stats[1]:,}, CO2 (Tons): {stats[2]:,}")
    return print(f"{stats[3]:,} Tons == {(stats[3] * 907.185):,} KG")


start_time = time.time()

if __name__ == '__main__':
    main()

print("--- %s seconds ---" % (time.time() - start_time))
