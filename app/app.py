## Starting point of application
##pip install flask

from flask import Flask, request, jsonify
import countries
import cities


##Using Flask Framework
app=Flask(__name__)

##Read API

@app.get('/countries')
def getallcountries():
    return countries.getcountries()


##Get capital Landmarks
@app.get('/cities/<CityId>')
def getLandMark(CityId):
    return cities.getLandMark(CityId)

##Get Countries in Continent
@app.get('/countries/<continent>')
def ContriesinContinent(continent):
    return countries.getcountriesincontinent(continent)
  
##Add Country
@app.post('/countries')
def createcountry():
    data= request.json
    return countries.createcountry(data)

## Delete Country
@app.delete('/countries/<int:country_id>')
def deletecountry(country_id):
    return countries.deletecountry(country_id)


## Put countries as in update country?

## Add new Capital
@app.post('/cities')
def createcity():
    data= request.json
    return cities.createCity(data)

## Get all Cities
@app.get('/cities')
def getallCities():
    return cities.getCities()



## Delete City
@app.delete('/cities/<int:city_id>')
def deletecity(city_id):
    return cities.deletecity(city_id)

## Update City?

if __name__=='__main__':
    app.run(debug=True)
