## Starting point of application
##pip install flask

from flask import Flask, request, jsonify
import countries



##Using Flask Framework
app=Flask(__name__)

##Read API

@app.get('/countries')
def getAllCountries():
    return countries.getCountries()
    
@app.get('/countries')
def getAllCities():
    return 






if __name__=='__main__':
    app.run()
