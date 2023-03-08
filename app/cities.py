from flask import Flask, request, jsonify
import services




## Get landmarks
def getLandMark(CityId):
    results= services.getLandMarks(CityId)
    data=[]
    
    for row in results:
        data.append({
            "CityId": row[0],
            "Name" : row[1],
            "CountryId" : row[2],
            "Capital" : row[3],
            "FirstLandmark": row[4],
            "SecondLandmark" : row[5],
            "ThirdLandMark" : row[6]
        })  
    return jsonify(data)   


## Get All Cities
def getCities():
    results= services.getAllCities()
    data=[]
    for row in results:
        data.append({
            "CityId": row[0],
            "Name" : row[1],
            "CountryId" : row[2],
            "Capital" : row[3],
            "FirstLandmark": row[4],
            "SecondLandmark" : row[5],
            "ThirdLandMark" : row[6]
        })  
    return jsonify(data)

def deletecity(city_id):
   services.deletecitybyID(city_id)
   return jsonify({"message" : "deleted successfully"})

def createCity(data):
   services.createCities(data)
   return jsonify({"message" : "Data inserted successfully"})

def UpdateCity(data,city_id):
    services.updateTheCity(data,city_id)
    return jsonify({"message" : "City has been updated"})

def getCapital(country_id):
    results=services.GetTheCapital(country_id)
    data=[]
    for row in results:
        data.append({
            "CityId": row[0],
            "Name" : row[1],
            "CountryId" : row[2],
            "Capital" : row[3],
            "FirstLandmark": row[4],
            "SecondLandmark" : row[5],
            "ThirdLandMark" : row[6]
        })  
    return jsonify(data)