# TripGenerator
Given an excel file with destinations, the TripGenerator returns the best combination to achieves all your destinations in a minimum of time in Python (Using Pandas, Csv, Requests, Numpy, Google API)

The Script is using Google API (Distance Matrix).
To run the script, you will need an API Key, provided from Google.
Please don't publish your API Key: API Key can generate costs if a lot of requests are made.

  The script takes a Excel Tabelle as entry.
  It converts the data in CSV (I feel more confident with Csv library).
  It store all destinations on an array and will try combinaisons to find the trip which requires a minimum of time.
  
The method used is the "Shortest time first".
It means that:
  For each start point, it calculate reaching time for each end point on the list
  It take the smallest time.
  The smallest time destination is taken as new start point and recalculate the new times with the end point remining.
  
The script is built that there is small functions and one main loop function. It makes easier to makes changes to independants functions.


I am sure the script could be better. Please feel free to propose any idea :)
