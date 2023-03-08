##Defines all countries in Country api

from flask import Flask, request, jsonify
import services


def getcountries():
    results= services.allcountries()
    data=[]
    for row in results:
        data.append({
            "CountryID": row[0],
            "Name" : row[1],
            "Population" : row[2],
            "Continent" : row[3]
            
        })  
    return jsonify(data)

def createcountry(data):
   services.createcountry(data)
   return jsonify({"message" : "Data inserted successfully"})

