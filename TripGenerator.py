import pandas as pd
import csv
import requests
import numpy

# Take the API Key (secured by importing from .txt. Never write the API Key on source code)
def takeAPI():
    apiFile = open("ApiKey.txt","r")
    apiKey = apiFile.read()
    apiFile.close()
    return apiKey

# Goal Adresses are listed in a excel file. I extract them and put them into an Array
# I like to work with CSV. I convert Xlsx to CSV
def readAdressFiles():
    goalAdressXlsx = pd.read_excel("goalAdress.xlsx")
    goalAdressXlsx.to_csv("goalAdress.csv")

    destinationRemain = []
    with open("goalAdress.csv") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # I only want to see the column with adresses. Others informations does not have interest
            destinationRemain.append(row[1])
        csvFile.close()
    return destinationRemain

# I know start point. I have a list of End point. I will always choose the End point with the lower travel time.
# I make a travel time request on google map for each End point, knowing the Start point.
# I choose the lower travel time and affect the End point choosen as the new Start point.
# Then iterate the process until there is no End point anymore (array empty)
def requestTimeOnGoogleMap(homeAdress,destinationRemain):
    # Make the request on Google Map
    baseUrl = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

    # List all time duration for each destination
    timeResponse = []
    for destination in destinationRemain:
        responseSingle = requests.get("{}origins={}&destinations={}&key={}".format(baseUrl, homeAdress, destination,apiKey))
        # I want our response to be in time (seconds)
        timeResponseSingle = responseSingle.json()["rows"][0]["elements"][0]["duration"]["value"]
        timeResponse.append(timeResponseSingle)

    # Affect each destination to his time duration
    listDestinationTime = []
    for t in range(len(destinationRemain)):
        listDestinationTime.append([destinationRemain[t],timeResponse[t]])
    # Sort all destinations by time
    listDestinationTime.sort(key=lambda index: index[1])
    # Take the first one in the list. This is the destination with the lower time duration
    destinationChoose = listDestinationTime[0][0]
    # Create an Array with all remain destinations to reach
    destinationRemain.remove(destinationChoose)

    return destinationChoose, destinationRemain



apiKey = takeAPI()
trip = []
# Take the starting point (in my case, it is always the same. I write it on source code)
homeAdress = "geisbachstrasse, 56072 Koblenz"
trip.append(homeAdress)
destinationRemain = readAdressFiles()
def loop(homeAdress,destinationRemain):
    while (len(destinationRemain) != 0):
        homeAdress, destinationRemain = requestTimeOnGoogleMap(homeAdress,destinationRemain)
        # For each adress choosen, I append it on the trip list which is the end returned list for the best travel (with lower time)
        trip.append(homeAdress)
    print("The trip is calculated: {}".format(trip))
loop(homeAdress,destinationRemain)