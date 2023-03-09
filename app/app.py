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


##Get capital Information for traveller GH 6
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
@app.put('/countries/<int:country_id>')
def updatecountry(country_id):
    data= request.json
    return countries.UpdateCountry(data,country_id)


## Add new City for travel agent  "GH-12 <message>"
@app.post('/cities')
def createcity():
    data= request.json
    return cities.createCity(data)

## Get all Cities
@app.get('/cities')
def getallCities():
    return cities.getCities()

## Get capital
@app.get('/countries/<int:country_id>')
def getCapital(country_id):
    return cities.getCapital(country_id)


## Delete City
@app.delete('/cities/<int:city_id>')
def deletecity(city_id):
    return cities.deletecity(city_id)

##  Put Update City?
@app.put('/cities/<int:city_id>')
def updatecity(city_id):
    data= request.json
    return cities.UpdateCity(data,city_id)

if __name__=='__main__':
    app.run(debug=True)
