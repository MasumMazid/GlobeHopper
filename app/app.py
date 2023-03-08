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
  
  
    
@app.post('/countries')
def createCountry():
    data= request.json
    return countries.createCountry(data)




if __name__=='__main__':
    app.run(debug=True)
